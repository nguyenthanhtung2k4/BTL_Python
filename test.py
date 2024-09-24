import json
# from time import*
# import sys,os
# # tung='''
# # toi la nguen  thanh tung
# # toi la nguen  thanh tung
# # toi la nguen  thanh tung
# # toi la nguen  thanh tung
# # toi la nguen  thanh tung
# # toi la nguen  thanh tung
# # '''
# # for i in tung:
# #     sys.stdout.write(i)
# #     # sys.stdout.flush()
# #     sleep(0.0000250000000000)



# text='''
# ==================== All Menu ====================

# 0.Thoát chương trình
# 1.Thêm phòng mới
# 2.Sửa thông tin phòng
# 3.Xóa phòng
# 4.Xem danh sách phòng
# 5.Hiện  thị  các phòng trống
# 6.Sửa thông tin khách hàng
# 7.Xem danh sách khách hàng
# 8.Đặt phòng mới
# 9.Hủy đặt phòng
# 10.Nhận phòng
# 11.Trả phòng
# 12.Xem danh sách đặt phòng
# 13.Thêm nhân viên mới
# 14.Sửa thông tin nhân viên
# 15.Xóa nhân viên
# 16.Xem danh sách nhân viên
# 17.Hiển thị báo cáo doanh thu chi tiết.
# 19.Setting
# 20.About     

# '''

# for i in  text:
#     sys.stdout.write(i)
#     sys.stdout.flush()
#     sleep(0.000000025)

file="D:\CODE\DNU_PYTHON\BTL\BTL_Python\Setting.json"


with open(file, "w+") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        data = {}  # Handle empty file or invalid JSON

    new_data = {
        "Setting": {
        "Font_Color": "F1",
        "Font_ERROR": "F2",
        "Back_Color": "B2",
        "Back_ERROR": "B8",
        "Thanhtung":"thanh"
        },
        "Delay": {
            "Time_logo": 0.025,
            "Time_About": 0.025
        }
    }

    data.update(new_data)
    # f.seek(0)  #quay lai  dau  file
    # f.truncate()  # Xoa noi dung hien co
    json.dump(data, f, indent=4)