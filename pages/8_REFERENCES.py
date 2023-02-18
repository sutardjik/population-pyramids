import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="References • Population Pyramid Visualizer")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
st.markdown("<h1 style='text-align: center;'>References</h1>", unsafe_allow_html=True)

add_vertical_space(1)

st.markdown(
    "“Population of Germany 2020.” PopulationPyramid.net. Accessed February 17, 2023. https://www.populationpyramid.net/germany/2020/.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "“Population of Japan 2009.” PopulationPyramid.net. Accessed February 17, 2023. https://www.populationpyramid.net/japan/2009/.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "Rutherford, Jill and Gillian Williams. <i>Environmental Systems and Societies: Course Companion</i>. United Kingdom: Oxford University Press, 2015. http://ionma.org/share/ess/essbookcomplete.pdf.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "Saroha, Jitender. “Types and Significance of Population Pyramids.” <i>World Wide Journal of Multidisciplinary Research and Development</i> 4, no. 4 (2018): 59. http://wwjmrd.com/upload/types-and-significance-of-population-pyramids_1523552342.pdf.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "“Tools of the Trade: POPULATION PYRAMIDS.” Pennsylvania Department of Health. Accessed February 17, 2023. https://www.health.pa.gov/topics/HealthStatistics/Statistical-Resources/UnderstandingHealthStats/Documents/Population_Pyramids.pdf.",
    unsafe_allow_html=True,
)

st.write("---")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    pass
with col2:
    pass
with col3:
    previous_button = st.button("⟵ PREV")
    if previous_button:
        switch_page("COUNTRY_COMPARISON")
with col4:
    previous_button = st.button("NEXT ⟶")
    if previous_button:
        switch_page("HOME")
with col5:
    pass
with col6:
    pass
