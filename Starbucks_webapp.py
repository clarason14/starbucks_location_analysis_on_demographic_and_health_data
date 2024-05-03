import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pydeck as pdk


tab1, tab2 = st.tabs(["Project Overview", "Main Page"])
with tab1:
    st.title('Starbucks Location Analysis based on Demographic and Health Data')
    st.subheader('By HaYoung (Clara) Son')
    st.write('Welcome to the analysis tool that explores the correlation between the number of Starbucks locations with demographics, and health data!')
    st.write('Please click the tab [Main Page] to actually view the Maps and Analysis!')

    st.subheader('Overview')
    st.write("1. Starbucks Location Map")
    st.write('    * Visualizes the number of Starbucks locations across different ZIP codes in Los Angeles. Users can interact with the map to view specific areas, and the intensity of the color on the map indicates the density of Starbucks locations. This helps to quickly grasp which areas have higher concentrations of Starbucks stores relative to others.'
    )
    st.write("2. Preview of the Dataset : First 10 rows")
    st.write("    * Displays the first 10 rows of the dataset including the number of Starbucks per ZIP code, health, and demographic data. This preview gives a snapshot of the data structure and helps users understand the types of information available for analysis.")

    st.write("3. Full Correlation Matrix Table")
    st.write("    * The full correlation matrix table is shown, allowing users to examine the relationships between all variables at once. This matrix is useful for identifying potential relationships and patterns across multiple data dimensions simultaneously.")

    st.write("4. Correlations with Number of Starbucks")
    st.write("    * This section presents the sorted correlation values between the number of Starbucks locations and each demographic and health variable in the dataset. The correlations are displayed in a user-friendly format, highlighting which factors are most and least associated with Starbucks locations. This aids in pinpointing significant influencers of Starbucks site selection.")

    st.write("5. Correlation Matrix Heatmap")
    st.write("    * A heatmap of the correlation matrix is displayed, using a color scale to indicate the strength and direction of correlations. Warm colors represent positive correlations while cool colors denote negative correlations. This visualization allows users to quickly capture the relationships between variables at a glance, facilitating easier interpretation of complex data relationships.")

    st.subheader('Sidebar Overview')

    st.write('1. Zip Code Search')
    st.write('    * Users can enter a ZIP code in the sidebar to fetch and display specific data for that area. Zip code 90007 for USC Campus is inputted as default value.')

    st.write('2. Select Demographic / Health Variable to Display Correlation')
    st.write('    * A dropdown menu in the sidebar lets users select a demographic or health variable from the dataset. The web application then calculates and displays the correlation coefficient between the selected variable and the number of Starbucks locations. ')

    st.subheader("Conclusion")  
    # Data from your correlation analysis
    data = {
        "PHLTH": [-0.2594162],
        "DIABETES": [-0.257205139],
        "Total Housing Units": [0.23464035432495128],
        "Median Contract Rent": [0.22183310673351067],
        "ACCESS2": [-0.219196115],
        "OBESITY": [-0.19347185],
        "DENTAL": [0.19283212672154643],
        "Total Labor Force Participation (Age 16+)": [0.1316778848698969],
        "MHLTH": [-0.103008613],
        "Median Household Income": [0.099931233],
        "Total Unemployment (Age 16+)": [0.092470457],
        "Total Population": [0.079060846],
        "CHECKUP": [0.024049007],
        "Zip Code": [-0.020449123]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Sort the DataFrame by values while keeping 'Zip Code' at the front
    sorted_columns = sorted(df.columns.difference(['Zip Code']), key=lambda col: df[col].iloc[0])
    sorted_columns = ['Zip Code'] + sorted_columns  # Adding 'Zip Code' to the front

    # Reorder DataFrame according to sorted column names
    df = df[sorted_columns]

    # Display the DataFrame in Streamlit
    st.dataframe(df)
    
    st.write('    * The analysis of the correlation between Starbucks locations per ZIP code and various health and demographic variables in Los Angeles revealed unexpectedly low correlations, contradicting the initial hypothesis. Most variables, such as physical health, diabetes prevalence, and median household income, showed weak correlation coefficients (ranging from -0.26 to +0.23), suggesting that Starbucks location strategy in Los Angeles may not be significantly influenced by these factors. This finding could be attributed to the unique socio-economic landscape of Los Angeles or the omission of other influential factors like property costs or zoning laws. Future research should consider a broader geographic scope (such as entire United States or Global scale) and additional variables to better understand the factors driving Starbucks location decisions.')

    st.subheader("Major Gotchas or Possible Improvements")

    st.write('1. Possible Way to Improve Starbucks Location Map')
    st.write('    * One way to improve the Starbucks Location Map is by adding  interactive layers for demographic and health variables on the map. This feature would enable users to overlay data such as total population or housing units with Starbucks locations, offering deeper insights into socio-economic patterns. While this would enhance user interaction and analysis, it requires careful planning for data management and map performance, especially when adding multiple layers.')

    st.write('2. Broader Geographic Scope')
    st.write('    * Expanding the scope of our analysis from Los Angeles to a nationwide or even global scale could potentially uncover stronger correlations between Starbucks locations and demographic or health data. While this broader has higher difficulty in gathering consistent ZIP code-specific data across different regions, it could provide a more comprehensive understanding of the factors influencing Starbucks location strategy.')

with tab2:

    st.title('Starbucks Location Analysis based on Demographic and Health Data')

    FILE_PATH = 'starbucks_health_location_demographic_merged.csv'
    ZIP_DATA_PATH = 'California_zipcode_longitude_latitude.csv'

    @st.cache_data
    def load_data(filepath):
        data = pd.read_csv(filepath)
        data['Zip Code'] = data['Zip Code'].astype(str).str.zfill(5)  # Ensure Zip Code is a string with leading zeros
        return data

    @st.cache_data
    def load_location_data(zip_data_filepath, starbucks_data_filepath):
        zip_data = pd.read_csv(zip_data_filepath)
        starbucks_data = pd.read_csv(starbucks_data_filepath)
        
        # Calculating number of Starbucks per ZIP code
        starbucks_counts = starbucks_data['Zip Code'].value_counts().reset_index()
        starbucks_counts.columns = ['Zip Code', 'NumberOfStarbucks']
        
        # Merging the Starbucks count data with the ZIP code data
        merged_data = pd.merge(zip_data, starbucks_counts, left_on='Zip', right_on='Zip Code', how='left')
        merged_data['NumberOfStarbucks'].fillna(0, inplace=True)
        
        return merged_data

    # Load your main dataset
    df_merged = load_data(FILE_PATH)

    # Prepare the location data for the map
    location_data = load_location_data(ZIP_DATA_PATH, FILE_PATH)

    # Function to create the map layer
    def create_starbucks_map_layer(data):
        max_starbucks = data['NumberOfStarbucks'].max()
        
        return pdk.Layer(
            "ScatterplotLayer",
            data,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=["Longitude", "Latitude"],
            get_fill_color="[0, 255, 0, NumberOfStarbucks / max_starbucks * 255]",  # Shade of green based on count
            get_line_color=[0, 0, 0],
        )

    # Create the map layer
    starbucks_layer = create_starbucks_map_layer(location_data)

    # Set the viewport location for the map
    view_state = pdk.ViewState(
        longitude=-118.24878,
        latitude=33.972914,
        zoom=5,
        min_zoom=1,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36
    )

    # Render the map
    st.subheader('Starbucks Location Map:')

    r = pdk.Deck(layers=[starbucks_layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v9')
    st.pydeck_chart(r)

    # Sidebar interaction for ZIP code search
    st.sidebar.subheader('Display Data for Your Zipcode ')
    default_zip_code = '90007'
    search_zip_code = st.sidebar.text_input('Enter a ZIP code', default_zip_code)
    if search_zip_code:
        # Ensure the input is a zero-padded string to match the format in the dataframe
        search_zip_code = search_zip_code.zfill(5)
        search_result = df_merged[df_merged['Zip Code'] == search_zip_code]
        if not search_result.empty:
            st.sidebar.write('Displaying data for ZIP code:', search_zip_code)
            st.sidebar.dataframe(search_result)
        else:
            st.sidebar.warning('No data found for this ZIP code.')

    # Sidebar selection for variable correlation
    st.sidebar.subheader('Display Correlation')
    st.sidebar.write('Select a variable to view its correlation with the number of Starbucks:')
    exclude_columns = ['Zip Code', 'NumberOfStarbucks']  # Exclude non-analytical columns
    options = [col for col in df_merged.columns if col not in exclude_columns]
    selected_variable = st.sidebar.selectbox("Select a variable", options)
    if selected_variable:
        correlation_value = df_merged['NumberOfStarbucks'].corr(df_merged[selected_variable])
        st.sidebar.write(f'Correlation between NumberOfStarbucks and {selected_variable}: {correlation_value:.2f}')

    # Display the first 10 rows of the dataframe
    st.subheader('Preview of the Dataset (first 10 rows):')
    st.dataframe(df_merged.head(10))

    # Display correlation matrix as a table
    st.subheader('Full Correlation Matrix Table:')
    corr_matrix = df_merged.corr()
    st.dataframe(corr_matrix)

    # Sorted correlation values with NumberOfStarbucks, presented horizontally, showing negative values
    st.subheader('Correlations with NumberOfStarbucks:')
    num_starbucks_corr = corr_matrix['NumberOfStarbucks'].drop('NumberOfStarbucks').sort_values(ascending=False, key=abs)
    st.dataframe(num_starbucks_corr.to_frame().T)  # Transpose to display horizontally

    # Visualize correlation matrix
    st.subheader('Correlation Matrix Heatmap:')
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    st.pyplot(plt)

