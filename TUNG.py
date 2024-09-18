import  csv
import os, sys
import re
from pystyle import System

#  try expcet cai thu vien pystyle 
'''
16,8,4,15,12,13
4.Xem danh sách phòng: Hiển thị danh sách tất cả các phòng và tình trạng của chúng.
8.Đặt phòng mới: Tạo một đơn đặt phòng mới.
12.Xem danh sách đặt phòng: Hiển thị danh sách tất cả các đơn đặt phòng.
13.Thêm nhân viên mới: Thêm thông tin một nhân viên mới vào hệ thống.
15.Xóa nhân viên: Xóa thông tin một nhân viên khỏi hệ thống.
16.Xem danh sách nhân viên: Hiển thị danh sách tất cả các nhân viên.
'''
def TextMenu(choce,text_small):
     System.Clear()
     if choce==1:
          text=''
     elif choce==2:
          text=f'==================== {text_small}====================\n'
     elif choce==3:
          text=20
     else:
          pass
     return text


class Phong:
     def __init__(self,so_phong,loai,gia,trang_thai):
          self.so_phong=so_phong
          self.loai=loai
          self.gia=gia
          self.trang_thai=trang_thai

     
      
def check(file):
     if os.path.exists(file):
          return( file)
def AutoFile(file,ob,fomat):
     if check(file):
          pass
     else:
          with open(file,'a+',newline='',encoding='utf-8')as filecsv:
               format=fomat
               writer=csv.DictWriter(filecsv,fieldnames=format)
               writer.writerow(ob)
def INput(Type,Text,index):
     while  True:
          try:  
               if index==1:
                    nhap=Type(input(Text).upper())

               elif index==0:
                    nhap=Type(input(Text).lower())

               else:
                    nhap=Type(input(Text))
               return nhap
          except ValueError:
               print('Vui Long nhap dung ki tu ! \n')
               
def check_Date(text):
     dem=0
     while dem<2:
          tung=input(text)
          result=tung
          tung=re.finditer('-',tung)
          for num in tung:
               num=num.start()
               if num==4 or num==7:
                    dem+=1
               else:
                    # print('Nhap lai ',text)
                    dem=0
          if dem==0:
               print('\nError Nhập lại :((')
     return result


               
def Write_File(file,type,fomat,ob,headr):
     with open(file,type,newline='',encoding='utf-8') as file:
          render=csv.DictWriter(file,fieldnames=fomat)
          if headr:
               render.writeheader()
               render.writerow(ob)
          else:
               render.writerow(ob)
               
def menu4(file):
     print('Xem phong')
     with open(file,'r',newline='',encoding='utf-8') as file:
          render=csv.DictReader(file)
          print(f'Số phòng\t Loại\t  Giá\t Trạng thái')
          for row in render:
               so=row['Số phòng']
               loai=row['Loại']
               gia=row['Giá']
               status=row['Trạng thái']
               print(f'  {so}\t\t {loai}\t  {gia}\t {status}')
          
          
def readphong(file,loai):
     status='NO'
     with open(file,'r+',newline='',encoding='utf-8')as file:
          render=csv.DictReader(file)
          Item_Phong=[];Item_Gia=[]
          for row in render:
               trang_thai=row['Trạng thái'].upper()
               Loai=row['Loại'].upper()
               if trang_thai==status and Loai==loai :
                    phong=row['Số phòng']
                    gia=row['Giá']
                    Item_Phong.append(phong)
                    Item_Gia.append(gia)
          return Item_Phong,Item_Gia
                    
def ThayDoiStatus(file,room):
     status='Yes'
     with open(file,'r+',newline='',encoding='utf-8')as file:
          arr=[]
          fomat=['Số phòng','Loại','Giá','Trạng thái']
          render=csv.DictReader(file)
          for row in render:
               arr.append(row)
          for data in arr:
               if data['Số phòng'] == room:
                    data['Trạng thái']=status
     return arr
   
