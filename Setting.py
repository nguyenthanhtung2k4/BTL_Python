import csv,json,sys,os
from pystyle import System
from time import*
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
          sleep(0.025)
def Update_Color(file_Setting):
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
          Back_RESET="\033[49m";Font_RESET="\033[39m"
          RESETs=Back_RESET+Font_RESET    
          return Font_Logo,Back_Logo,Bar_Logo ,Font_color,Back_color,Font_ERROR,Back_ERROR,RESETs;
def setting(file_setting):
     System.Clear()
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
               System.Clear()
               font_color=INput(int,f'Chọn màu chữ',9)
               if font_color==0:
                    font_color='F5'
               else:
                    font_color=f'F{font_color}'
               with open(file_setting,'r')as file:
                    data=json.load(file)
                    data['Setting']['Font_Color']=font_color
                    with open(file_setting,'w')as file:
                         json.dump(data,file,indent=4)
                         print(f'\n\nFont_Color đã thay đ��i thành {font_color}\n\n')
  
def  main():
     file_Setting=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Setting.json'
     global colorF_logo,colorB_logo,color_bar, colorF,colorB,erF,erB,RESETs;
     colorF_logo,colorB_logo,color_bar, colorF,colorB,erF,erB,RESETs=Update_Color(file_Setting)
main()