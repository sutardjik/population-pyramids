# Population Pyramid Visualizer

Explores the population trends of six countries—the USA, Brazil, Germany, Kenya, India, and Japan—from 1950 to 2020 through population pyramids and annual population growth line graphs.

Written in Python using Streamlit.

Site: https://sutardjik-population-pyramids-home-vqx83m.streamlit.app/

## Homepage

- OpenStreetMap
  - Pinned locations of countries’ capitals
    - Hover on capital to view name
    - Click on capital to see geographic coordinates
- Individual Mapbox displays for each country
- Click on country name to access its page
- View complete list of pages and web app’s outlined features through sidebar

## Countries

- Population pyramid alters according to chosen year with interactive slider
  - Data source link directs to specified year’s PopulationPyramid.net page
- Annual population growth line graph
- Interactive data frames
  - Data used to create pyramids and line graphs
    - Query by column name
    - Download as Excel spreadsheet

## Country Comparison

- Annual population growth multiple-line graph for all six countries
  - Line trace can be excluded through single/double-click
- Sidebar displays description of trend observations

## Download Requirements

- Streamlit version 1.18.1
- Type `streamlit run HOME.py` in command prompt to run app
