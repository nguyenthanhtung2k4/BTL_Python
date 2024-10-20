import csv
import os
from datetime import datetime #Lấy date
#from pystyle import System
# from Main import Update_Color # lay mau color
# colorF_logo,colorB_logo,color_bar, colorF,colorB,erF,erB=Update_Color

#1.Thêm phòng mới: Thêm thông tin một phòng mới vào hệ thống.
#2.Sửa thông tin phòng: Cập nhật thông tin của một phòng đã tồn tại.
#3.Xóa phòng: Xóa thông tin một phòng khỏi hệ thống.
#4.Xem danh sách phòng: Hiển thị danh sách tất cả các phòng và tình trạng của chúng.
#5.Hiện  thị  các phòng trống; 
#6.Sửa thông tin khách hàng: Cập nhật thông tin của một khách hàng đã tồn tại.
#7.Xem danh sách khách hàng: Hiển thị danh sách tất cả các khách hàng.
#8.Đặt phòng mới: Tạo một đơn đặt phòng mới.
#9.Hủy đặt phòng : Hủy một đơn đặt phòng đã tồn tại.
#10.Nhận phòng : Xác nhận khách đã nhận phòng.
#11.Trả phòng: Xác nhận khách đã trả phòng, tính toán số tiền cần thanh toán.
#12.Xem danh sách đặt phòng: Hiển thị danh sách tất cả các đơn đặt phòng.
#13.Thêm nhân viên mới: Thêm thông tin một nhân viên mới vào hệ thống.
#14.Sửa thông tin nhân viên: Cập nhật thông tin của một nhân viên đã tồn tại.
#15.Xóa nhân viên: Xóa thông tin một nhân viên khỏi hệ thống.
#16.Xem danh sách nhân viên: Hiển thị danh sách tất cả các nhân viên.
#17.Xem báo cáo doanh thuHiển thị báo cáo doanh thu chi tiết.
#7,5,1,14,9,2
def check(file):
    if os.path.exists(file):
        return file
so=[]
loai=[]
gia=[]
status=[]
if __name__ == '__main__':
    file_phong='Phong.csv'
    if check(file_phong):
        with open(file_phong,'r', encoding='utf-8')as r:
            render=csv.DictReader(r)
            for row in render:
                so.append(row['Số phòng'])
                loai.append(row['Loại'])
                gia.append(row['Giá'])
                status.append(row['Trạng thái'])
    else:
        print('File khong ton tai!')
MaNv=[]
TenNV=[]
Chuc=[]
sdt=[]
DayJoin=[]
if __name__ == '__main__':
    file_nhanvien='NhanVien.csv'
    if check(file_phong):
        with open(file_nhanvien,'r', encoding='utf-8')as r:
            rende=csv.DictReader(r)
            for row in rende:
                MaNv.append(row['MaNv'])
                TenNV.append(row['HoTen'])
                Chuc.append(row['ChucVu'])
                sdt.append(row['Sdt'])
                DayJoin.append(row['NgayThamGia'])
    else:
        print('File khong ton tai!')
Number = []
Name =[]
PhoneNumber=[]
Info=[]
DateTakeRoom =[]
DateCheckIn=[]
DateCheckOut=[]
Status_Visitors=[]
if __name__ == '__main__':
    file_KHACH='KhachHang.csv'
    if check(file_KHACH):
        with open(file_KHACH,'r', encoding='utf-8')as r:
            rendr=csv.DictReader(r)
            for row in rendr:
                Number.append(row['SoPhong']) #Lay so phong file khachang
                Name.append(row['TenKhach'])
                PhoneNumber.append(row['Sdt'])
                Info.append(row['GiayTo'])
                DateTakeRoom.append(row['NgayDat'])
                DateCheckIn.append(row['NgayDen'])
                DateCheckOut.append(row['NgayDi'])
                Status_Visitors.append(row['StatusCheck'])
    else:
        print('File khong ton tai!')
