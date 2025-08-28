import io

import pandas as pd
import requests
import streamlit as st

url = "https://data.cnra.ca.gov/dataset/78ac95ac-9665-4e53-aea6-ad0762055cce/resource/4e6aaf6f-7055-484b-84f4-3a66df294f27/download/2020-09-11_microparticledata.xlsx"
sheet_name = "fish"


def read_excel_from_url(url: str, sheet_name: str=None) -> pd.DataFrame:
    response= requests.get(url)
    data = io.BytesIO(response.content)
    return pd.read_excel(data, sheet_name="fish")


if __name__=='__main__':
    url = "https://data.cnra.ca.gov/dataset/78ac95ac-9665-4e53-aea6-ad0762055cce/resource/4e6aaf6f-7055-484b-84f4-3a66df294f27/download/2020-09-11_microparticledata.xlsx"
    sheet_name = "fish"

    st.title("Streamlit Example")
    st.header("Day 2")
    st.subheader("Example 7")

    
    df = read_excel_from_url(url, sheet_name)

    st.text("Fishery Data Frame")
    st.dataframe(df[["SampleDate", "Latitude", "Longitude", "CommonName", "Count", "Weight", "UnitWeightFish"]])
    
    st.text("Fishery Data Editor")
    edited_df = st.data_editor(df[["SampleDate", "Latitude", "Longitude", "CommonName", "Count", "Weight", "UnitWeightFish"]])
    edited_df.to_excel("edited_data.xlsx")
