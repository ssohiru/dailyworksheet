import streamlit as st

st.header("특수학급 학생들을 위한 매일 학습지 생성기")

st.text("매일 학습지를 만드시나요?")
st.text("이 프로그램이 있으면 학생들을 위한 맞춤형 학습지가 생성됩니다!!")

# 이미지 URL
image_url_1 = "https://drive.google.com/uc?id=1w8CI_1ZwiwKvCrgR08vjglJ710JOFyIZ"
image_url_2 = "https://drive.google.com/uc?id=1hFHElRXYfFWzculdbrSgBfO-IwVWWpz4"
image_url_3 = "https://drive.google.com/uc?id=1aJ_4B9CtWhp5XKAK4j42H6sDN_JN_1yS"
image_url_4 = "https://drive.google.com/uc?id=1KbKRBQaNQxR-f0tpCuYuf9LaYaFQIgwo"

# 이미지를 2x2로 배치
col1, col2 = st.columns(2)

with col1:
    st.image(image_url_1, use_column_width=True)

with col2:
    st.image(image_url_2, use_column_width=True)

col3, col4 = st.columns(2)

with col3:
    st.image(image_url_3, use_column_width=True)

with col4:
    st.image(image_url_4, use_column_width=True)

    