def menu8(filePhong,fileKhach):
     fomat_khach=['SoPhong','TenKhach','Sdt','GiayTo','NgayDat','NgayDen','NgayDi','StatusCheck']
     fomat_phong=['Số phòng','Loại','Giá','Trạng thái']
     print('Loai Phong Gom:\nGiaDinh,CapDoi,Don\n\n')
     LoaiPhong=INput(str,'Loai Phong: ',1)
     phong,gia=readphong(filePhong,LoaiPhong)
     if len(phong)>=1 :
          room=phong[0]
          Name=INput(str,'Ten Khach hang: ',1)
          Sdt=INput(int,'SDT Khach: ',2)
          Giay=INput(str,'Nhap Giay to: ',1)
          print(f'Check: [1]Nhan\n\t[]Len lich')
          check=INput(int,'Check luon or len lich: ',1)
          if check==1:
               NgayNhan=check_Date('Ngay Nhan')
               NgayDi=check_Date('Ngay Di')
               NgayDat=NgayNhan; check='Đã nhận'
          else:
               NgayDat=check_Date('Ngay Dat')
               NgayNhan=check_Date('Ngay Nhan')
               NgayDi=check_Date('Ngay Di')
               check='Lên lịch'  
          ob={
               'SoPhong':room,
               'TenKhach':Name,
               'Sdt':Sdt,
               'GiayTo':Giay,
               'NgayDat':NgayDat,
               'NgayDen':NgayNhan,
               'NgayDi':NgayDi,
               'StatusCheck':check
          }
          Write_File(fileKhach,'a+',fomat_khach,ob,False)
          data=ThayDoiStatus(filePhong,room)
          #  viet lai file
          for i,ob  in enumerate(data):
               # print(ob)
               if  i==0:
                    Write_File(filePhong,'w',fomat_phong,ob,True)
               else:
                    Write_File(filePhong,'a+',fomat_phong,ob,False)
                    
     else:
          print("<HET PHONG>\n\nRat mong quy khach thong cam !")
def view_all_Khach(file,check,text):
      with open (file, 'r',newline='',encoding='utf-8') as f:
          render=csv.DictReader(f)
          dem=-1
          for data in  render:
               if data['StatusCheck'].upper()==check.upper() and check.upper()=='YES': # YES la da nhan
                         dem+=1
                         # print(i)
                         soPhong=data['SoPhong']
                         Ten=data['TenKhach']
                         Sdt=data['Sdt']
                         Ngayden=data['NgayDen']
                         Ngaydi=data['NgayDi']
                         print(f'\t{soPhong}\t{Ten} {Sdt}\t{Ngayden}\t{Ngaydi}')
               elif check.upper()==data['StatusCheck'].upper(): # NO  la  da dat truoc
                         dem+=1
                         # print(i)
                         soPhong=data['SoPhong']
                         Ten=data['TenKhach']
                         Sdt=data['Sdt']
                         Ngayden=data['NgayDen']
                         Ngaydi=data['NgayDi']
                         NgayDat=data['NgayDat']
                         print(f'\t{soPhong}\t{Ten}    {Sdt}\t{NgayDat}\t{Ngayden}\t{Ngaydi}')
          else:
               if dem==-1:
                    print(f'\tKhông có {text}')

def menu12(file):
     #  check danh sach da dat phong trong file khach 
     print("Thông tin khách Đặt trước: \n") # chcek : NO --> Len lich
     print(f'\tSố phòng  Tên khách\t\tSdt\tNgay Đặt\tNgay Đến\tNgày Đi')
     view_all_Khach(file,'no','Dat Lich')
    
     print("Thông tin khách Đã Nhận: \n") # check : Yess--> Nhan
     print(f'\tSố phòng\tTên khách   Sdt\t\tNgay Đến\tNgày Đi\n')
     view_all_Khach(file,'yes','Dat Phong')

def check_MaNv(file,fomat):
     while True:
          kq=False
          Ma=INput(int,'Ma Nhan Vien: ',2)
          with open (file,'r', newline='',encoding='utf-8')as r:
               render=csv.DictReader(r); write=csv.DictReader(r,fieldnames=fomat)
               for read  in render :
                    Int=int(read['MaNv'].strip())
                    if  Int == Ma:
                         kq=True          
               return  kq,Ma
          
