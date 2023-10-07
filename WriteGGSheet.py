import gspread
from oauth2client.service_account import ServiceAccountCredentials


def write(messageText):
    
    command = messageText.split()[0]
    if command == "\chi" :
    
        # Đường dẫn đến file JSON chứa thông tin xác thực
        credentials_file = 'path/to/credentials.json'

        # Phạm vi truy cập của Google Sheets API
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        # Xác thực và mở kết nối với Google Sheets
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(credentials)

        # Mở bảng tính theo tên hoặc URL
        spreadsheet = client.open('Tên bảng tính')

        # Chọn một trang trong bảng tính
        worksheet = spreadsheet.worksheet('Tên trang')

        # Viết dữ liệu vào ô
        worksheet.update('A1', 'Hello, World!')

        # Hoặc viết dữ liệu vào nhiều ô cùng một lúc
        data = [['Dữ liệu 1', 'Dữ liệu 2', 'Dữ liệu 3'],
                ['Dữ liệu 4', 'Dữ liệu 5', 'Dữ liệu 6']]
        worksheet.update('A2:C3', data)