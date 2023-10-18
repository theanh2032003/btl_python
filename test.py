import pygsheets

# Xác thực và kết nối với tài khoản Google Sheets
gc = pygsheets.authorize(service_file='telebot-python-ggsheet01-1affd58d7dc4.json')

# Tạo một bảng tính mới
spreadsheet = gc.create('Tên bảng')

spreadsheet.share("", role="reader", type="anyone")

# worksheet.share("", role="reader", type="anyone")
# Lấy URL của bảng tính mới tạo
sheet_url = spreadsheet.url

# In ra URL của bảng tính
print(sheet_url)