import streamlit as st
import pandas as pd

st.set_page_config(page_title = 'Pattern data Check tool')
st.title('Pattern data Check tool')

st.subheader('Input your Factory Piece data CSV')

upload_file_1 = st.file_uploader('choose the factory piece data csv file', type='csv')
if upload_file_1:
    st.markdown('---')
    df1 = pd.read_csv(upload_file_1)
    st.dataframe(df1)

st.subheader('Input SS Piece data CSV')
upload_file_2 = st.file_uploader('choose the SS piece data csv file', type='csv')
if upload_file_2:
    st.markdown('---')
    df2 = pd.read_csv(upload_file_2)
    st.dataframe(df2)

st.subheader('Comparison Table') 

if upload_file_1 and upload_file_2: 
    df1['Piece Name'] = df1['Piece Name'] + '_'+df1['Size']
    df2['Piece Name'] = df2['Piece Name'] +'_'+ df2['Size']

    df1.drop(['Size', 'Marker Date/Time', 'User Last Mod', 'Created Time', 'User Created','Prev Mod Time','User Prev Mod'], axis=1, inplace = True)
    df2.drop(['Size', 'Marker Date/Time', 'User Last Mod', 'Created Time', 'User Created','Prev Mod Time','User Prev Mod'], axis=1, inplace = True)

    merged_df = df1.merge(df2, on = 'Piece Name',how = 'outer', suffixes=('_Factory','_SS'))

    common_columns = ['Single Piece Perimeter', 'Shrink/Stretch X', 'Shrink/Stretch Y']  # replace with your actual column names

    for column in common_columns:
     merged_df[column + '_difference'] = merged_df[column + '_Factory'] - merged_df[column + '_SS']

    
    st.dataframe(merged_df)
    st.download_button(("Download Comaprison CSV"), merged_df.to_csv(), file_name="Comparison.csv", mime = 'test/csv')


