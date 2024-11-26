from Thanhtung import*
from LeVuong import*
from BuiTuan import*
from Setting import*
from time import*
import  csv
import os, sys
import re,json
#  try expcet cai thu vien pystyle 
try:
     from pystyle import System # type: ignore
except :
     os.system('pip install pystyle')
def TextMenu(choce,text_small):

     if choce==1:
          text=f'''
{color_bar}==================== {colorB_logo+colorF_logo}All Menu{RESETs+color_bar} ====================

{colorF_logo+colorB_logo}0. {RESETs+colorF}Thoát chương trình
{colorF_logo+colorB_logo}1. {RESETs+colorF}Thêm phòng mới
{colorF_logo+colorB_logo}2. {RESETs+colorF}Sửa thông tin phòng
{colorF_logo+colorB_logo}3. {RESETs+colorF}Xóa phòng
{colorF_logo+colorB_logo}4. {RESETs+colorF}Xem danh sách phòng
{colorF_logo+colorB_logo}5. {RESETs+colorF}Hiện  thị  các phòng trống
{colorF_logo+colorB_logo}6. {RESETs+colorF}Sửa thông tin khách hàng
{colorF_logo+colorB_logo}7. {RESETs+colorF}Xem danh sách khách hàng
{colorF_logo+colorB_logo}8. {RESETs+colorF}Đặt phòng mới
{colorF_logo+colorB_logo}9. {RESETs+colorF}Hủy đặt phòng
{colorF_logo+colorB_logo}10. {RESETs+colorF}Nhận phòng
{colorF_logo+colorB_logo}11. {RESETs+colorF}Trả phòng
{colorF_logo+colorB_logo}12. {RESETs+colorF}Xem danh sách đặt phòng
{colorF_logo+colorB_logo}13. {RESETs+colorF}Thêm nhân viên mới
{colorF_logo+colorB_logo}14. {RESETs+colorF}Sửa thông tin nhân viên
{colorF_logo+colorB_logo}15. {RESETs+colorF}Xóa nhân viên
{colorF_logo+colorB_logo}16. {RESETs+colorF}Xem danh sách nhân viên
{colorF_logo+colorB_logo}17. {RESETs+colorF}Hiển thị báo cáo doanh thu chi tiết.{RESETs+colorF}
{colorF_logo+colorB_logo}18. {RESETs+colorF}Setting
{colorF_logo+colorB_logo}19. {RESETs+colorF}About

'''
     elif choce==2:
          text=f'{colorF_logo}==================== {colorF_logo+colorB_logo}{text_small} {RESETs+colorF_logo}===================={RESETs}\n'
     elif choce==3:
          text=20
     else:
          pass
     return text

def error():
     System.Clear()
     print(f'{erF}Lựa chọn {erB+erF}không hợp lệ !{RESETs}')
    
'''Đường đân file các đường dẫn liên quan đến color và fomat được nằm trong setting.py(def main) 
AutoFile sẽ kiểm tra để viết lại file
AutoColor sẽ được kiểm tra nếu file không tồn tại
'''
if  __name__=='__main__':
#  File Main  khi chạy nó sẽ chạy file Setting.py (  function main() -->  đầu tiên để check thông tin trước.)
     #////Claer trong termial
     System.Clear()
     options={
          1: lambda: menu1(file_phong),
          2: lambda: menu2(file_phong),
          3: lambda: menu3(file_phong), # cần nâng cấp thêm trước khi xóa cần xem phòng đó có ai thuêy chưa, nếu chưa thì xóa , không thì không xóa được.
          4: lambda: menu4(file_phong),
          5: lambda: menu5(file_phong),
          6: lambda: menu6(file_Khach,file_phong),
          7: lambda: menu7(file_Khach),
          8: lambda: menu8(file_phong,file_Khach),
          9: lambda: menu9(file_Khach,file_phong),
          10: lambda: menu10(file_Khach),
          11: lambda: menu11(file_phong,file_Khach),
          12: lambda: menu12(file_Khach),
          13: lambda: menu13(file_NhanVien,fomat_nhanVien),
          14: lambda: menu14(file_NhanVien),
          15: lambda: menu15(file_NhanVien,fomat_nhanVien),
          16: lambda: menu16(file_NhanVien),# cần nâng cấp thêm chức năng xem tiền lương nhân viên trong file ..
          17: lambda: menu17(file_phong,file_Khach), # cần nâng cấp vấn đề lưu lại lịch sử tính tổng số tiền một cách chính xác và hiểu quả hơn.
          18: lambda: setting(file_setting),
          19: lambda: About(),
     } 
# /////////////////////////// INTRO LOGO //////////////
     main()
     for i in  TextMenu(1,''):
          sys.stdout.write(i)
          sleep(time_logo)
     dem=0;
# ******************************** Open  Script ********************************
     while True:
          color_bar,colorF_logo,colorB_logo,colorF,colorB,erF,erB,RESETs,time_logo,time_about=Update_Color(file_setting)
          dem+=1
          if dem>1:
               print(TextMenu(1,f'{colorB}All Menu{RESETs}'))
          Nhap=INput(int,f'{color_bar}Chọn Chức Năng\n==> {RESETs}',2)
          if Nhap == 0:
               System.Clear()
               print(f'{erF}Tạm biệt !{RESETs}') 
               break;
          options.get(Nhap,lambda: error())()