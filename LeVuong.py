import csv
from datetime import datetime
from pystyle import System
from Setting import*
from Main import check_Date
#3 Xóa phòng: Xóa thông tin một phòng khỏi hệ thống.
def menu3(fileRoom):
    System.Clear()
    NumberDel = int(input(f'{colorF}Nhap So phong ban can xoa: '))
    Number=[]
    cost=[]
    TypeRoom=[]
    status=[]
    CheckDelete= False
    with open(fileRoom,'r',encoding='utf-8') as f:
        ReadF = csv.DictReader(f)
        for row in ReadF:
            Number_Room = row['Số phòng']
            # print(Number_Room)
            Numbertrans = int(Number_Room)
            Type = row['Loại']
            Cost = row['Giá']
            Status = row['Trạng thái']
            Number.append(Numbertrans)
            cost.append(Cost)
            TypeRoom.append(Type)
            status.append(Status)
    for i in range(len(Number)):
        if(NumberDel== Number[i]):
            # print(Number[i],cost[i],TypeRoom[i],status[i])
            del Number[i]
            del cost[i]
            del TypeRoom[i]
            del status[i]
            print(f'{colorF}Phòng {NumberDel} {erF}đã bị xóa.',RESETs)
            CheckDelete = True
            break
        else:
            CheckDelete = False
            continue
    if(CheckDelete == False):
        print(f"Phòng {NumberDel}{erB} không tồn tại.",RESETs)

    with open(fileRoom,'w',encoding='utf-8', newline='') as FileWrite:
        format=['Số phòng','Loại','Giá','Trạng thái']
        writer=csv.DictWriter(FileWrite,fieldnames=format) #Lưu thuộc tính vào FileWrite với fieldnames là mảng format
        writer.writeheader() #thuộc tính này nhằm để lưu lại các fieldnames ở trong file
        for i in range(0,len(Number),1):
            Num = Number[i]
            Type = TypeRoom[i]
            Cost = cost[i]
            Status = status[i]
            # Cho vào for vì là các mảng của dữ liệu, mỗi lần lặp sẽ lại lưu 1 thuộc tính mới
            writer.writerow({
                'Số phòng': Num,
                'Loại': Type,
                'Giá':Cost,
                'Trạng thái':Status
            }) #Lưu thành các cột
