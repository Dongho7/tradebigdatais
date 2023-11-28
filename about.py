import streamlit as st

def app():
    st.subheader("위성 사진을 활용하여 **식생 및 수역지수** 시각화")


    st.markdown(
        """
        **Satellite Info** : COPERNICUS/Sentinel-2 \n
        **Cloud Ratio** : 구름 비율에 대한 정보입니다. 설정 기간이 짧을 수록 높은 Cloud Ratio를 선택하는 것이 좋습니다. \n
        **NDVI(정규식생지수)** : 식물의 생존과 생장 상태를 평가하기 위한 인공위성 이미지 처리 지수입니다. 
        높은 NDVI 값은 식물 생장 및 녹지를 나타내며, 낮은 값은 물이나 비생장 지역을 나타냅니다. \n
        **NDWI(정규수역지수)** : 물 체적 및 물의 존재 여부를 감지하는 데 사용되는 인공위성 이미지 처리 지수입니다. 
        높은 NDWI 값은 물을 나타내며, 낮은 값은 건조한 지역을 나타냅니다. \n
        *NDVI 및 NDWI가 높을 수록 진한 녹색 계열로 표시됩니다.*
        """
    )
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("  \n  \n**If you need a code, please contact me via email.**")
    st.markdown(
        "Created by: [Dongho Shin](https://blog.naver.com/tlsehdgh4162) / [tlsehdgh4162@naver.com](tlsehdgh4162@naver.com)"
    )