import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from pathlib import Path

st.set_page_config(page_title="HOME | Population Pyramids")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    "<h1 style='text-align: center;'>Population Pyramids</h1>",
    unsafe_allow_html=True,
)
st.write("")

data = pd.DataFrame(
    {
        "cities": [
            "Tokyo",  # japan
            "Washington D.C.",  # usa
            "New Delhi",  # india
            "Nairobi",  # kenya
            "Berlin",  # germany
            "Rio de Janeiro",  # brazil
        ],
        "lat": [35.6762, 38.9072, 28.65381, -1.28333, 52.52437, -22.90278],
        "lon": [139.6503, -77.0369, 77.22897, 36.81667, 13.41053, -43.2075],
    }
)

midpoint = (np.average(data["lat"]), np.average(data["lon"]))
st.map(data, zoom=0.5, use_container_width=True)

with st.container():
    st.write("---")
    st.markdown(
        "<h5 style='text-align: center;'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porta arcu sed lorem ultricies, et gravida mauris dapibus. Duis elementum ipsum velit, nec efficitur libero accumsan at. Pellentesque viverra accumsan sem, in auctor augue gravida sit amet. Duis commodo ultrices nulla at lacinia. Aenean magna lectus, sollicitudin a velit vitae, finibus pretium erat. Donec eget pulvinar lacus. Donec porttitor tellus nec dapibus elementum.</h5>",
        unsafe_allow_html=True,
    )

st.sidebar.write(
    """
    ## About this app
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porta arcu sed lorem ultricies, et gravida mauris dapibus. Duis elementum ipsum velit, nec efficitur libero accumsan at. Pellentesque viverra accumsan sem, in auctor augue gravida sit amet. Duis commodo ultrices nulla at lacinia. Aenean magna lectus, sollicitudin a velit vitae, finibus pretium erat. Donec eget pulvinar lacus. Donec porttitor tellus nec dapibus elementum.
    """
)
