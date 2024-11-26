from Setting import*
from Main import TextMenu
import csv,sys         
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
               loai=row['Loại'].upper()
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
               if trang_thai==status and Loai==loai.upper() :
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
          print(f'\n{colorB}Số phòng là: {room}\n\t Giá qua đêm là: {gia[0]}')         
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
               print(f'\t{erF}Mã Nv Tồn tại! \n\t{erF}Nhập lại mã Nv{RESETs}')
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
def menu16(file_NhanVien):
     System.Clear()
     # xem danh sach nhan vien
     print(TextMenu(2,'Xem danh sách nhân viên'))
     with open(file_NhanVien,'r',newline='',encoding='utf-8') as  file:
               render=csv.DictReader(file)
               print(f'{colorF}MaNv\tHoTen\t\tChucVu\tSdt\tNgayThamGia{RESETs}')
               for data  in  render:
                    Ma = data['MaNv']
                    HoTen = data['HoTen']
                    ChucVu = data['ChucVu']
                    Sdt = data['Sdt']
                    NgayThamgia = data['NgayThamGia']
                    print(f'{Ma}\t{HoTen}\t{ChucVu}\t{Sdt}\t{NgayThamgia}')   