import streamlit as st
import geemap.foliumap as geemap
from datetime import datetime
import json
from streamlit_folium import folium_static
import ee

service_account_info = st.secrets["GEE_SERVICE_ACCOUNT"]

# Google Earth Engine 인증 정보 생성 및 초기화
credentials = ee.ServiceAccountCredentials(
    service_account_info["client_email"],
    key_data=service_account_info["private_key"]
)
ee.Initialize(credentials)
#
# import ee
# service_account = 'trade-bigdata@tradebigdata.iam.gserviceaccount.com'
# credentials = ee.ServiceAccountCredentials(service_account, '.streamlit/tradebigdata-d03dbc7e3c77.json')
# ee.Initialize(credentials)

# Google Earth Engine 초기화


# Streamlit 앱 구성
def app():
    main()

def main():
    st.title("Visualization of Satellite images(Demo):satellite_antenna:")
    st.markdown("*데모 버전*입니다.. :sob: 디버깅 별로 못 했어요,, \n 그래서 오류가 발생할 수 있어요.  \n꼭 **지정된 형식**에 맞추어 입력해주세요.")

    start_date_input = st.text_input("시작 날짜 입력 (YYYY-MM-DD 형식):")
    end_date_input = st.text_input("종료 날짜 입력 (YYYY-MM-DD 형식):")

    date_valid = True
    try:
        datetime.strptime(start_date_input, '%Y-%m-%d')
        datetime.strptime(end_date_input, '%Y-%m-%d')
    except ValueError:
        date_valid = False
        if start_date_input and end_date_input:
            st.error("날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해주세요.")

    country = st.text_input("나라 입력(ex: Republic of Korea, Panama):")

    index_choice = st.radio("지수 선택:", ('NDVI', 'NDWI'))
    cloud_ratio = st.radio(":cloud: Cloud Ratio(너무 낮으면 사진이 일부 짤려요, 40정도로 해도 잘 보여요!) :", ("40", "30", "20"))

    if st.button("시각화") and date_valid:

        aoi = (ee.FeatureCollection("FAO/GAUL/2015/level0")
                .filter(ee.Filter.eq('ADM0_NAME', country)).geometry())

        def getVegetationIndex(image, index_type):
            if index_type == 'NDVI':
                index = image.normalizedDifference(['B8', 'B4']).rename("NDVI")
            elif index_type == 'NDWI':
                index = image.normalizedDifference(['B3', 'B8']).rename("NDWI")

            return image.addBands(index)

        def addDate(image):
            img_date = ee.Date(image.date())
            img_date = ee.Number.parse(img_date.format('YYYYMMdd'))
            return image.addBands(ee.Image(img_date).rename('date').toInt())

        Sentinel_data = ee.ImageCollection('COPERNICUS/S2') \
            .filterDate(start_date_input, end_date_input).filterBounds(aoi) \
            .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', int(cloud_ratio))) \
            .map(lambda image: getVegetationIndex(image, index_choice)).map(addDate).median()

        color = ['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718',
                 '74A901', '66A000', '529400', '3E8601', '207401', '056201',
                 '004C00', '023B01', '012E01', '011D01', '011301']

        pallete = {"min": 0, "max": 1, 'palette': color}

        map1 = geemap.Map()
        map1.centerObject(aoi, 8)
        map1.addLayer(Sentinel_data.clip(aoi).select(index_choice), pallete, index_choice)

        map1.addLayerControl()
        folium_static(map1)


if __name__ == "__main__":
    main()
