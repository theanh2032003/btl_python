import pygsheets
import numpy as np
from datetime import datetime
from datetime import datetime, timedelta
import requests
import json
from geopy.geocoders import Nominatim


# def caculater_sum(worksheet,range_str):
#     range_data = worksheet.get_values(range_str)
#     data_array = np.array(range_data,dtype=float)
    
#     Sum = np.sum(data_array,axis=0)
#     return Sum

# tìm các tuần trong tháng
def find_sunday_ranges(year, month):
    # Tạo ngày đầu tháng
    first_day = datetime(year, month, 1)

    # Tìm ngày Chủ nhật đầu tiên
    first_sunday = first_day + timedelta(days=(6 - first_day.weekday() + 1))

    # Tạo danh sách các khoảng ngày chứa ngày Chủ nhật
    sunday_ranges = []
    current_sunday = first_sunday

    while current_sunday.month == month:
        next_sunday = current_sunday + timedelta(days=6)
        sunday_ranges.append((current_sunday, next_sunday))
        current_sunday = next_sunday + timedelta(days=1)

    return sunday_ranges

# tính tổng theo cột trong sheet
def caculater_sum(sheet,column_number,start_row,end_row):
    # col_values = sheet.get_col(column_name,start=start_row,end=end_row)
    # gc=pygsheets.authorize(service_account_file=path_json)
    # workbook = gc.open_by_key(sheet_id)
    # sheet = workbook.worksheet_by_title(sheet_name)
    start_cell = (start_row, column_number)
    end_cell = (end_row, column_number)
    col_values = sheet.get_values(start=start_cell,end=end_cell, returnas='matrix', majdim='COLUMNS')
    return sum([float(value) for sublist in col_values for value in sublist  if value[0] != ''])
    # return col_values
    
# sheet_id ='1-Ouzw_BGRgt-8ZxQVA33FHO_V2sDcrDbFUSfPQm4rwU'
# print(caculater_sum('telebot-python-ggsheet01-1affd58d7dc4.json',sheet_id,'Bảng tổng hợp',4,7,11))

# tìm row trống đầu tiên
def find_last_row(worksheet,col):
   
    column_values = worksheet.get_col(col)
    empty_row_index = None
    for i, value in enumerate(column_values):
        # if not value:
        #     return i+row_begin 
        if value: 
        #  print(i,value)
         empty_row_index=i
    return (empty_row_index+2)


# xác định 1 ngày có trong 1 khoảng thời gian không
def compare_String_date(star_date_str,end_date_str,date_str):
    start_date = datetime.strptime(star_date_str,'%Y-%m-%d')
    end_date = datetime.strptime(end_date_str,'%Y-%m-%d')
    date = datetime.strptime(date_str,'%Y-%m-%d')
    if start_date <= date <= end_date:
        return True
    else: return False
    

# trả về thông tin thời tiết 7 ngày
def weather(text):
    
    geolocator = Nominatim(user_agent="my_application")

    # Lấy thông tin vị trí của địa điểm
    location = geolocator.geocode(text)
    base_url = "http://api.openweathermap.org/data/3.0/onecall?"

    # Tọa độ của vị trí bạn muốn lấy thông tin thời tiết
    lat = str(location.latitude)
    lon = str(location.longitude)

    # Khóa API của bạn
    # api_key = "fe8d8c65cf345889139d8e545f57819a"
    api_key = "baa9836372d89099b39df87393ae2fed"
    # Cập nhật URL với tọa độ và khóa API
    call_url = base_url + "lat=" + lat + "&lon=" + lon + "&exclude=current,minutely,hourly,alerts&appid=" + api_key
    
    response = requests.get(call_url)
    data = response.json()

    
    if data:
    # Lấy thông tin dự báo hàng ngày
        daily_forecasts = data["daily"]
        content=""
    # In thông tin dự báo cho mỗi ngày
        for day in daily_forecasts:
            date = datetime.fromtimestamp(day['dt'])
            formatted_date = date.strftime('%d/%m/%Y')
            temperature = day["temp"]["day"]-273.15
            humidity = day["humidity"]
            wind_speed = day["wind_speed"]
            pressure = day["pressure"]
            weather_description = day["weather"][0]["description"]
            content += """
            Ngày {date}:
            Nhiệt độ: {temperature} K
            Độ ẩm: {humidity}%
            Tốc độ gió: {wind_speed} m/s
            Áp suất: {pressure} hPa
            Mô tả thời tiết: {weather_description}""".format(date=formatted_date,temperature=round(temperature),humidity=humidity,wind_speed=wind_speed,
                                                             pressure=pressure,weather_description=weather_description)
        return content
    else:
        return("Nhập vào không hợp lệ")


