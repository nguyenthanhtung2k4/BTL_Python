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
     
'''
16,8,4,15,12,13
'''
def TextMenu(choce,text_small):

     if choce==1:
          text=f'''
{color_bar}==================== {colorB_logo+colorF_logo}All Menu{RESETs+color_bar} ====================

{colorF_logo+colorB_logo}0. {RESETs+colorF_logo}Thoát chương trình
{colorF_logo+colorB_logo}1. {RESETs+colorF_logo}Thêm phòng mới
{colorF_logo+colorB_logo}2. {RESETs+colorF_logo}Sửa thông tin phòng
{colorF_logo+colorB_logo}3. {RESETs+colorF_logo}Xóa phòng
{colorF_logo+colorB_logo}4. {RESETs+colorF_logo}Xem danh sách phòng
{colorF_logo+colorB_logo}5. {RESETs+colorF_logo}Hiện  thị  các phòng trống
{colorF_logo+colorB_logo}6. {RESETs+colorF_logo}Sửa thông tin khách hàng
{colorF_logo+colorB_logo}7. {RESETs+colorF_logo}Xem danh sách khách hàng
{colorF_logo+colorB_logo}8. {RESETs+colorF_logo}Đặt phòng mới
{colorF_logo+colorB_logo}9. {RESETs+colorF_logo}Hủy đặt phòng
{colorF_logo+colorB_logo}10. {RESETs+colorF_logo}Nhận phòng
{colorF_logo+colorB_logo}11. {RESETs+colorF_logo}Trả phòng
{colorF_logo+colorB_logo}12. {RESETs+colorF_logo}Xem danh sách đặt phòng
{colorF_logo+colorB_logo}13. {RESETs+colorF_logo}Thêm nhân viên mới
{colorF_logo+colorB_logo}14. {RESETs+colorF_logo}Sửa thông tin nhân viên
{colorF_logo+colorB_logo}15. {RESETs+colorF_logo}Xóa nhân viên
{colorF_logo+colorB_logo}16. {RESETs+colorF_logo}Xem danh sách nhân viên
{colorF_logo+colorB_logo}17. {RESETs+colorF_logo}Hiển thị báo cáo doanh thu chi tiết.{RESETs+colorF_logo}
{colorF_logo+colorB_logo}18. {RESETs+colorF_logo}Setting
{colorF_logo+colorB_logo}19. {RESETs+colorF_logo}About

'''
     elif choce==2:
          text=f'{colorF_logo}==================== {colorF_logo+colorB_logo}{text_small} {RESETs+colorF_logo}===================={RESETs}\n'
     elif choce==3:
          text=20
     else:
          pass
     return text

def check(file):
     if os.path.exists(file):
          return( file)
def AutoFile(file,fomat):
     if check(file):
          pass
     else:
          with open(file,'a+',newline='',encoding='utf-8')as filecsv:
               format=fomat
               writer=csv.DictWriter(filecsv,fieldnames=format)
               writer.writeheader()
def INput(Type,Text,index):
     while  True:
          try:  
               if index==1:
                    nhap=Type(input(colorF+Text).upper())

               elif index==0:
                    nhap=Type(input(colorF+Text).lower())

               else:
                    nhap=Type(input(colorF+Text))
               return nhap
          except ValueError:
               print(f'{erF}Vui Long nhap dung {erF+erB} ki tu ! {RESETs}\n')
               
def check_Date(text):
     while True:
          text=input(text)
          try:
               y,m,d= map(int,text.split('-'))
               if  y>=1000 and 1<=m<=12 and  1<=d<=31:
                    break
               else:
                    print(f'{colorF}Định dạng Năm-Tháng-Ngày\n{erF}Vui Lòng Nhập Lại{RESETs}')
          except:
               print(f'{erB}Cú Pháp Sai :((')
     return text

               
def Write_File(file,type,fomat,ob,headr):
     with open(file,type,newline='',encoding='utf-8') as file:
          render=csv.DictWriter(file,fieldnames=fomat)
          if headr:
               render.writeheader()
               render.writerow(ob)
          else:
               render.writerow(ob)
               
