from telegram.ext import Updater, CommandHandler
import pygsheets
from process_ggsheet import update_month_sheet,update_week_sheet,update_daily_sheet,get_total_data,find_sunday_ranges,delete_row
from controller import weather
from telegram import ParseMode

sheet_id ='1-Ouzw_BGRgt-8ZxQVA33FHO_V2sDcrDbFUSfPQm4rwU'
path_json='telebot-python-ggsheet01-1affd58d7dc4.json'
sheet_name='Bảng tổng hợp'
gc=pygsheets.authorize(service_account_file=path_json)
workbook = gc.open_by_key(sheet_id)
sheet = workbook.worksheet_by_title(sheet_name)
workbook.share('dinhanh2032003@gmail.com', role='reader')
# print(get_total_data(sheet))
# Định nghĩa hàm xử lý lệnh /start
def start_command(update,context):
    update.message.reply_text('Xin chào, tôi là bot quản lí chi tiêu')
    
def Help(update,context):
    update.message.reply_text(""""Nhập các lệnh sau
                              /start để bắt đầu
                              /chi để thêm vào số tiền vừa tiêu theo cú pháp /chi tên sp,số tiền,loại chi tiêu
                              /tien để xem thống kê số tiền đã tiêu
                              /thoitiet để xem thời tiết, cú pháp /thoitiet tên tỉnh thành
                              /xoa để xóa hàng mới cập nhật
                              """)
    
def process_chi(update, context):
    global sheet
    text = update.message.text.replace("\chi","")
    data = [i.strip() for i in text.split(',')]
    update_daily_sheet(sheet,data)
    update_week_sheet(sheet)
    update_month_sheet(sheet)
    update.message.reply_text('Dữ liệu đã được thêm vào')
    
def get_data(update, context):
    global sheet
    message = get_total_data(sheet) + " Nếu bạn muốn xem thêm, vui lòng <a href='https://docs.google.com/spreadsheets/d/1-Ouzw_BGRgt-8ZxQVA33FHO_V2sDcrDbFUSfPQm4rwU/edit?usp=sharing'>ấn vào đây</a>"
    update.message.reply_text(message, parse_mode=ParseMode.HTML)
# Định nghĩa hàm xử lý lệnh /hello
def hello(update, context):
    update.message.reply_text('Xin chào! Bạn đã gửi lệnh /hello.')

def thoitiet(update,context):
        city = update.message.text.replace("/thoitiet","").strip()
        update.message.reply_text(weather(city))
    
def delete(update,context):
    global sheet
    delete_row(sheet)

def main():
    # Khởi tạo Updater với mã token của bot Telegram
    updater = Updater('6081198225:AAFL7zPIho4vOPGAh-kP0uEraCnK4lMJW_4', use_context=True)

    # Lấy Dispatcher từ Updater
    dispatcher = updater.dispatcher

    # Đăng ký trình xử lý lệnh /start

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', Help))
    dispatcher.add_handler(CommandHandler('chi', process_chi))
    dispatcher.add_handler(CommandHandler('tien', get_data))
    dispatcher.add_handler(CommandHandler('thoitiet', thoitiet))
    dispatcher.add_handler(CommandHandler('xoa',delete))
    
    
    
    

    # Đăng ký trình xử lý lệnh /hello 
    dispatcher.add_handler(CommandHandler('hello', hello))

    # Bắt đầu bot
    updater.start_polling()

    # Dừng bot khi nhận được tín hiệu từ bàn phím (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()