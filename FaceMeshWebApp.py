
"""

    PROJECT: Face Mess Detection Web
    MADE BY: Mohd Ali Bin Naser
    GITHUB : github.com/mohdalibn

"""

# Importing the required libraries for the project
import streamlit as st
import mediapipe as mp
from PIL import Image
import numpy as np
import tempfile
import time
import cv2


# Setting the Title of the Streamlit App
st.title('Face Mesh Detection Web App')


# Adding the SideBar Markdown
st.markdown(
    """

    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:350px}

    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width:350px
        margin-left: -350px
        }
    </style>

    """,

    unsafe_allow_html=True,

)

st.sidebar.title('Face Mesh Controls')  # Sidebar Title
st.sidebar.subheader('parameters')  # Sidebar subheading


# This function is going to resize the User selected Image or Video File so that it fits within the assigned space in the Web App
@st.cache()
def FrameResize(Frame, FrameWidth=None, FrameHeight=None, InterpolationMtd=cv2.INTER_AREA):
    FrameDimensions = None
    height, width, _ = Frame.shape

    # We simply return the Image or Video Frame if both the Width and Height are None
    if FrameWidth is None and FrameHeight is None:
        return Frame

    # This statement executes if only the FrameWidth is None
    if FrameWidth is None:
        result = FrameWidth / float(width)
        FrameDimensions = (int(width * result), FrameHeight)

    else:
        result = FrameWidth / float(width)
        FrameDimensions = (FrameWidth, int(height * result))

    # Here, we resize the frame using the calculated values above using opencv
    ResizedFrame = cv2.resize(Frame, FrameDimensions,
                              interpolation=InterpolationMtd)

    # Return the new Resized Frame
    return ResizedFrame
