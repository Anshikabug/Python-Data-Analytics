import streamlit as st
import pandas as pd
import plotly.express as px 

#ui configuration
st.set_page_config(
    page_title="Pokemon App",
    page_icon="🐰",
    layout="wide"
)
# load data
@st.cache_data
def load_data():
    return pd.read_csv("Pokemon.csv",index_col="#")

# integration
with st.spinner("loading dataset..."):
    df=load_data()
    # st.snow()

st.title("Pokemon Data Analytics")
st.subheader("A simple data app to analyze Pokemon data")

st.sidebar.title("Menu")
choice=st.sidebar.radio("Options",["View Data","Visualize Data"])

if choice == "View Data":
    st.header("View Dataset")
    st.dataframe(df)
else:
    st.header("Visualization")
    cat_cols=df.select_dtypes(include="object").columns.tolist()
    num_cols=df.select_dtypes(exclude="object").columns.tolist()
    cat_cols.remove("Name")
    num_cols.remove("Generation")
    num_cols.remove("Legendary")
    cat_cols.append("Generation")
    cat_cols.append("Legendary")
    snum_cols=st.sidebar.selectbox("Select a numeric column",num_cols)
    scat_cols=st.sidebar.selectbox("Select a categorical column",cat_cols)

    c1,c2 =st.columns(2)
    # visualize numerical column 
    fig1=px.histogram(df,
                      x=snum_cols,
                      title=f"Distribution of{snum_cols}"
                      )
    
    # visualize categorical column
    fig2= px.pie(df,
                 names=scat_cols,
                 title=f"Distribution of {scat_cols}",
                 hole=0.3
                 )
    c1.plotly_chart(fig1)
    c2.plotly_chart(fig2)

    fig3=px.box(df,x=scat_cols,y=snum_cols,title=f"{snum_cols} by {scat_cols}")
    st.plotly_chart(fig3)
    fig4= px.treemap(df,
                 path=["Generation","Type 1"],
                 title=f"Pokemon Type Distribution"
     )
    st.plotly_chart(fig4)

# to run this program, open terminal and run the following command
# streamlit run app.py