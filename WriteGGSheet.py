import pygsheets

def init_sheet(sheet_id,path_json,sheet_name):
    gc=pygsheets.authorize(service_account_file=path_json)
    workbook = gc.open_by_key(sheet_id)
    sheet = workbook.worksheet_by_title(sheet_name)
    sheet.resize(rows=500,cols=11)
    sheet.merge_cells(start='A1', end='E1')
    sheet.merge_cells(start='A5', end='E5')
    sheet.merge_cells(start='A13', end='E13')
    sheet.merge_cells(start='G1', end='J1')
    cell = sheet.cell('A1')
    cell.value = 'Bảng tổng hợp'.title()
    cell.set_text_format("fontSize", 14)
    cell.set_text_format("bold", True)
    cell.update()
    cell = sheet.cell('A5')    
    cell.value = 'Bảng tổng hợp theo tuần'.title()
    cell.set_text_format("fontSize", 14)
    cell.set_text_format("bold", True)
    cell.update()
    cell = sheet.cell('A13')
    cell.value = 'Thu chi theo ngày'.title()
    cell.set_text_format("fontSize", 14)
    cell.set_text_format("bold", True)
    cell.update()
    cell = sheet.cell('G1')
    cell.value = 'Bảng tổng hợp các tháng'.title()
    cell.set_text_format("fontSize", 14)
    cell.set_text_format("bold", True)
    cell.update()
    
    monthly_data = [['Tháng','Tổng thu','Tổng chi','Tiết kiệm']]
    sheet.update_values('A2D2',monthly_data)
    
    monthly_data = [['Tháng','Tổng thu','Tổng chi','Tiết kiệm']]
    sheet.update_values('G2J2',monthly_data)
    
    weekly_data = [['Tuần','Bắt Đầu','Kết Thúc','Tổng Thu','Tổng Chi']]
    sheet.update_values('A6E6',weekly_data)
    
    dayly_data = [['Ngày','Mô Tả','Thu','Chi','Loại']]
    sheet.update_values('A14E14',dayly_data)
    return workbook,sheet
    
# init_sheet('14MNmqBeaf4pp8Q09pxoIFfuaWuBqVDu11NH1HKsE--U','telebot-python-ggsheet01-1affd58d7dc4.json','Trang tính1')