def menu13(file,fomat):
     print(TextMenu(2,'Add NhanVien'))
     while True:
          check,Ma=check_MaNv(file,fomat)
          if(check):
               print('\tMa Nv Tồn tại! \n\tNhập lại mã Nv')
          else:
               pass
               break;
     Ten=INput(str,'Ten Nhan Vien: ',1)
     ChucVu=INput(str,'Chuc vu Nv: ',1)
     Sdt=INput(int,'Sdt',1)
     print("Date Tham Gia (y/m/d)")
     date=check_Date('\tNgay Lam vc: ')
     ob_NhanVien={
          'MaNv':Ma,
          'HoTen':Ten,
          'ChucVu':ChucVu,
          'Sdt':Sdt,
          'NgayThamGia':date   
     }
     Write_File(file,'a+',fomat,ob_NhanVien,False)
     print(f'Thêm nhân viên thành công!')


def Del_NhanVien(file,type,Ma):
     arr=[]
     with open(file,type,newline='',encoding='utf-8')as  file:
          render=csv.DictReader(file)
          for data in render:
               MaNv=int(data['MaNv'].strip())
               if MaNv!= Ma:
                    arr.append(data)
          return arr
          
             
def menu15(file,fomat):
     # xoa nhan vien
     print(TextMenu(2,'Xoa Nhan Vien'))
     while True:
          check,Ma=check_MaNv(file,fomat) # kt ma co ton tai hay khong
          if(check):
               ob_NhanVien=Del_NhanVien(file,'r+',Ma) # tra ve arr-obj  ===>  data
               with open(file,'w',newline='',encoding='utf-8')as file:
                    clear=csv.DictWriter(file,fieldnames=fomat)
                    clear.writeheader()
               for ob in  ob_NhanVien:
                         Write_File(file,'a',fomat,ob,False)
               break;       
          else:
               print('\tMa Nv Không Tồn tại! \n\tNhập lại mã Nv')
          
def menu16():
     # xem danh sach nhan vien
     pass

 
if  __name__=='__main__':
#//// data duong dan chuyen vao
     file_phong=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Phong.csv'
     file_Khach=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\KhachHang.csv'
     file_NhanVien=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\NhanVien.csv'
     
     ob_phong={
          'Số phòng':'Số phòng',
          'Loại':'Loại',
          'Giá':'Giá',
          'Trạng thái':'Trạng thái'    
     }
     ob_khach={
          'SoPhong':'Sophong',
          'TenKhach':'TenKhach',
          'Sdt':'Sdt',
          'GiayTo':'GiayTo',
          'NgayDat':'NgayDat',
          'NgayDen':'NgayDen',
          'NgayDi':'NgayDi',
          'StatusCheck':'StatusCheck'
     }
     ob_NhanVien={
          'MaNv':'MaNv',
          'HoTen':'HoTen',
          'ChucVu':'ChucVu',
          'Sdt':'Sdt',
          'NgayThamGia':'NgayThamGia'   
     }

     fomat_khach=['SoPhong','TenKhach','Sdt','GiayTo','NgayDat','NgayDen','NgayDi','StatusCheck']
     fomat_phong=['Số phòng','Loại','Giá','Trạng thái']
     fomat_nhanVien=['MaNv','HoTen','ChucVu','Sdt','NgayThamGia']
#////Check  file auto tao file
     AutoFile(file_phong,ob_phong,fomat_phong)
     AutoFile(file_Khach,ob_khach,fomat_khach)
     AutoFile(file_NhanVien,ob_NhanVien,fomat_nhanVien)

#////Claer trong termial     
     System.Clear()

#////All Menu
     # menu4(file_phong)
    
     menu8(file_phong,file_Khach)
     
     # menu12(file_Khach)
     
     # menu13(file_NhanVien,fomat_nhanVien)


     # a=Del_NhanVien(file_NhanVien,'r',122)
     # # print(a) 
     # for i,data in enumerate(a):
     #      if  i==1:
     #           print(data)
     #           Write_File(file_NhanVien,'a',fomat_nhanVien,data,True)
     # print(len(a))
     # menu15(file_NhanVien,fomat_nhanVien)     