def menu4(file):
     System.Clear();# print('Xem phong')
     with open(file,'r',newline='',encoding='utf-8') as file:
          render=csv.DictReader(file)
          print(f'{colorF}Số phòng\t Loại\t  Giá\t Trạng thái{RESETs}')
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
     System.Clear()
     fomat_khach=['SoPhong','TenKhach','Sdt','GiayTo','NgayDat','NgayDen','NgayDi','StatusCheck']
     fomat_phong=['Số phòng','Loại','Giá','Trạng thái']
     print(f'{RESETs}Loại phòng gồm:\nTo,Đôi,Đơn\n\n')
     LoaiPhong=INput(str,'Loại Phòng: ',1)
     phong,gia=readphong(filePhong,LoaiPhong)
     if len(phong)>=1 :
          room=phong[0]
          Name=INput(str,'Tên Khách Hàng: ',1)
          Sdt=INput(int,'SĐT Khách: ',2)
          Giay=INput(str,'Nhập Giấy Tờ: ',1)
          print(f'{colorF}Check: [1]Nhận\n\t[]Lên Lịch')
          check=INput(int,'Check luôn or lên lịch: ',1)
          if check==1:
               NgayNhan=check_Date('Ngày Nhận: ')
               NgayDi=check_Date('Ngày Đi: ')
               NgayDat=NgayNhan; check='Yes' # check = da nhan
          else:
               NgayDat=check_Date('Ngày Đặt:')
               NgayNhan=check_Date('Ngày Nhận: ')
               NgayDi=check_Date('Ngày Đi: ')
               check='No'  # check=  len lich
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
          System.Clear()
          print(f'\n{colorB}Đặt Phòng Thành Công !{RESETs}\n')         
     else:
          print(f"{RESETs+erB}<HẾT PHÒNG>\n\n{colorF}Rất mong quý khách thông cảm !{RESETs}")
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
                    print(f'\t{RESETs+erB}Không có {text+RESETs}')

def menu12(file):
     System.Clear()
     #  check danh sach da dat phong trong file khach 
     print(f"{RESETs+colorB}Thông tin khách Đặt trước: {RESETs}\n") # chcek : NO --> Len lich
     print(f'\t{colorF}Số phòng  Tên khách\t\tSdt\tNgày Đặt\tNgày Đến\tNgày Đi')
     view_all_Khach(file,'no','Đặt Lịch')
    
     print(f"{RESETs+colorB}Thông tin khách Đã Nhận:{RESETs} \n") # check : Yess--> Nhan
     print(f'\t{colorF}Số phòng\tTên khách   Sdt\t\tNgày Đến\tNgày Đi{RESETs}\n')
     view_all_Khach(file,'yes','Đặt Phòng')

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
     System.Clear()
     print(TextMenu(2,'Add Nhân Viên'))
     while True:
          check,Ma=check_MaNv(file,fomat)
          if(check):
               print(f'\t{color_bar}Mã Nv Tồn tại! \n\t{erF}Nhập lại mã Nv{RESETs}')
          else:
               pass
               break;
     Ten=INput(str,'Tên Nhân Viên: ',1)
     ChucVu=INput(str,'Chức vụ: ',1)
     Sdt=INput(int,'SĐT: ',1)
     print("Date Tham Gia (y/m/d)")
     date=check_Date('\tNgày Làm vc: ')
     ob_NhanVien={
          'MaNv':Ma,
          'HoTen':Ten,
          'ChucVu':ChucVu,
          'Sdt':Sdt,
          'NgayThamGia':date   
     }
     Write_File(file,'a+',fomat,ob_NhanVien,False)
     print(f'{RESETs+colorF}Thêm nhân viên thành công!{RESETs}')


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
     System.Clear()
     # xoa nhan vien
     print(TextMenu(2,'Xóa Nhân Viên'))
     while True:
          check,Ma=check_MaNv(file,fomat) # kt ma co ton tai hay khong
          if(check):
               ob_NhanVien=Del_NhanVien(file,'r+',Ma) # tra ve arr-obj  ===>  data   
               with open(file,'w',newline='',encoding='utf-8')as file:
                    clear=csv.DictWriter(file,fieldnames=fomat)
                    clear.writeheader()
                    for ob in  ob_NhanVien:
                         clear.writerow(ob)
               break
          else:
               print(f'\t{erB}Mã Nv Không Tồn tại!{RESETs} \n\t{colorF}Nhập lại mã Nv{RESETs}')
     if len(ob_NhanVien)>-1:
          pass
     else:
          print(f'{RESETs+colorB}Lỗi xóa nhân viên :(({RESETs}')
  
