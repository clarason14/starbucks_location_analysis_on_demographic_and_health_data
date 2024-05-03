import streamlit as st

tab1, tab2 = st.tabs(["Project Analysis Questions", "Data Description"])
with tab1:
    st.write("4.	What did you set out to study?  ")

    st.write("5.	What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?)")

    st.write("6.	What difficulties did you have in completing the project?  ")

    st.write("7.	What skills did you wish you had while you were doing the project?")

    st.write("8.	What would you do “next” to expand or augment the project?    ")

with tab2:
    st.write("Dataset 1: Starbucks Location Data")
    st.write('This dataset was created by scraping the official Starbucks store locator website, gathering detailed information on Starbucks locations across Los Angeles. The data was filtered using LA ZIP codes sourced from a public LA County data repository. The scraping process yielded detailed information on each location, which was then aggregated to show the number of Starbucks locations per ZIP code, ensuring there were no duplicates, and saved in the file starbucks_LA_counts_per_zipcode.csv.')

    st.write('Dataset 2: Demographics Data by ZIP Code')
    st.write('Sourced from the United States Census Bureau API, specifically the American Community Survey 5-Year Data for 2022, this dataset provides comprehensive demographic metrics such as total population, median household income, and employment rates. Only data pertaining to the Los Angeles ZIP codes listed in LA_City_ZIP_code.csv were collected, and the pertinent demographic data were saved in LA_demographics_by_zipcode.csv.')
