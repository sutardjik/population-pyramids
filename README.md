# Population Pyramid Visualizer

Explores the population trends of six countries—the USA, Brazil, Germany, Kenya, India, and Japan—from 1950 to 2020 through population pyramids and annual population growth line graphs.

Written in Python using Streamlit. Site: https://sutardjik-population-pyramids-home-vqx83m.streamlit.app/.

## Homepage

- Folium map
  - Pinned locations of countries’ capitals
    - Hover on capital to view name
    - Click on capital to see geographic coordinates
- Individual Mapbox displays for each country
- Click on country name to access its page
- View complete list of pages and web app’s outlined features through sidebar

## Countries’ Pages

- Population pyramid alters according to chosen year with interactive slider
  - Data source link directs to specified year’s PopulationPyramid.net page
- Annual population growth line graph from 1950 to 2020
- Interactive data frames
  - Data used to create pyramids and line graphs
    - Query according to column name
    - Download as Excel spreadsheet

## Country Comparison Page

- Annual population growth multiple-line graph for all six countries
  - Line trace can be excluded through single/double-click
- Sidebar displays description of trend observations

## References Page

- Lists sources used to gather data and research information in Chicago style

## Download Requirements

- Streamlit version 1.18.1
- In command prompt, type `streamlit run HOME.py`
