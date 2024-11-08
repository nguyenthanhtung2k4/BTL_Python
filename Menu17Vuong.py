import csv
import os

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
        print(f'File {file} không tồn tại!')
    return data

def save_data(file, data):
    keys = data.keys()
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for i in range(len(data[next(iter(keys))])):
            row = {key: data[key][i] for key in keys}
            writer.writerow(row)
    print(f"Đã lưu dữ liệu vào file {file} thành công!")

def menu17(file_phong, file_khach):
    phong_key = ['Số phòng', 'Loại', 'Giá', 'Trạng thái']
    data_phong = load_data(file_phong, phong_key)
    khach_key = ['SoPhong', 'TenKhach', 'Sdt', 'GiayTo', 'NgayDat', 'NgayDen', 'NgayDi', 'StatusCheck']
    data_khach = load_data(file_khach, khach_key)

    for i in range(len(data_phong['Số phòng'])):
        if data_phong['Số phòng'][i] in data_khach['SoPhong'] and data_khach['StatusCheck'][data_khach['SoPhong'].index(data_phong['Số phòng'][i])] == 'Yes':
            data_phong['Trạng thái'][i]= 'Yes'
            total_income = sum(float(data_phong['Giá'][i]) for i in range(len(data_phong['Số phòng'])) if data_phong['Trạng thái'][i] == 'Yes')
            
        else:
            data_phong['Trạng thái'][i] = 'No'

#     save_data(file_phong, data_phong)

#     total_income = sum(float(data_phong['Giá'][i]) for i in range(len(data_phong['Số phòng'])) if data_phong['Trạng thái'][i] == 'Yes')
    print(f'Doanh Thu là: {total_income}$')

menu17('Phong.csv', 'KhachHang.csv')
