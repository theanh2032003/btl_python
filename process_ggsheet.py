import pygsheets
from datetime import datetime, timedelta
import calendar
from controller import caculater_sum,find_last_row,compare_String_date,find_sunday_ranges

# def update_dayly_sheet(path_json,sheet_id,sheet_name,cell_range,value):
#     gc=pygsheets.authorize(service_account_file=path_json)
#     workbook = gc.open_by_key(sheet_id)
#     sheet = workbook.worksheet_by_title(sheet_name)
        
#     sheet.update_values(cell_range,value)
    
sheet_id ='1-Ouzw_BGRgt-8ZxQVA33FHO_V2sDcrDbFUSfPQm4rwU'
# update_dayly_sheet('telebot-python-ggsheet01-1affd58d7dc4.json',sheet_id,'Bảng tổng hợp','B15:D15',[['42500','','nha']])


# def update_month_sheet(path_json,sheet_id,sheet_name):
#     gc=pygsheets.authorize(service_account_file=path_json)
#     workbook = gc.open_by_key(sheet_id)
#     sheet = workbook.worksheet_by_title(sheet_name)
#     weeks = find_sunday_ranges(datetime.now().year,datetime.now().month)
#     lenght_of_weeksheet = len(weeks)
#     sheet.update_value('B3',caculater_sum(sheet,4,7,6+lenght_of_weeksheet))
#     sheet.update_value('C3',caculater_sum(sheet,5,7,6+lenght_of_weeksheet))
#     sheet.update_value('D3',float(sheet.get_value('B3'))-float(sheet.get_value('C3')))
#     # sheet.update_value('B3',caculater_sum(sheet,4,7,6+lenght_of_weeksheet))
    
# update_month_sheet('telebot-python-ggsheet01-1affd58d7dc4.json',sheet_id,'Bảng tổng hợp')

# def update_week_sheet(path_json,sheet_id,sheet_name):
#     gc=pygsheets.authorize(service_account_file=path_json)
#     workbook = gc.open_by_key(sheet_id)
#     sheet = workbook.worksheet_by_title(sheet_name)
#     weeks = find_sunday_ranges(datetime.now().year,datetime.now().month)
#     lenght_of_weeksheet = len(weeks)
#     end_row = find_last_row(sheet,1,15)
#     for i in range(len(weeks)):
#         Sum1=Sum2=0
#         for j in range(15,end_row):
#             if compare_String_date(weeks[i][0],weeks[i][1],sheet.get_value(f'A{j}'))  :
#                 Sum1+=int(sheet.get_value(f'C{j}'))
#                 Sum2+=int(sheet.get_value(f'D{j}'))
#         sheet.update_value(f'D{7+i}',Sum1)
#         sheet.update_value(f'E{7+i}',Sum2)
        
# def update_daily_sheet(path_json,sheet_id,sheet_name,values):
#     gc=pygsheets.authorize(service_account_file=path_json)
#     workbook = gc.open_by_key(sheet_id)
#     sheet = workbook.worksheet_by_title(sheet_name)
#     first_empty_row = find_sunday_ranges(sheet,1,15)
#     sheet.update_value(f'A{first_empty_row}',datetime.now().strftime('%Y-%m-%d'))
#     cells = [f'B{first_empty_row},'f'D{first_empty_row}',f'E{first_empty_row}']
#     for value, cell  in zip(values,cells):
#         sheet.update_value(cell,value)
        
# def get_total_data(path_json,sheet_id,sheet_name):
#     gc=pygsheets.authorize(service_account_file=path_json)
#     workbook = gc.open_by_key(sheet_id)
#     sheet = workbook.worksheet_by_title(sheet_name)
#     date = datetime.now().strftime('%Y-%m-%d')
#     weeks = find_sunday_ranges(datetime.now().year,datetime.now().month)
#     last_row=7
#     for i in range(len(weeks)):
#         if compare_String_date(weeks[i][0],weeks[i][1],date):
#             last_row=i
#             break   
#     weekly_money = sheet.get_value(f'E{last_row}')
#     monthly_money = sheet.get_value('B3')
#     return f'Tháng này bạn đã chi {monthly_money}, tuần này đã tiêu hêt {weekly_money}'


import pygsheets
from datetime import datetime, timedelta
import calendar
# from TimeGoogleSheet import find_sunday_ranges
from controller import caculater_sum,find_last_row,compare_String_date,find_sunday_ranges

# def update_dayly_sheet(path_json,sheet_id,sheet_name,cell_range,value):
#     gc=pygsheets.authorize(service_account_file=path_json)
#     workbook = gc.open_by_key(sheet_id)
#     sheet = workbook.worksheet_by_title(sheet_name)
        
#     sheet.update_values(cell_range,value)
    
sheet_id ='1-Ouzw_BGRgt-8ZxQVA33FHO_V2sDcrDbFUSfPQm4rwU'
# update_dayly_sheet('telebot-python-ggsheet01-1affd58d7dc4.json',sheet_id,'Bảng tổng hợp','B15:D15',[['42500','','nha']])


# def update_month_sheet(sheet):

#     weeks = find_sunday_ranges(datetime.now().year, datetime.now().month)
#     lenght_of_weeksheet = len(weeks)
#     sheet.update_value('B3', caculater_sum(sheet, 4, 7, 6 + lenght_of_weeksheet))
#     sheet.update_value('C3', caculater_sum(sheet, 5, 7, 6 + lenght_of_weeksheet))
#     sheet.update_value('D3',float(sheet.get_value('B3')) - float(sheet.get_value('C3')))
#     sheet.update_value('A3',datetime.now().strftime('%Y-%m'))    
#     sheet.sync()
    # sheet.update_value('B3',caculater_sum(sheet,4,7,6+lenght_of_weeksheet))
    
