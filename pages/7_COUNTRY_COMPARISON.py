import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly_express as px
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
import io

st.set_page_config(page_title="Country Comparison • Population Pyramid Visualizer")


@st.cache_data
def get_data():
    df = pd.read_excel("data/6-Growth-1950-2020.xlsx")
    return df


df = get_data()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    "<h1 style='text-align: center;'>Country Comparison</h1>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<h4>Six Countries’ Annual Population Growth Multiple-Line Graph</h4>",
    unsafe_allow_html=True,
)
fig = px.line(
    df,
    x="Year",
    y="Population",
    title="Annual Population Growth of Six Countries (1950 – 2020)",
    color="Country",
    markers=True,
    height=700,
)
fig.update_layout(
    font_family="sans-serif",
    title_font_family="adelle-sans",
    title_font_size=16,
    font=dict(family="adelle-sans"),
    yaxis_title="Population (Billions)",
)
st.plotly_chart(fig)

st.markdown(
    "<p>To exclude any of the lines in the graph, locate the graph’s legend on the right and click on any of the line names. The name on the legend slightly fades when excluded. Click on a semi-faded line name to redisplay a line.</p>",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<p>Double-clicking a non-faded line name will remove all lines besides the double-clicked name. Double-click any semi-faded name to reinclude all lines back in the graph.</p>",
    unsafe_allow_html=True,
)

add_vertical_space(1)
st.markdown(
    "<p>An overview of observations in the multiple-line graph trends is included in the left sidebar.</p>",
    unsafe_allow_html=True,
)
st.write("---")

st.markdown(
    "<h4>Six Countries’ Annual Population Growth Data (1950 – 2020)</h4>",
    unsafe_allow_html=True,
)
filtered_df = dataframe_explorer(df)
s = filtered_df.style.format({"Year": lambda x: "{:.0f}".format(x)})
st.dataframe(s, use_container_width=True)

col1, col2, col3 = st.columns(3)
buffer = io.BytesIO()
with col1:
    pass
with col2:
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="6-Growth-1950-2020")
        writer.close()
        st.download_button(
            label="DOWNLOAD TABLE DATA",
            data=buffer,
            file_name="6-Growth-1950-2020.xlsx",
            mime="application/vnd.ms-excel",
        )
    buffer.flush()
    buffer.close()
with col3:
    pass

st.write("---")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    pass
with col2:
    pass
with col3:
    previous_button = st.button("⟵ PREV")
    if previous_button:
        switch_page("JAPAN")
with col4:
    next_button = st.button("NEXT ⟶")
    if next_button:
        switch_page("REFERENCES")
with col5:
    pass
with col6:
    pass

add_vertical_space(1)

st.markdown(
    "<sup>5 </sup>“Population of Japan 2009,” PopulationPyramid.net, accessed February 17, 2023, https://www.populationpyramid.net/japan/2009/.",
    unsafe_allow_html=True,
)

add_vertical_space(1)

st.markdown(
    "<sup>6 </sup>“Population of Germany 2020,” PopulationPyramid.net, accessed February 17, 2023, https://www.populationpyramid.net/germany/2020/.",
    unsafe_allow_html=True,
)

st.sidebar.write(
    """<h1>Observations</h1>
    <p>The multiple-line graph shows diverse population growth patterns within 70 years. India had the six countries’ steepest population growth and remained the most populous of the six. Meanwhile, Kenya is the least populous, with a gradual growth incline.

Not all nations see consistent population growth. Japan peaked in 2009 with its population at 128.117M and had a persistent drop afterward.<sup>5</sup> The causes of population reduction differ amongst nations from the effects of political or environmental events.

A noteworthy observation is Germany’s annual population growth, which fluctuates more often compared to other countries. The trend shows an increase from 1950 to 1973, a decline until it reached its valley in 1984, another increase where it peaked in 1999, a decline up to 2006, and one more increase until 2020.<sup>6</sup> Although Germany reached its all-time peak in 2020, the future trend of its population has yet to be forecasted.

Contrarily, The USA, Brazil, Kenya, and India witnessed ongoing population growth throughout the 70 years interval.</p>""",
    unsafe_allow_html=True,
)