def menu1(so,loai,gia,status):
    #System.Clear();
    print("Nhập thông tin của phòng muốn thêm:")
    phong=input("Số phòng: ")
    pl=input("Loại phòng: ")
    money=input("Giá thuê: ")
    tt=input("Tình trạng: ")
    ktr=0
    for i in range(len(so)):
        if so[i]==phong:
            print("Phòng bạn nhập đã có vui lòng nhập lại thông tin phòng cần thêm!")
            return menu1(so,loai,gia,status)
        if i==len(so)-1:
            so.append(phong)
            loai.append(pl)
            gia.append(money)
            status.append(tt)
            break
        if so[i]<phong and so[i+1]>phong and i!=len(so)-1:
            so.insert(i+1,phong)
            loai.insert(i+1,pl)
            gia.insert(i+1,money)
            status.insert(i+1,tt)
            break
    with open(file_phong,'w',encoding='utf-8') as f:
        WriteF = csv.DictWriter(f,fieldnames=['Số phòng','Loại','Giá','Trạng thái'])
        WriteF.writeheader()
        for i in range(len(so)):
            obj={
                'Số phòng':so[i],
                'Loại':loai[i],
                'Giá':gia[i],
                'Trạng thái':status[i]
            }
            WriteF.writerow(obj)
        print("Đã thêm thông tin phòng thành công!")
def menu2(so,status):
    #System.Clear();
    phong=input("Nhập số phòng bạn cần thay đổi: ")
    ktr=0
    dem=-1
    for i in range(len(so)):
        if so[i]==phong:
            ktr=1
            dem=i
            break
    if ktr==1:
        tt=str(input(f"Nhập trạng thái mới của phòng {phong}: "))
        status[dem]=tt
    else:
        print("Số phòng bạn nhập không tồn tại, hãy nhập lại!")
        return menu2(so,status)
    with open(file_phong,'w',encoding='utf-8') as f:
        WriteF = csv.DictWriter(f,fieldnames=['Số phòng','Loại','Giá','Trạng thái'])
        WriteF.writeheader()
        for i in range(len(so)):
            obj={
                'Số phòng':so[i],
                'Loại':loai[i],
                'Giá':gia[i],
                'Trạng thái':status[i]
            }
            WriteF.writerow(obj)
        print("Đã thay đổi trạng thái phòng thành công!")
def menu5(so,loai,gia,status):
    #System.Clear();
    for i in range(len(so)):
        if status[i]!="Yes":
            print(so[i],"\t\t",loai[i],"\t",gia[i],"\t",status[i])

def menu7():
    print("Số phòng\t\tTên Khách\t\tSĐT\t\t\t Giấy tờ\n")
    for i in range(len(Number)):
        print(Number[i],"\t\t\t",Name[i],"\t\t\t",PhoneNumber[i],"\t\t\t",Info[i])
def menu14():
    m=input("Nhập mã nhân viên cần thay đổi: ")
    dem=0
    if m in MaNv:
        for i in range(len(MaNv)):
            if m==MaNv[i]:
                print("Nhập thông tin nhân viên cần thay đổi:")
                n=input("Họ tên: ")
                c=input("Chức vụ: ")
                p=input("Số điện thoại: ")
                d=input("Ngày tham gia: ")
                TenNV[i]=n
                Chuc[i]=c
                sdt[i]=p
                DayJoin[i]=d
                break
    else:
        print("Mã nhân viên bạn nhâp không tồn tại, vui lòng nhập lại!")
        menu14()
    with open(file_nhanvien,'w',encoding='utf-8') as f:
        WriteF = csv.DictWriter(f,fieldnames=['MaNv','HoTen','ChucVu','Sdt','NgayThamGia'])
        WriteF.writeheader()
        for i in range(len(MaNv)):
            obj={
                'MaNv':MaNv[i],
                'HoTen':TenNV[i],
                'ChucVu':Chuc[i],
                'Sdt':sdt[i],
                'NgayThamGia':DayJoin[i]
            }
            WriteF.writerow(obj)
    print("Đã thay đổi thông tin nhân viên thành công!")
menu14()