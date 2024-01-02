import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide")
st.markdown("""
<style>
.css-18ni7ap.e8zbici2  /*default menu of streamlit library*/
{
    visibility: hidden;
}
.st-emotion-cache-vk3wp9.eczjsme11/*sidebar of MultipageApp*/
{
    visibility: hidden;
    margin-left: -350px;
}
.st-emotion-cache-18ni7ap.ezrtsby2
{
    visibility: hidden;
}

.appview-container.css-1wrcr25.egzxvld6  /*Whole page*/
{
    background-color:Beige;
    margin-bottom:-150px;
}
    
.css-1v0mbdj.etr89bj1 /* XAIface logo */
{
    text-align: center;
    display: block;
    margin-top: -5px;
    width: 100%;
    margin-left: 100px;
    margin-right: 100px;

}

.css-1kyxreq.etr89bj2
{
margin-left: 100px;
}

div.stButton > button:first-child 
{ 
    background-color: #D3D3D3;
    border-radius: 20%;
    height: 3.5em;
    width: 180px; 
    margin-top: 70px;
    margin-left:900px; 
}

div[data-testid="stMarkdownContainer"] p {
    font-size: 34px;
    font-family: Arial; 
    font-weight: bold;
}

</style>
""", unsafe_allow_html = True)

st.markdown("<h1 style='margin-left:200px;text-align: center;  color: Grey; font-size:54px; margin-top: 55px; font-family: Sans-Serif;'>Welcome to the XAIface Project Demo</h1>", unsafe_allow_html=True)
image = Image.open("xaiface_logo_PNG.png")
image = image.resize((550, 350))
st.image(image)

st.markdown("<h5 style='margin-left:200px; text-align: center;  color: red; font-size:30px; margin-top: 60px; margin-bottom: -10px; font-family: Sans-Serif; '>Please press F11 on your keyboard to enter the full screen mode</h5>", unsafe_allow_html=True)
naima ="Start"
strat_button = st.button(label=naima)

if strat_button:
    switch_page("interface")
