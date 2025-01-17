import streamlit as st
import time
import subprocess


st.text("This app takes your text as an input and propose tags for your message\n\
        The tag attributiuon was trained on stackoverflow questions in March2023\n\n\
        type a sentence or copy paste this exmaple: \n\
        'I want to integrate java script in python notebook to display dynamic images'\n")

# with st.spinner('Installing dependencies...'):
#     subprocess.run(["streamlit", "cache", "clear"])
#     time.sleep(0.05)
#     subprocess.check_call(["python3", "-m", "pip", "install", "-r", "requirements.txt"])
#     st.success("Dependencies installed successfully!")

import requests
import pandas as pd

from utils.text_pre_processing import clean_text, make_tokens
from utils.tag_prediction import predict_tag

def main():
    st.title("Text Processing API")

    text = st.text_area("Enter your text:")

    if st.button("Process Text"):
    

            
        text_ready = clean_text(text)
        tokens_ready = make_tokens(text_ready)

        st.text("Processed Text:")
        st.text(tokens_ready)
        tag_predicted, proba = predict_tag(tokens_ready)
        
        st.subheader("Top 3 sugested tag and associated confidence percentage are:")
        for i in [0,1,2]:
            st.success((tag_predicted[i], proba[i]))

    

if __name__ == '__main__':
    main()