def menu16(file):
     System.Clear()
     # xem danh sach nhan vien
     print(TextMenu(2,'Xem danh sách nhân viên'))
     with open(file,'r',newline='',encoding='utf-8') as  file:
          next(file) # bo qua dong dau
          length=file.readline()# check  do dai  file
          if length> '0':
               render=csv.DictReader(file)
               print(f'{colorF}MaNv\tHoTen\t\tChucVu\tSdt\tNgayThamGia{RESETs}')
               for data  in  render:
                    Ma=data['MaNv']
                    HoTen=data['HoTen']
                    ChucVu=data['ChucVu']
                    Sdt=data['Sdt']
                    NgayThamgia=data['NgayThamGia']
                    print(f'{Ma}\t{HoTen}\t{ChucVu}\t{Sdt}\t{NgayThamgia}')
          else:
                    print(f'\t\t   {RESETs+color_bar}Danh Sách Trống rỗng !{RESETs}')
                    quit;
def about():
     System.Clear()
     about=f'''{RESETs+colorB}
\t\tVề chúng tôi{RESETs+colorF}
\tChương trình được phát triển bởi các sinh viên Đại Nam phát triển
 - Các sinh viên thực hiện:
                    Nguyễn Thanh Tùng
                    Lê Văn Vượng
                    Bùi Quang Tuấn
Chương trình được thiết kế để giúp các khách sạn nâng cao chất lượng dịch vụ,tối ưu hóa quy trình hoạt động và tăng doanh thu.Chúng tôi phát triển gồm 20 chức năng để quản lý khách sản một cách tận tiện nhất
{RESETs}
'''
     for  i  in about:
          sys.stdout.write(i)
          sleep(0.025)
def Update_Color():
     f={
     "F1":"\033[30m"  ,     # black
     "F2":"\033[31m",       # red
     "F3":"\033[32m"  ,     # green
     "F4":"\033[33m"   ,    # yellow
     "F5":"\033[34m" ,      # blue
     "F6":"\033[35m"    ,   # magenta
     "F7":"\033[36m" ,      # cyan
     "F8":"\033[37m"  ,     # white
     "F0":"\033[39m"      # reset
     }
     # /////////// Back color
     b={
          "B1":"\033[40m"  ,    # black
          "B2":"\033[41m",      # red
          "B3":"\033[42m"  ,    # green
          "B4":"\033[43m"   ,   # yellow
          "B5":"\033[44m" ,     # blue
          "B6":"\033[45m"    ,  # magenta
          "B7":"\033[46m" ,     # cyan
          "B8":"\033[47m"  ,    # white
          "B0":"\033[49m"      # reset
     }
     with open(file_Setting,'r')as file:
          data=json.load(file)
          Font_Logo=data['Setting']['Font_Logo']
          Back_Logo=data['Setting']['Back_Logo']
          Bar_Logo=data['Setting']['Bar_Logo']
          Font_color=data['Setting']['Font_Color']
          Back_color=data['Setting']['Back_Color']
          Font_ERROR=data['Setting']['Font_ERROR']
          Back_ERROR=data['Setting']['Back_ERROR']
          for i  in f :# check font
               if  Font_color== i:
                    Font_color=f[i]
               if  Font_ERROR== i:
                    Font_ERROR=f[i]
               if Bar_Logo == i:
                    Bar_Logo=f[i]
               if Font_Logo== i:
                    Font_Logo=f[i]
          for  j in b:#check back
               if  Back_color== j:
                    Back_color=b[j]
               if Back_ERROR == j:
                    Back_ERROR =b[j]
               if Back_Logo==j:
                    Back_Logo=b[j]
                    
          return Font_Logo,Back_Logo,Bar_Logo ,Font_color,Back_color,Font_ERROR,Back_ERROR;
def read_Table_color():
     with open(file_Setting,'r') as f:
          data=json.load(f)
          return data
def setting(file_setting):
     System.Clear()
     data_Setting=read_Table_color()
     print('[1]Version\n[2]Setting\n[3]About')
     nhap=INput(int,'Nhập ',2)
     if nhap==1:
          System.Clear()
          version='TVT_1.10'
          print(f'\n\nVersion: {version}\n\n')
     elif nhap==2:
          print(f'''
{colorB_logo+colorF_logo}[1]{colorF_logo}Font_Color
{colorB_logo+colorF_logo}[2]{colorF_logo}Back_Color
{colorB_logo+colorF_logo}[3]{colorF_logo}Font_ERROR
{colorB_logo+colorF_logo}[2]{colorF_logo}Back_ERROR
{colorB_logo+colorF_logo}[4]{colorF_logo}Delay_logo
{colorB_logo+colorF_logo}[5]{colorF_logo}Delay_about       
               ''')
          nhap=INput(int,f'Lựa chọn',2)
          if nhap==1:
               for c,color in enumerate(data_Setting['Tabale']['Font'].values()):
                    print(f'[{c}]{color}')
               
               font_color=INput(int,f'Chọn màu chữ',2)
               font_color=f'F{font_color}'
               data_Setting['Tabale']['Font'][font_color]=font_color
               
