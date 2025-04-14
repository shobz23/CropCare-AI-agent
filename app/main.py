import streamlit as st
from app.image_diagnosis import diagnose_image
from app.text_support import handle_text_query

st.title("Crop Doctor - AI Plant Health Assistant")

option = st.radio("Choose Input Method:", ("Upload Image", "Text Query"))

if option == "Upload Image":
    image = st.file_uploader("Upload a plant image")
    if image:
        result = diagnose_image(image)
        st.write(result)

elif option == "Text Query":
    query = st.text_input("Describe the problem")
    if query:
        response = handle_text_query(query)
        st.write(response)
