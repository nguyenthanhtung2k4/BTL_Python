import csv,json,sys,os
from pystyle import System
from time import*
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
def Auto_Color(file_setting):
     if check(file_setting):
          pass
     else:
          with open(file_setting,'w+')as f:
               ob={"Setting": {"Font_Logo": "F4", "Back_Logo": "B0", "Font_Color": "F8", "Back_Color": "B1", "Font_ERROR": "F2", "Back_ERROR": "B5"}, "Delay": {"Time_logo": 0.0025, "Time_About": 0.025}, "Tabale": {"Font": {"0": "Blue", "1": "Black", "2": "Red", "3": "Green", "4": "yellow", "5": "Mac dinh", "6": "Magenta", "7": "Cyan", "8": "White"}, "Back": {"0": "Black", "1": "Mac dinh", "2": "Red", "3": "Green", "4": "yellow", "5": "Blue", "6": "Magenta", "7": "Cyan", "8": "White"}}}
               json.dump(ob,f,indent=4);
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
          sleep(time_about)
          

def Update_Color(file_Setting):
     f={
     "F0":"\033[34m" ,      # blue
     "F1":"\033[30m"  ,     # black
     "F2":"\033[31m",       # red
     "F3":"\033[32m"  ,     # green
     "F4":"\033[33m"   ,    # yellow
     "F5":"\033[39m",      # reset
     "F6":"\033[35m"    ,   # magenta
     "F7":"\033[36m" ,      # cyan
     "F8":"\033[37m"       # white
     }
     # /////////// Back color
     b={
          "B0":"\033[40m"  ,    # black
          "B1":"\033[49m"  ,    # reset
          "B2":"\033[41m",      # red
          "B3":"\033[42m"  ,    # green
          "B4":"\033[43m"   ,   # yellow
          "B5":"\033[44m" ,     # blue
          "B6":"\033[45m"    ,  # magenta
          "B7":"\033[46m" ,     # cyan
          "B8":"\033[47m"      # white
     }
     with open(file_Setting,'r')as file:
          data=json.load(file)
          Font_Logo=data['Setting']['Font_Logo']
          Back_Logo=data['Setting']['Back_Logo']
          Font_color=data['Setting']['Font_Color']
          Back_color=data['Setting']['Back_Color']
          Font_ERROR=data['Setting']['Font_ERROR']
          Back_ERROR=data['Setting']['Back_ERROR']
          for i  in f :# check font
               if  Font_color== i:
                    Font_color=f[i]
               if  Font_ERROR== i:
                    Font_ERROR=f[i]
               if Font_Logo== i:
                    Font_Logo=f[i]
          for  j in b:#check back
               if  Back_color== j:
                    Back_color=b[j]
               if Back_ERROR == j:
                    Back_ERROR =b[j]
               if Back_Logo==j:
                    Back_Logo=b[j]
          color_bar="\033[32m"
          Back_RESET="\033[49m";Font_RESET="\033[39m"
          RESETs=Back_RESET+Font_RESET    
          time_logo=data['Delay']['Time_logo']
          time_about=data['Delay']['Time_About']
          return color_bar,Font_Logo,Back_Logo,Font_color,Back_color,Font_ERROR,Back_ERROR,RESETs,time_logo,time_about;
def read_Table_color(file_Setting):
     with open(file_Setting,'r') as f:
          data=json.load(f)
          return data
# Thay doi mau color tronag setting
def TableColor(file_setting,text,format,noteMau):
     System.Clear()
     data_Setting=read_Table_color(file_setting)
     System.Clear()
     for c,color in enumerate(data_Setting['Tabale'][format].values()):
          print(f'[{c}]{color}')
     font_color=INput(int,text,9)
     if font_color==0:
          font_color=noteMau
     else:
          font_color=f'F{font_color}'
     with open(file_setting,'r')as file:
          data=json.load(file)
          data['Setting']['Font_Color']=font_color
          with open(file_setting,'w')as file:
               json.dump(data,file,indent=4)
               print(f'\n\nFont_Color đã thay đ��i thành {font_color}\n\n')
#  setting
def setting(file_setting):
     System.Clear()
     while True:
          print('[1]Version\n[2]Setting\n[3]About\n[4]Exit')
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
{colorB_logo+colorF_logo}[4]{colorF_logo}Back_ERROR
{colorB_logo+colorF_logo}[5]{colorF_logo}Font_Logo  
{colorB_logo+colorF_logo}[6]{colorF_logo}Back_Logo 
{colorB_logo+colorF_logo}[7]{colorF_logo}Delay
     
               ''')
               nhap=INput(int,f'Lựa chọn',2)
               if nhap==1:
                    format='Font'
                    TableColor(file_setting,'Nhập màu Font_Color',format,'F8')
               elif nhap==2:
                    format='Back'
                    TableColor(file_setting,'Nhập màu Back_Color',format,'B1')
               elif nhap==3:
                    format='Font'
                    TableColor(file_setting,'Nhập màu Font_ERROR',format,'F2')
               elif nhap==4:
                    format='Back'
                    TableColor(file_setting,'Nhập màu Back_ERROR',format,'B5')
               elif nhap==5:
                    TableColor(file_setting,'Nhập màu Font_Logo',"Font",'F4')
               elif nhap==6:
                    TableColor(file_setting,'Nhập màu Back_ERROR','Back','B0')
               elif nhap==7:
                    logo=INput(int,'Nhập Delay_logo[0 Mac dinh]: ',2)
                    about=INput(int,'Nhập Delay_About[0 Mac dinh]: ',2)
                    if logo==0:
                         logo=0.0025
                    elif about==0:
                         about=0.025
                    else:
                         with open(file_setting,'r')as file:
                              data=json.load(file)
                              data['Setting']['Delay_logo']=logo
                              with open(file_setting,'w')as file:
                                   json.dump(data,file,indent=4)
                                   print(f'\n\nDelay_logo đã thay đ��i thành {nhap}\n\n')
          elif nhap==3:
               System.Clear()
               about()
          else:
               System.Clear()
               Update_Color(file_setting)
               break;
#  Đường dẫn sẽ được để ở phần main, mọi cài đặt liên quan đường dẫn fomat color sẽ được nẳm trong  def main()
def  main():
#  Khai bao biến global
     global file_phong,file_Khach,file_NhanVien,file_setting;
     global fomat_khach,fomat_phong,fomat_nhanVien;
     global color_bar, colorF_logo,colorB_logo, colorF,colorB,erF,erB,RESETs,time_logo,time_about;
#//// data duong dan chuyen vao
     file_phong='Phong.csv'
     file_Khach='KhachHang.csv'
     file_NhanVien='NhanVien.csv'
     file_setting='Setting.json'
#  format csv sẽ được khai báo ở đây.
     fomat_khach=['SoPhong','TenKhach','Sdt','GiayTo','NgayDat','NgayDen','NgayDi','StatusCheck']
     fomat_phong=['Số phòng','Loại','Giá','Trạng thái']
     fomat_nhanVien=['MaNv','HoTen','ChucVu','Sdt','NgayThamGia']
#  check file setting
     #////Check  file auto tao file
     AutoFile(file_phong,fomat_phong)
     AutoFile(file_Khach,fomat_khach)
     AutoFile(file_NhanVien,fomat_nhanVien)
     Auto_Color(file_setting) #auto tao file color
#  trả về biến toàn cục color
     color_bar,colorF_logo,colorB_logo,colorF,colorB,erF,erB,RESETs,time_logo,time_about=Update_Color(file_setting)
main()