def Auto_Color():
     if check(file_Setting):
          pass
     else:
          with open(file_Setting,'w+')as f:
               ob={"Setting": {"Font_Color": "F5", "Font_ERROR": "F2", "Back_Color": "B0", "Back_ERROR": "B4"}, "Delay": {"Time_logo": 0.025, "Time_About": 0.025}, "Tabale": {"Font": {"0": "Mac dinh", "1": "Black", "2": "Red", "3": "Green", "4": "yellow", "5": "Blue", "6": "Magenta", "7": "Cyan", "8": "White"}, "Back": {"0": "Mac dinh", "1": "Black", "2": "Red", "3": "Green", "4": "yellow", "5": "Blue", "6": "Magenta", "7": "Cyan", "8": "White"}}}
               json.dump(ob,f,indent=4);
         
def error():
     System.Clear()
     print(f'{erF}Lựa chọn {erB+erF}không hợp lệ !{RESETs}')

    
if  __name__=='__main__':
#//// data duong dan chuyen vao
     file_phong=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Phong.csv'
     file_Khach=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\KhachHang.csv'
     file_NhanVien=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\NhanVien.csv'
     file_Setting=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Setting.json'

     fomat_khach=['SoPhong','TenKhach','Sdt','GiayTo','NgayDat','NgayDen','NgayDi','StatusCheck']
     fomat_phong=['Số phòng','Loại','Giá','Trạng thái']
     fomat_nhanVien=['MaNv','HoTen','ChucVu','Sdt','NgayThamGia']
#////Check  file auto tao file
     AutoFile(file_phong,fomat_phong)
     AutoFile(file_Khach,fomat_khach)
     AutoFile(file_NhanVien,fomat_nhanVien)
     Auto_Color() #auto tao file color

#////Claer trong termial
     System.Clear()
     
#////All Menu 16,8,4,15,12,13
     options={
          1: lambda: menu1(file_phong),
          2: lambda: menu2(file_phong),
          3: lambda: menu3(file_phong),
          4: lambda: menu4(file_phong),
          5: lambda: menu5(file_phong),
          6: lambda: menu6(file_Khach,file_phong),
          7: lambda: menu7(file_Khach),
          8: lambda: menu8(file_phong,file_Khach),
          9: lambda: menu9(file_Khach),
          10: lambda: menu10(file_Khach),
          11: lambda: menu11(file_phong,file_Khach),
          12: lambda: menu12(file_Khach),
          13: lambda: menu13(file_NhanVien,fomat_nhanVien),
          14: lambda: menu14(file_NhanVien),
          15: lambda: menu15(file_NhanVien,fomat_nhanVien),
          16: lambda: menu16(file_NhanVien),
          17: lambda: menu17(file_phong,file_Khach),
          18: lambda: setting(file_Setting),
          19: lambda: about(),
     }
     Back_RESET="\033[49m";Font_RESET="\033[39m"
     RESETs=Back_RESET+Font_RESET
# //////  update color
     # Update_Color()
     colorF_logo,colorB_logo,color_bar, colorF,colorB,erF,erB=Update_Color()
     # print(colorF,colorB,erF,erB)
# //////////////////// TEST
     # setting(file_Setting)
     
     
     
     
     
     
     
     
     
     
     
     
# ///////////////////////////
     
#  ///  about
     for i in  TextMenu(1,''):
          sys.stdout.write(i)
          sleep(0.009)
     dem=0;
     while True:
          #  update  color
          dem+=1
          if dem>1:
               print(TextMenu(1,f'{colorB}All Menu{RESETs}'))
          Nhap=INput(int,f'{colorF}Chọn Chức Năng\n==> {RESETs}',2)
          if Nhap == 0:
               System.Clear()
               print(f'{erF}Tạm biệt !{Back_RESET+Font_RESET}') 
               break;
          options.get(Nhap,lambda: error())()

#  chinh  setting +  menu chx xog