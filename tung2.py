import csv

# Hàm load dữ liệu từ file CSV
def load_data(file_name, keys):
    data = {key: [] for key in keys}
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key in keys:
                data[key].append(row[key])
    return data

# Hàm lưu dữ liệu vào file CSV
def save_data(file_name, data):
    keys = list(data.keys())
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        for i in range(len(data[keys[0]])):
            row = {key: data[key][i] for key in keys}
            writer.writerow(row)

# Hàm menu2 chỉnh sửa dữ liệu phòng
def menu2(file_Phong):
    # Load room data
    room_keys = ['Số phòng', 'Loại', 'Giá', 'Trạng thái']
    room_data = load_data(file_Phong, room_keys)
    
    so_phong = input("Nhập số phòng bạn cần thay đổi: ")
    if so_phong in room_data['Số phòng']:
        index = room_data['Số phòng'].index(so_phong)
        room_data['Loại'][index] = input('Nhập loại phòng mới: ')
        room_data['Giá'][index] = input('Nhập Giá mới: ')
        room_data['Trạng thái'][index] = input(f"Nhập trạng thái mới của phòng {so_phong}: ")
        
        save_data(file_Phong, room_data)
        print("Đã thay đổi trạng thái phòng thành công!")
    else:
        print("Số phòng bạn nhập không tồn tại, hãy nhập lại!")
        menu2(file_Phong)
