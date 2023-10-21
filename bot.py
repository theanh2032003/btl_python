from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
import pygsheets
from process_ggsheet import update_month_sheet,update_week_sheet,update_daily_sheet_chi,update_daily_sheet_thu,get_total_data,find_sunday_ranges,delete_row,reset_daily_sheet_month
import datetime
from controller import weather,get_news,find_last_row
from telegram import ParseMode
from WriteGGSheet import init_sheet

# sheet_id ='1-Ouzw_BGRgt-8ZxQVA33FHO_V2sDcrDbFUSfPQm4rwU'
path_json='telebot-python-ggsheet01-1affd58d7dc4.json'
# sheet_name='Bảng tổng hợp'
# sheet_id ='14MNmqBeaf4pp8Q09pxoIFfuaWuBqVDu11NH1HKsE--U'
# path_json='telebot-python-ggsheet01-1affd58d7dc4.json'
# sheet_name='Trang tính1'
# gc=pygsheets.authorize(service_account_file=path_json)
# workbook = gc.open_by_key(sheet_id)
# sheet = workbook.worksheet_by_title(sheet_name)
workbook,sheet = init_sheet(path_json)
workbook.share("", role="reader", type="anyone")
# print(get_total_data(sheet))
# Định nghĩa hàm xử lý lệnh /start
def start_command(update,context):
    global sheet
    reset_daily_sheet_month(sheet)
    update.message.reply_text('Xin chào, tôi là bot quản lí chi tiêu')
    
def Help(update,context):
    global sheet
    reset_daily_sheet_month(sheet)
    update.message.reply_text(""""Nhập các lệnh sau
                             /start để bắt đầu
                             /chi để thêm vào số tiền vừa tiêu theo cú pháp /chi tên sp,số tiền,loại chi tiêu
                             /thu để thêm vào số tiền vừa tiêu theo cú pháp /thu tên sp,số tiền,loại chi tiêu
                             /tien để xem thống kê số tiền đã tiêu                              
                             /xoa để xóa hàng mới cập nhật
                             /thoitiet để xem thời tiết, cú pháp /thoitiet tên tỉnh thành
                             /news để xem tin tức
                              """)
    
    
def process_chi(update, context):
  global sheet
  reset_daily_sheet_month(sheet)
  text = update.message.text.replace("/chi", "")
  data = [i.strip() for i in text.split(',')]
  try:
    if len(data) != 3:
      raise ValueError('Số lượng dữ liệu không đúng')
    i = float(data[1])
    update_daily_sheet_chi(sheet, data)
    update_week_sheet(sheet, [0, i])
    update_month_sheet(sheet)
    update.message.reply_text('Dữ liệu đã được thêm vào')
  except ValueError:
    update.message.reply_text(
        "Vui lòng nhập đúng định dạng /chi tên sp,số tiền,loại chi tiêu")
        
    
def process_thu(update, context):
  global sheet
  reset_daily_sheet_month(sheet)
  text = update.message.text.replace("/thu", "")
  data = [i.strip() for i in text.split(',')]
  try:
    if len(data) != 3:
      raise ValueError('Số lượng dữ liệu không đúng')
    i = float(data[1])
    update_daily_sheet_thu(sheet, data)
    update_week_sheet(sheet, [i, 0])
    update_month_sheet(sheet)
    update.message.reply_text('Dữ liệu đã được thêm vào')
  except ValueError:
    update.message.reply_text(
        "Vui lòng nhập đúng định dạng cú pháp /thu tên sp,số tiền,loại chi tiêu"
    )
        
    
def get_data(update, context):
    global sheet
    reset_daily_sheet_month(sheet)
    message = get_total_data(sheet) + " Nếu bạn muốn xem thêm, vui lòng <a href='https://docs.google.com/spreadsheets/d/1-Ouzw_BGRgt-8ZxQVA33FHO_V2sDcrDbFUSfPQm4rwU/edit?usp=sharing'>ấn vào đây</a>"
    update.message.reply_text(message, parse_mode=ParseMode.HTML)
# Định nghĩa hàm xử lý lệnh /hello
def hello(update, context):
    update.message.reply_text('Xin chào! Bạn đã gửi lệnh /hello.')

def thoitiet(update,context):
        city = update.message.text.replace("/thoitiet","").strip()
        update.message.reply_markdown_v2(weather(city))
    
def delete(update,context):
    global sheet
    row = find_last_row(sheet, 1) - 1
    data=[-float(sheet.get_value(f'C{row}')),-float(sheet.get_value(f'C{row}'))]
    reset_daily_sheet_month(sheet)
    delete_row(sheet)
    update_week_sheet(sheet,data)
    update_month_sheet(sheet)
    update.message.reply_text('Dữ liệu đã được xóa')

# def reset(update,context):
#     global sheet
#     reset_daily_sheet_month(sheet)
#     context.bot.send_message(chat_id=context.job.context, text='Sang tháng mới rồi, hãy tiết kiệm nhé:))')
    
def handle_default_message(update,context):
    message = update.message.text
    update.message.reply_text('Tin nhắn ko hợp lệ')
    
def get_new(update,context):
    message = get_news()
    update.message.reply_markdown_v2(message)
    
    

def main():
    # Khởi tạo Updater với mã token của bot Telegram
    updater = Updater('6562823385:AAHVs5NlnGpyiKi6Ybi7VnLtIS1hCArljck', use_context=True)

    # Lấy Dispatcher từ Updater
    dispatcher = updater.dispatcher
 
    # Đăng ký trình xử lý lệnh /start

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', Help))
    dispatcher.add_handler(CommandHandler('chi', process_chi))
    dispatcher.add_handler(CommandHandler('thu', process_thu))
    dispatcher.add_handler(CommandHandler('tien', get_data))
    dispatcher.add_handler(CommandHandler('thoitiet', thoitiet))
    dispatcher.add_handler(CommandHandler('xoa',delete))
    dispatcher.add_handler(CommandHandler('news',get_new))
    default_handler = MessageHandler(Filters.text,handle_default_message)
    dispatcher.add_handler(default_handler)
    
    
    

    # Đăng ký trình xử lý lệnh /hello 
    dispatcher.add_handler(CommandHandler('hello', hello))
    # job_queue = updater.job_queue
    # # first_day_of_month = datetime.time(hour=0,minute=0,second=0)
    # # job = Job(reset,first_day_of_month)
    # job_queue.run_daily(reset,time=datetime.time(hour=0, minute=0, second=0))
    # Bắt đầu bot
    updater.start_polling()

    # Dừng bot khi nhận được tín hiệu từ bàn phím (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()