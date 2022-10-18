import requests
import datetime

def get_hourly_weather_data(url):
    response = requests.get(url)  # 对获取天气信息接口进行get请求,并获取响应信息
    assert response.status_code == 200
    res = (response.json())
    HourlyWeatherForecast = res['HourlyWeatherForecast']
    today = datetime.date.today().strftime('%Y%m%d')
    after_tomorrow_day = str(int(today) + 2)
    n = len(HourlyWeatherForecast)
    ForecastRelativeHumidityList = []  # 后天的24小时相对湿度列表
    for i in range(n):
        if after_tomorrow_day in HourlyWeatherForecast[i]['ForecastHour']:
            ForecastRelativeHumidityList.append(HourlyWeatherForecast[i]['ForecastRelativeHumidity'])
    minHumidityList, maxHumidityList = min(ForecastRelativeHumidityList), max(
        ForecastRelativeHumidityList)  # 从列表中抽取最大和最小的湿度数据
    print("the relative humidity for the day after tomorrow is {0}% - {1}%".format(minHumidityList, maxHumidityList))


if __name__ == '__main__':
    url = "https://pda.weather.gov.hk/locspc/data/ocf_data/HKO.v2.xml"
    get_hourly_weather_data(url)