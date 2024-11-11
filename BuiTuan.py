import csv
import os
from datetime import datetime
from Setting import*
def check(file):
    return os.path.exists(file)
def load_data(file, keys):
    data = {key: [] for key in keys}
    if check(file):
        with open(file, 'r', encoding='utf-8') as r:
            reader = csv.DictReader(r)
            for row in reader:
                for key in keys:
                    data[key].append(row[key])
    else:
        print(f'{erF}File {file}{erB}không tồn tại!{RESETs}')
    return data

def save_data(file, data):
    keys = data.keys() ## lay fomat csv
    with open(file, 'w', encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for i in range(len(data[next(iter(keys))])):
            row = {key: data[key][i] for key in keys}
            writer.writerow(row)
    print(f'{colorF}Đã lưu dữ liệu vào file {file} thành công!')
def load_data_khach_hang(file,keys, phong):
    data={key: [] for key in keys}
    if check(file):
        with open(file, 'r', encoding='utf-8') as r:
            reader = csv.DictReader(r)
            for row in reader:
                for key in keys:
                    if(row[key]!=phong):
                        data[key].append(row[key])
    else:
        print(f'{erF}File {file} không tồn tại!{RESETs}')
    return data

# def menu1(file_Phong):
#     # Load room data
#     room_keys = ['Số phòng', 'Loại', 'Giá', 'Trạng thái']
#     room_data = load_data(file_Phong, room_keys)
    
#     print("Nhập thông tin của phòng muốn thêm:")
#     so_phong = input("Số phòng: ")
#     loai_phong = input("Loại phòng: ")
#     gia_thue = input("Giá thuê: ")
#     tinh_trang = input("Tình trạng: ")

#     if so_phong in room_data['Số phòng']:
#         print("Phòng bạn nhập đã có vui lòng nhập lại thông tin phòng cần thêm!")
#         return menu1(file_Phong)
#     else:
          
#                 # room_data['Số phòng'].insert() .append(so_phong)
#                 # room_data['Loại'].append(loai_phong)
#                 # room_data['Giá'].append(gia_thue)
#                 # room_data['Trạng thái'].append(tinh_trang)
#                 save_data('Phong.csv', room_data)
#                 print("Đã thêm thông tin phòng thành công!")
#                 del room_data
def menu1(file_phong):
    so=[]
    loai=[]
    gia=[]
    status=[]
    if check(file_phong):
        with open(file_phong,'r', encoding='utf-8')as r:
            render=csv.DictReader(r)
            for row in render:
                so.append(row['Số phòng'])
                loai.append(row['Loại'])
                gia.append(row['Giá'])
                status.append(row['Trạng thái'])
        print(colorF,"Nhập thông tin của phòng muốn thêm:")
        phong=input(f'{colorF+colorB}Số phòng:')
        pl=input(f'{colorF+colorB}Loại phòng:')
        money=input(f'{colorF+colorB}Giá thuê:')
        # tt=input("Tình trạng: ")
        tt="No"
        for i in range(len(so)):
            if so[i]==phong:
                print(erF,"Phòng bạn nhập đã có vui lòng nhập lại thông tin phòng cần thêm!",)
                return menu1(file_phong)
                
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
        with open(file_phong,'w',encoding='utf-8', newline='') as f:
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
            print(colorF,"Đã thêm thông tin phòng thành công!")
    else:
        print('File khong ton tai!')
    del so,loai,gia,status

def menu2(file_Phong):
    # Load room data
    room_keys = ['Số phòng', 'Loại', 'Giá', 'Trạng thái']
    room_data = load_data(file_Phong, room_keys)
    
    so_phong = input("Nhập số phòng bạn cần thay đổi: ")
    if so_phong in room_data['Số phòng']:
        index = room_data['Số phòng'].index(so_phong)
        room_data['Loại'][index]=input(f'Nhập loại phòng mới: ')
        room_data['Giá'][index]=input(f'Nhập Giá mới: ')
        room_data['Trạng thái'][index] = input(f"Nhập trạng thái mới của phòng {so_phong}: ")
        save_data(file_Phong, room_data)
        print(colorF,"Đã thay đổi trạng thái phòng thành công!")
        del room_data
    else:
        print(erF,"Số phòng bạn nhập không tồn tại, hãy nhập lại!",RESETs)
        menu2(file_Phong)

def menu5(file_Phong):
        # Load room data
    room_keys = ['Số phòng', 'Loại', 'Giá', 'Trạng thái']
    room_data = load_data(file_Phong, room_keys)
    print(room_data)
    print(f'{colorF}Số phòng\t Loại\t  Giá\t Trạng thái{RESETs}')
    
    for i in range(len(room_data['Số phòng'])):
        phong=room_data['Trạng thái'][i].upper()
        if room_data['Trạng thái'][i].upper().strip() == "NO":
            print(f"{room_data['Số phòng'][i]}\t\t{room_data['Loại'][i]}\t{room_data['Giá'][i]}\t{room_data['Trạng thái'][i].upper()}")
    del room_data
        
def menu7(file_KhachHang):
        # Load customer data
    customer_keys = ['SoPhong', 'TenKhach', 'Sdt', 'GiayTo', 'NgayDat', 'NgayDen', 'NgayDi', 'StatusCheck']
    customer_data = load_data(file_KhachHang, customer_keys)

    print(colorF,"Số phòng\tTên Khách\tSĐT\tGiấy tờ",RESETs)
    for i in range(len(customer_data['SoPhong'])):
        print(f"{customer_data['SoPhong'][i]}\t{customer_data['TenKhach'][i]}\t{customer_data['Sdt'][i]}\t{customer_data['GiayTo'][i]}")
    del customer_data
        
def menu9(file_KhachHang):
    # Load booking data
    booking_keys = ['SoPhong', 'TenKhach', 'Sdt', 'GiayTo' , 'NgayDat', 'NgayDen', 'NgayDi', 'StatusCheck']
    booking_data = load_data(file_KhachHang, booking_keys)
    phong=input(f'{erF}Số phòng muốn hủy:')
    if phong in booking_data['SoPhong']:
        index= booking_data['SoPhong'].index(phong)
        
        data=load_data_khach_hang(file_KhachHang,booking_keys,phong)
        save_data(file_KhachHang,data)
        print(erB,'Đã hủy phòng thành công!',RESETs)
    else:
        print(erF,"Số phòng chưa có ai đặt!",RESETs)
    del booking_data
def menu14(file_NhanVien):
        # Load employee data
    employee_keys = ['MaNv', 'HoTen', 'ChucVu', 'Sdt', 'NgayThamGia']
    employee_data = load_data(file_NhanVien, employee_keys)

    ma_nv = input(f'{colorF}Nhập mã nhân viên cần thay đổi: ')
    if ma_nv in employee_data['MaNv']:
        index = employee_data['MaNv'].index(ma_nv)
        print("Nhập thông tin nhân viên cần thay đổi:")
        employee_data['HoTen'][index] = input("Họ tên: ")
        employee_data['ChucVu'][index] = input("Chức vụ: ")
        employee_data['Sdt'][index] = input("Số điện thoại: ")
        employee_data['NgayThamGia'][index] = input("Ngày tham gia: ")
        save_data(file_NhanVien, employee_data)
        print("Đã thay đổi thông tin nhân viên thành công!",RESETs)
        del employee_data
    else:
        print("Mã nhân viên bạn nhập không tồn tại, vui lòng nhập lại!")
        return menu14(file_NhanVien)