# update_month_sheet('telebot-python-ggsheet01-1affd58d7dc4.json',sheet_id,'Bảng tổng hợp')

def update_month_sheet(sheet):
  # gc=pygsheets.authorize(service_account_file=path_json)
  # workbook = gc.open_by_key(sheet_id)
  # sheet = workbook.worksheet_by_title(sheet_name)
  weeks = find_sunday_ranges(datetime.now().year, datetime.now().month)
  lenght_of_weeksheet = len(weeks)
#   cell = sheet.cell('B3')  
#   cell.value = caculater_sum(sheet, 4, 7, 6 + lenght_of_weeksheet)
#   cell.update()
#   cell = sheet.cell('C3')  
#   cell.value = caculater_sum(sheet, 5, 7, 6 + lenght_of_weeksheet)
#   cell.update()
  value_B3=caculater_sum(sheet, 4, 7, 6 + lenght_of_weeksheet)
  value_C3=caculater_sum(sheet, 5, 7, 6 + lenght_of_weeksheet)
  sheet.update_values('A3D3', [[datetime.now().strftime('%Y-%m'),value_B3,value_C3,value_B3-value_C3]])
  sheet.sync()

def update_week_sheet_thu(sheet,data):
    # gc=pygsheets.authorize(service_account_file=path_json)
    # workbook = gc.open_by_key(sheet_id)
    # sheet = workbook.worksheet_by_title(sheet_name)
    weeks = find_sunday_ranges(datetime.now().year,datetime.now().month)
    lenght_of_weeksheet = len(weeks)
    end_row = find_last_row(sheet,1)
    for i in range(len(weeks)):
        sheet.update_values(f'A{i+7}C{i+7}',[[f'{i+1}',weeks[i][0].strftime('%Y-%m-%d'),weeks[i][1].strftime('%Y-%m-%d')]])
    for i in range(len(weeks)):
            if compare_String_date(weeks[i][0].strftime('%Y-%m-%d'),weeks[i][1].strftime('%Y-%m-%d'),datetime.now().strftime('%Y-%m-%d'))  :
               if sheet.get_value(f'D{7+i}') == '': sheet.update_value(f'D{7+i}',0)
               if sheet.get_value(f'E{7+i}') == '': sheet.update_value(f'E{7+i}',0)
               sheet.sync()
               sheet.update_value(f'D{7+i}',float(sheet.get_value(f'D{7+i}'))+data[0])
               sheet.update_value(f'E{7+i}',float(sheet.get_value(f'E{7+i}'))+data[1])    
    sheet.sync()
    
        
def update_daily_sheet_chi(sheet,values):
    # gc=pygsheets.authorize(service_account_file=path_json)
    # workbook = gc.open_by_key(sheet_id)
    # sheet = workbook.worksheet_by_title(sheet_name)
    first_empty_row = find_last_row(sheet,1)
    sheet.update_value(f'A{first_empty_row}',datetime.now().strftime('%Y-%m-%d'))
    sheet.update_value(f'B{first_empty_row}',values[0])
    sheet.update_value(f'D{first_empty_row}',values[1])
    sheet.update_value(f'E{first_empty_row}',values[2])
    sheet.sync()

def update_daily_sheet_thu(sheet,values):
    # gc=pygsheets.authorize(service_account_file=path_json)
    # workbook = gc.open_by_key(sheet_id)
    # sheet = workbook.worksheet_by_title(sheet_name)
    first_empty_row = find_last_row(sheet,1)
    sheet.update_value(f'A{first_empty_row}',datetime.now().strftime('%Y-%m-%d'))
    sheet.update_value(f'B{first_empty_row}',values[0])
    sheet.update_value(f'C{first_empty_row}',values[1])
    sheet.update_value(f'E{first_empty_row}',values[2])
    sheet.sync()
        
def get_total_data(sheet):
    # gc=pygsheets.authorize(service_account_file=path_json)
    # workbook = gc.open_by_key(sheet_id)
    # sheet = workbook.worksheet_by_title(sheet_name)
    date = datetime.now().strftime('%Y-%m-%d')
    weeks = find_sunday_ranges(datetime.now().year,datetime.now().month)
    last_row=0
    for i in range(len(weeks)):
        if compare_String_date(weeks[i][0].strftime('%Y-%m-%d'),weeks[i][1].strftime('%Y-%m-%d'),date):
            last_row=i+7
            break   
    weekly_money = sheet.get_value(f'E{last_row}')
    monthly_money = sheet.get_value('C3')
    # sheet.sync()
    return f'Tháng này bạn đã chi {monthly_money}, tuần này đã tiêu hêt {weekly_money}'

def delete_row(sheet):
  row = find_last_row(sheet, 1) - 1
  data = [['', '', '', '', '']]
  sheet.update_values(f'A{row}E{row}', data)
  sheet.sync()
    
def update_repo_sheet(sheet):
    data = sheet.get_values('A3D3')
    sheet.update_values('G3J3',data)
    sheet.sync()   
 
def reset_daily_sheet_month(sheet):
    today = datetime.now()
    first_day_of_next_month = (today.replace(day=1)+timedelta(days=32-today.day)).replace(day=1)
    if today.date() == first_day_of_next_month.date():
        update_repo_sheet(sheet)
        end_row = find_last_row(sheet,1)
        range_label = f'A{15}:E{end_row}'
        sheet.clear_range(range_label)
        sheet.clear_range(f'A{7}:E{12}')
        sheet.clear_range(f'A{3}:D{3}')    
        sheet.sync() 



        