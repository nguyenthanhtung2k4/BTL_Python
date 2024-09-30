import csv
import os
from pystyle import System
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
            
def ReadFile(filename):
     phong=[];loai=[];gia=[];tt=[]
     with open(filename, 'r',newline='',encoding='utf-8') as f:
          reader = csv.DictReader(f)
          for  row in  reader:
               phong.append(row['Số phòng'])
               loai.append(row['Loại'])
               gia.append(row['Giá'])
               tt.append(row['Trạng thái'])
          return phong,loai,gia,tt

def Write_File(file,type,fomat,ob,headr):
     with open(file,type,newline='',encoding='utf-8') as file:
          render=csv.DictWriter(file,fieldnames=fomat)
          if headr:
               render.writeheader()
               render.writerow(ob)
          else:
               render.writerow(ob)

def Write_Arr_File(file,fomat,so,loai,gia,status):
     # print(f'phong:{so}\n{loai}:{status}\n{gia}')   
     with open(file,'w',newline='',encoding='utf-8') as file:
          render=csv.DictWriter(file,fieldnames=fomat)
          render.writeheader()
          for i in range(len(so)):
               ob_phong={
               'Số phòng':so[i],
               'Loại':loai[i],
               'Giá':gia[i],
               'Trạng thái':status[i],
               }
               render.writerow(ob_phong)
def menu1(file,flat):
     if flat:
          System.Clear();
     fomat_phong=['Số phòng','Loại','Giá','Trạng thái']
     so,loai,gia,status=ReadFile(file)
     print("Nhập thông tin của phòng muốn thêm:")
     phong=input("Số phòng: ")
     pl=input("Loại phòng: ")
     money=input("Giá thuê: ")
     tt=int(input("\t[1]Đã Nhận Phòng\t[2]Phòng Trống\nTình trạng: "))
     if tt==1:
          tt='Yes'
     else:
          tt='No'
     for i in range(len(so)):
          if so[i]==phong:
               print("\n\tPhòng đã tồn tại!\n")
               return menu1(file,False)
               
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
               print("Đã thêm thông tin phòng thành công!")
               break  
     Write_Arr_File(file,fomat_phong,so,loai,gia,status)
      
def menu2(file,flat):
     if flat:
          System.Clear();
     fomat_phong=['Số phòng','Loại','Giá','Trạng thái']
     so,loai,gia,status=ReadFile(file)
     phong=input("Nhập số phòng bạn cần thay đổi: ")
     ktr=0
     dem=-1
     for i in range(len(so)):
          if so[i]==phong:
               ktr=1
               dem=i
               break
     if ktr==1:
          print('\n[1]Đã NHận Phòng\t[2]Lên lịch')
          nhap=INput(int,f"Nhập trạng thái mới của phòng {phong}: ",2)
          if nhap==1:
               status[dem]='Yes'
          else:
               status[dem]='No'
          print(f'\n\tThành Công!\nĐã thay đổi trạng thái phòng {phong}\n')
               
     else:
          print("\n\tSố phòng bạn nhập không tồn tại, hãy nhập lại!")
          return menu2(file,False)
     Write_Arr_File(file,fomat_phong,so,loai,gia,status)

def menu5(file,flat):
     if flat:  
          System.Clear();
     with open(file,'r',newline='',encoding='utf-8') as file:
          reader = csv.DictReader(file)
          for  row in  reader:
               if row['Trạng thái'].upper()!='YES':
                    print(f'{row["Số phòng"]}\t{row["Loại"]}\t{row["Giá"]}\t{row["Trạng thái"]}')

def menu7():
     System.Clear();
     print(f'\n\nCảm ơn bạn đã quan tâm chức năng này!\nChúng tôi sẽ sớm phát triển xog chức năng này\n\n\tChọn chức năng khác \n\t THANK YOU!')
def menu9():
     System.Clear();
     print(f'\n\nCảm ơn bạn đã quan tâm chức năng này!\nChúng tôi sẽ sớm phát triển xog chức năng này\n\n\tChọn chức năng khác \n\t THANK YOU!')
def menu14():
     System.Clear();
     print(f'\n\nCảm ơn bạn đã quan tâm chức năng này!\nChúng tôi sẽ sớm phát triển xog chức năng này\n\n\tChọn chức năng khác \n\t THANK YOU!')
def menu17():
     System.Clear();
     print(f'\n\nCảm ơn bạn đã quan tâm chức năng này!\nChúng tôi sẽ sớm phát triển xog chức năng này\n\n\tChọn chức năng khác \n\t THANK YOU!')
if __name__ == "__main__":
     file_phong=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Phong.csv'
     erF='';erB='';colorF='';RESETs='';
     # menu1(file_phong,True);
     # menu2(file_phong,True)
     # menu5(file_phong,True);