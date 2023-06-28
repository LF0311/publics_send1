import streamlit as st
import time
import requests


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    f'''
        <style>
            .reportview-container .sidebar-content {{
                padding-top: {0}rem;
            }}
            .appview-container .main .block-container {{
                {f'max-width: 100%;'}
                padding-top: {0}rem;
                padding-right: {1}rem;
                padding-left: {1}rem;
                padding-bottom: {0}rem;
                overflow: auto;
            }}
        </style>
        ''',
    unsafe_allow_html=True,
)

st.subheader("  ")

colmns0 = st.columns([1, 8, 1], gap="medium")

with colmns0[1]:
    st.markdown(
        '<nobr><p style="text-align: center;font-family:sans serif; color:Black; font-size: 32px; font-weight: bold">环境传感器目标识别平台</p></nobr>',
        unsafe_allow_html=True)

with colmns0[1]:
    # st.markdown('###')

    timestr = time.strftime('%Y-%m-%d %H:%M:%S')
    st.markdown(
        '<nobr><p style="text-align: center;font-family:sans serif; color:Black; font-size: 20px;">{}</p></nobr>'.format(
            timestr),
        unsafe_allow_html=True)

colmns = colmns0[1].columns([1, 1, 1, 1, 1], gap="small")
button7 = colmns[2].button(' 清除数据 ')

if button7:
    url = 'http://52.52.52.101:9011/api/WLW_MLFW/clearTargetInfo'
    try:
        response = requests.get(url, timeout=1)
        # 处理响应数据
        print(response.text)
        colmns[2].success('已发送清除数据指令！')
    except requests.exceptions.Timeout:
        # 请求超时处理
        print("请求超时")
    except requests.exceptions.RequestException as e:
        # 其他请求异常处理
        print("请求异常:", e)

    print("指令发送已完成...")



# 按钮字体
st.markdown("""<style>p, ol, ul, dl
{
margin: 0px 0px 1rem;
padding: 0px;
font-size: 1.0rem;
font-weight: 1000;
}
</style>""", unsafe_allow_html=True)

st.markdown("""<style> div.stButton > button:first-child {
background-color: white;
color: black;
height:3em; 
width:8em; 
border-radius:10px 10px 10px 10px;
border: 3px solid #008CBA;
}
</style>""", unsafe_allow_html=True)

st.markdown("""<style> 
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(1) > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(5) > div > div.css-c6gdys.edb2rvg0 > div > p {
font-size: 4px;
}
</style>""", unsafe_allow_html=True)
st.markdown("""<style> 
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(1) > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(4) > div > div.css-c6gdys.edb2rvg0 > div > p {
font-size: 4px;
}
</style>""", unsafe_allow_html=True)

st.markdown("""<style> 
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(1) > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(6) > div > div > div > div > div > div > p {
font-size: 4px;
}
</style>""", unsafe_allow_html=True)
st.markdown("""<style> div.stButton > button:first-child {
background-color: white;
color: black;
height:3em; 
width:8em; 
border-radius:10px 10px 10px 10px;
border: 3px solid #008CBA;
}
</style>""", unsafe_allow_html=True)

st.markdown("""<style> div.stButton > button:hover {
background-color: #008CBA;
color: white;
}
</style>""", unsafe_allow_html=True)
