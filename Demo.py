import csv 
import os,sys
import tkinter as tk
# from PIL import* #  image , imageTk 
from PIL import Image , ImageTk 


#  CAI DAT THU  VIEN TRONG PYTHON  csv, pip install imagetk
# TRY EXPECT


menu='''
1.Thêm phòng mới: Thêm thông tin một phòng mới vào hệ thống.
2.Sửa thông tin phòng: Cập nhật thông tin của một phòng đã tồn tại.
3.Xóa phòng: Xóa thông tin một phòng khỏi hệ thống.
4.Xem danh sách phòng: Hiển thị danh sách tất cả các phòng và tình trạng của chúng.
5.Thêm khách hàng mới: Thêm thông tin một khách hàng mới vào hệ thống.
6.Sửa thông tin khách hàng: Cập nhật thông tin của một khách hàng đã tồn tại.
7.Xem danh sách khách hàng: Hiển thị danh sách tất cả các khách hàng.
8.Đặt phòng mới: Tạo một đơn đặt phòng mới.
9.Hủy đặt phòng : Hủy một đơn đặt phòng đã tồn tại.
10.Nhận phòng : Xác nhận khách đã nhận phòng.
11.Trả phòng: Xác nhận khách đã trả phòng, tính toán số tiền cần thanh toán.
12.Xem danh sách đặt phòng: Hiển thị danh sách tất cả các đơn đặt phòng.
13.Thêm nhân viên mới: Thêm thông tin một nhân viên mới vào hệ thống.
14.Sửa thông tin nhân viên: Cập nhật thông tin của một nhân viên đã tồn tại.
15.Xóa nhân viên: Xóa thông tin một nhân viên khỏi hệ thống.
16.Xem danh sách nhân viên: Hiển thị danh sách tất cả các nhân viên.
17.Tính toán doanh thu: Tính toán tổng doanh thu theo ngày, tháng, năm.
18.Xem báo cáo doanh thuHiển thị báo cáo doanh thu chi tiết.
'''

def check(file):
     if os.path.exists(file):
          return file
# menu1 them phong moi
def add():
     
     loai='To'
     Gia='200'
     status='No'
     ob={
          'Số phòng':122,
          'Loại':loai,
          'Giá':Gia,
          'Trạng thái':status
     }
     arr=[133,'Don','400','yes']
     return ob
def menu1(file,add):
     with open(file,'a+',newline='',encoding='utf-8')as filecsv:
          format=['Số phòng','Loại','Giá','Trạng thái']
          writer=csv.DictWriter(filecsv,fieldnames=format)
          writer.writerow(add)
          
# menu4 xem tat ca phong
def menu4(file):
     with open(file,'r', encoding='utf-8')as r:
          render=csv.DictReader(r)
          next(render)
          print(f'Số phòng\t Loại\t  Giá\t Trạng thái')
          for row in render:
               so=row['Số phòng']
               loai=row['Loại']
               gia=row['Giá']
               status=row['Trạng thái']
               print(f'  {so}\t\t {loai}\t  {gia}\t {status}')

if __name__ == '__main__':
     file_phong='Phong.csv'

#MENU4 xem tat ca
     if check(file_phong):
          menu4(file_phong)
     else:
          print('File khong ton tai!')
# MENU1 them phong
     # add=add()
     # print(add)
     # menu1(file_phong,add)
     # menu4(file_phong)