#  tra phong
def menu11(fileRoom, fileVisitors):
    # System.Clear()
    # Cac danh sach luu tru  file  Phong
    Room=[];Type=[];Cost=[];Status=[]
    # Các danh sách lưu trữ dữ liệu từ file Khach Hang
    Number = []
    Name = []
    PhoneNumber = []
    Info = []
    DateTakeRoom = []
    DateCheckIn = []
    DateCheckOut = []
    Status_Visitors = []
    #dicstion gia phong
    # room_costs = {}
    
    # Nhập số phòng muốn check out
    print(colorF,"Nhập số phòng bạn muốn check out: ")
    RoomNumber = int(input().strip())
    
    # Đọc dữ liệu từ file khách hàng
    with open(fileVisitors, 'r', encoding='utf-8') as File:
        ReadF = csv.DictReader(File)
        for row in ReadF:
            Number.append(int(row['SoPhong']))
            Name.append(row['TenKhach'])
            PhoneNumber.append(int(row['Sdt']))
            Info.append(row['GiayTo'])
            DateTakeRoom.append(datetime.strptime(row['NgayDat'], '%Y-%m-%d'))
            DateCheckIn.append(datetime.strptime(row['NgayDen'], '%Y-%m-%d'))
            DateCheckOut.append(datetime.strptime(row['NgayDi'], '%Y-%m-%d'))
            Status_Visitors.append(row['StatusCheck'])

    # Đọc giá phòng từ file Phong.csv và lưu vào dictionary với key là số phòng
    with open(fileRoom, 'r', encoding='utf-8') as f:
        ReadF = csv.DictReader(f)
        # for row in ReadF:
        #     room_number = int(row['Số phòng'])
        #     cost = int(row['Giá'])
        #     room_costs[room_number] = cost
        for row in  ReadF:
            Room.append(int(row['Số phòng']))
            Type.append(row['Loại'])
            Cost.append(int(row['Giá']))
            Status.append(row['Trạng thái'])
            
    # Kiểm tra phòng có tồn tại và đã được nhận chưa
    if RoomNumber not in Number:
        print(f"{RESETs}Phòng {RoomNumber} {erF}không tồn tại trong danh sách khách hàng.{RESETs}")
        return
    
    visitors_index = Number.index(RoomNumber) # index khach hang
    room_index=Room.index(RoomNumber) # index  phong
    if Status_Visitors[visitors_index] != "Yes":
        print(f"{erF}Phòng {RoomNumber} đã có khách đặt phòng trước \nVui lòng kiểm tra lại!{RESETs}")
        return

    # Tính số tiền cần thanh toán
    check_in_date = DateCheckIn[visitors_index]
    check_out_date = DateCheckOut[visitors_index]
    days_stayed = (check_out_date - check_in_date).days
    total_cost=days_stayed*Room[room_index]

    # Cập nhật trạng thái phòng
    print(f"{RESETs}Phòng {RoomNumber} đã trả phòng.\n{RESETs}Số tiền cần thanh toán là: {erB}{total_cost} ${RESETs}")
    # Cap  nhat lai  trang thai phong
    Status[room_index] = "No"
    with open(fileRoom, 'w', encoding='utf-8', newline='') as f:
        room_keys = ['Số phòng', 'Loại', 'Giá', 'Trạng thái']
        writeF=csv.DictWriter(f, fieldnames=room_keys)
        writeF.writeheader()
        for i in range(len(Room)):
                obj = {
                    'Số phòng': Room[i],
                    'Loại': Type[i],
                    'Giá': Cost[i],
                    'Trạng thái': Status[i]
                }
                writeF.writerow(obj)
    # Ghi lại dữ liệu vào file khách hàng sau khi cập nhật
    with open(fileVisitors, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['SoPhong', 'TenKhach', 'Sdt', 'GiayTo', 'NgayDat', 'NgayDen', 'NgayDi', 'StatusCheck']
        WriteF = csv.DictWriter(f, fieldnames=fieldnames)
        WriteF.writeheader()
        for i in range(len(Number)):
            if i != visitors_index:
                obj = {
                    'SoPhong': Number[i],
                    'TenKhach': Name[i],
                    'Sdt': PhoneNumber[i],
                    'GiayTo': Info[i],
                    'NgayDat': DateTakeRoom[i].strftime('%Y-%m-%d'),
                    'NgayDen': DateCheckIn[i].strftime('%Y-%m-%d'),
                    'NgayDi': DateCheckOut[i].strftime('%Y-%m-%d'),
                    'StatusCheck': Status_Visitors[i]
                }
                WriteF.writerow(obj)
    del Room,Type,Cost,Status,Number,Name,PhoneNumber,Info,DateTakeRoom,DateCheckIn,DateCheckOut,Status_Visitors,
# cap nhap  thong tin khach hang
def menu6(fileVisitors,fileRoom):
    System.Clear()
    
    InputNumber = str(input("Nhập số phòng cần cập nhật: "))
    Number = []
    NameVisitorsCheck = []
    PhoneNumber = []
    Info = []
    DateTakeRoom = []
    DateCheckIn = []
    DateCheckOut = []
    CheckStatus = []
    Updated = False

    # Đọc dữ liệu từ file
    with open(fileVisitors, 'r', encoding='utf-8') as File:
        Reader = csv.DictReader(File)
        for i in Reader:
            Number.append(i['SoPhong'])
            NameVisitorsCheck.append(i['TenKhach'])
            PhoneNumber.append(i['Sdt'])
            Info.append(i['GiayTo'])
            DateTakeRoom.append(i['NgayDat'])
            DateCheckIn.append(i['NgayDen'])
            DateCheckOut.append(i['NgayDi'])
            CheckStatus.append(i['StatusCheck'])

    # Ghi dữ liệu đã cập nhật vào file
    with open(fileVisitors, 'w', encoding='utf-8', newline='') as FileWrite:
        format = ['SoPhong', 'TenKhach', 'Sdt', 'GiayTo', 'NgayDat', 'NgayDen', 'NgayDi', 'StatusCheck']
        Writer = csv.DictWriter(FileWrite, fieldnames=format)
        Writer.writeheader()

        for i in range(len(Number)):
            if InputNumber == Number[i]:
                print("Nhập thông tin cần cập nhật: ")
                NameVisitorsCheck[i] = str(input("Tên: "))
                PhoneNumber[i] = str(input("Số điện thoại: "))
                Info[i] = str(input("Giấy tờ: "))

                DateTakeRoom[i] = check_Date("Nhập ngày đặt mới (yyyy-mm-dd): ")
                DateCheckIn[i] = check_Date("Nhập ngày đến đến (yyyy-mm-dd): ")
                DateCheckOut[i] = check_Date("Nhập ngày đi đi (yyyy-mm-dd): ")

                # Kiểm tra tính hợp lệ của ngày
                if CheckDate(DateTakeRoom[i], DateCheckIn[i], DateCheckOut[i]):
                    status = 'Yes'
                    CheckStatus[i] = status
                    Updated = True
                    print("Thông tin của khách hàng đã được cập nhật thành công!")
                else:
                    print("Ngày không hợp lệ!")
                    status = 'No'
                    CheckStatus[i] = status

                objUser = {
                    'SoPhong': Number[i],
                    'TenKhach': NameVisitorsCheck[i],
                    'Sdt': PhoneNumber[i],
                    'GiayTo': Info[i],
                    'NgayDat': DateTakeRoom[i],
                    'NgayDen': DateCheckIn[i],
                    'NgayDi': DateCheckOut[i],
                    'StatusCheck': CheckStatus[i]
                }
                Writer.writerow(objUser)
                break
            else:
                objUser = {
                    'SoPhong': Number[i],
                    'TenKhach': NameVisitorsCheck[i],
                    'Sdt': PhoneNumber[i],
                    'GiayTo': Info[i],
                    'NgayDat': DateTakeRoom[i],
                    'NgayDen': DateCheckIn[i],
                    'NgayDi': DateCheckOut[i],
                    'StatusCheck': CheckStatus[i]
                }
                Writer.writerow(objUser)

        if not Updated:
            print("Không tìm thấy khách hàng nào trong danh sách.")
    del Number,NameVisitorsCheck,PhoneNumber,Info,DateTakeRoom,DateCheckIn,DateCheckOut,
#  khach nhan phong
def CheckDate(Date_To_Check,Start_Date,End_Date):
    # Kiểm tra nếu ngày nằm trong khoảng giữa start_date và end_date
    if (Start_Date <= Date_To_Check <= End_Date):
        return True
    else:
        return False
def menu10(fileVisitors):
    System.Clear()
    Number=[]
    NameVisitors=[]
    PhoneNumber=[]
    Info=[]
    CheckOrder=[]
    DateCheckIn=[]
    DateCheckOut=[]
    Status=[]
    TakeDate = 0
    with open(fileVisitors,'r',encoding='utf-8') as File:
        Check = csv.DictReader(File)
        dateFormat = '%Y-%m-%d'
        for row in Check:
            # print(row)
            Number.append(row['SoPhong'])
            NameVisitors.append(row['TenKhach'])
            PhoneNumber.append(row['Sdt'])
            Info.append(row['GiayTo'])
            TakeDateCheckIn = datetime.strptime(row['NgayDen'],dateFormat)
            DateCheckIn.append(TakeDateCheckIn)
            TakeDateCheckOut = datetime.strptime(row['NgayDi'],dateFormat)
            DateCheckOut.append(TakeDateCheckOut)
            TakeDate = datetime.now()
            TakeCheckOrder = datetime.strptime(row['NgayDat'],dateFormat)
            CheckOrder.append(TakeCheckOrder)
            Status.append(row['StatusCheck'])
    #  kiem tra phong khach hang.
    room_number=input("Số phòng nhận: ")
    room_number=room_number.strip()
    try:
        room_index=Number.index(room_number)
        if (Status[room_index].upper() != 'NO'):
            print("Phòng đã được nhận")
            return
    except ValueError:
        print(erF,"Số phòng không tồn tại",RESETs)
        return
    #  Cap nhap  lai  status nhan phong
    Status[room_index]="Yes"
    # Ghi lại dữ liệu vào file sau khi cập nhật trạng thái
    with open(fileVisitors, 'w', newline='', encoding='utf-8') as File:
        format = ['SoPhong', 'TenKhach', 'Sdt', 'GiayTo', 'NgayDat', 'NgayDen', 'NgayDi', 'StatusCheck']
        Writer = csv.DictWriter(File, fieldnames=format)
        Writer.writeheader()

        # Ghi dữ liệu từng dòng
        for i in range(len(Number)):
            objVisitors = {
                'SoPhong': Number[i],
                'TenKhach': NameVisitors[i],
                'Sdt': PhoneNumber[i],
                'GiayTo': Info[i],
                'NgayDat': CheckOrder[i].strftime(dateFormat),
                'NgayDen': DateCheckIn[i].strftime(dateFormat),
                'NgayDi': DateCheckOut[i].strftime(dateFormat),
                'StatusCheck': Status[i]
            }
            Writer.writerow(objVisitors)
    print(erB,"Phòng ",room_number," đã được nhận",RESETs)
    print(erF,"Chúc quý khách ",NameVisitors[room_index]," có một ngày tuyệt vời!")
    del  Number,NameVisitors,PhoneNumber,Info,CheckOrder,DateCheckIn,DateCheckOut,Status,
# Xem bao cao doanh thu 
def menu17(fileRoom,fileVisitors):
    System.Clear()
    cost_day={}
    Number_RoomVisitors =[]
    Name=[]
    PhoneNumber=[]
    Info=[]
    DateCheckIn=[]
    DateCheckOut=[]
    Status =[]
    with open(fileRoom,'r',encoding='utf-8') as File:
        Reader = csv.DictReader(File)
        for i in Reader:
            room_number=i['Số phòng']
            cost_day[room_number]=i['Giá']
    with open(fileVisitors,'r',encoding='utf-8') as File:
        Reader = csv.DictReader(File)
        for i in Reader:
            Number_RoomVisitors.append(i['SoPhong'])
            Name.append(i['TenKhach'])
            PhoneNumber.append(i['Sdt'])
            Info.append(i['GiayTo'])
            DateCheckIn.append(datetime.strptime(i['NgayDen'], '%Y-%m-%d'))
            DateCheckOut.append(datetime.strptime(i['NgayDi'], '%Y-%m-%d'))
            Status.append(i['StatusCheck'])
    # Tinh tong doanh thu
    totalCost,totalThu=0,0
    for i  in range(len(Number_RoomVisitors)):
        if Status[i].upper()=="YES":
            start_day=DateCheckIn[i]
            end_day=DateCheckOut[i]
            day = (end_day - start_day).days
            cost = day * int(cost_day[Number_RoomVisitors[i]])
            totalCost += cost 
            print("Phòng ",Number_RoomVisitors[i]," của ",Name[i]," đã thu ",cost," $")
        else:
            start_day=DateCheckIn[i]
            end_day=DateCheckOut[i]
            day = (end_day - start_day).days
            thu = day * int(cost_day[Number_RoomVisitors[i]])
            # print("Phòng ",Number_RoomVisitors[i]," của ",Name[i]," chưa thu ",thu,' $')
            totalThu+=thu
            totalCost+=thu
    print("\n\nĐã thu: ",totalCost-totalThu,' $')
    print("Chưa thu: ",totalThu," $")
    print(f"{erB}\tTổng doanh thu: ",RESETs,totalCost," $")
    del  Number_RoomVisitors ,Name,PhoneNumber,Info,DateCheckIn,DateCheckOut,Status ,
# if  __name__=='__main__':
# #//// data duong dan chuyen vao
#      file_phong=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Phong.csv'
#      file_Khach=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\KhachHang.csv'
#      file_NhanVien=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\NhanVien.csv'
#      file_Setting=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Setting.json'