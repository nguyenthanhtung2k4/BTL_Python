import math
from datetime import datetime #Lấy date
import csv
from pystyle import System
# vuong:  11,3,10,6,17

# 11.Trả phòng: Xác nhận khách đã trả phòng, tính toán số tiền cần thanh toán.
def menu11(fileRoom,fileVisitors):
    System.Clear()
    CheckStatus = True
    # Check phòng đã nhận phòng hay chưa
    Number = []
    Name =[]
    PhoneNumber=[]
    Info=[]
    DateTakeRoom =[]
    DateCheckIn=[]
    DateCheckOut=[]
    Status_Visitors=[]

    cost =[]
    sum =0
    Number_room =[]
    Status=[]
    print("Nhap so phong ban muon check out: " )
    RoomNumber = int(input())
    with open(fileVisitors,'r', encoding='utf-8') as File:
        ReadF = csv.DictReader(File)
        for row in ReadF:
            Number_Room = int(row['SoPhong'])
            Name_Visitor = str(row['TenKhach'])
            Phone_Visitor = int(row['Sdt'])
            Info_Visitor = str(row['GiayTo'])
            DateTake_Room = datetime.strptime(row['NgayDat'], '%Y-%m-%d')
            DateCheck_In = datetime.strptime(row['NgayDen'], '%Y-%m-%d')
            DateCheck_Out = datetime.strptime(row['NgayDi'], '%Y-%m-%d')
            Status_room = str(row['StatusCheck'])
            
            Number.append(Number_Room) #Lay so phong file khachang
            Name.append(Name_Visitor)
            PhoneNumber.append(Phone_Visitor)
            Info.append(Info_Visitor)
            DateTakeRoom.append(DateTake_Room)
            DateCheckIn.append(DateCheck_In)
            DateCheckOut.append(DateCheck_Out)
            Status_Visitors.append(Status_room)
        with open(fileRoom,'r',encoding='utf-8') as f:
            ReadF = csv.DictReader(f)
            for row in ReadF:
                Cost = row['Giá']
                cost.append(Cost)
                Number_room .append(row['Số phòng']) #Lay so phong trong file phong
        for i in range(0,len(Number),1):
            if(RoomNumber == int(Number[i])):
                # print(True)
                if(int(Number[i]) == int(Number_room[i])): #Kiểm tra điều kiện và nhớ chuyển dữ liệu thành int 
                    # print (True)
                        if(Status_Visitors[i] != "Yes"):
                            print(f"Phòng {RoomNumber} đã có khách trả phòng, vui lòng chuyển đến phòng khác.")
                            return
                        else:
                            day = DateCheckOut[i] - DateCheckIn[i] #Tính số ngày trả phòng
                            sum = day.days * int(cost[i]) #Lay so ngay nhan voi cost
                            print(f"Phòng {RoomNumber} đã trả phòng. Số tiền cần thanh toán là: {sum} $")
                            Status_Visitors[i] = "No"
                            CheckStatus = False
                            break
                else:
                    print(f"Phòng {RoomNumber} không tồn tại.")
                    # print(False)
                    return
    with open(fileVisitors,'w',encoding='utf-8') as f:
        WriteF = csv.DictWriter(f,fieldnames=['SoPhong','TenKhach','Sdt','GiayTo','NgayDat','NgayDen','NgayDi','StatusCheck'])
        WriteF.writeheader()
        for i in range(len(Number)):
            obj={
                'SoPhong':Number[i],
                'TenKhach':Name[i],
                'Sdt':PhoneNumber[i],
                'GiayTo':Info[i],
                'NgayDat':DateTakeRoom[i].strftime('%Y-%m-%d'),
                'NgayDen':DateCheckIn[i].strftime('%Y-%m-%d'),
                'NgayDi':DateCheckOut[i].strftime('%Y-%m-%d'),
                'StatusCheck':Status_Visitors[i]
            }
            WriteF.writerow(obj)

#3 Xóa phòng: Xóa thông tin một phòng khỏi hệ thống.
def menu3(fileRoom):
    System.Clear()
    NumberDel = int(input("Nhap So phong ban can xoa: "))
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
            print(f"Phòng {NumberDel} đã bị xóa.")
            CheckDelete = True
            break
        else:
            CheckDelete = False
            continue
    if(CheckDelete == False):
        print(f"Phòng {NumberDel} không tồn tại.")

    with open(fileRoom,'w',encoding='utf-8') as FileWrite:
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
        


#10 Nhận phòng : Xác nhận khách đã nhận phòng.
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
            # print (Date, DateCheckIn,DateCheckOut)
    with open(fileVisitors, 'w', newline='', encoding='utf-8') as File:
        format = ['SoPhong', 'TenKhach', 'Sdt', 'GiayTo', 'NgayDat', 'NgayDen', 'NgayDi', 'StatusCheck']
        Writer = csv.DictWriter(File, fieldnames=format)
        Writer.writeheader()  # Ghi tiêu đề một lần
        
        for i in range(len(DateCheckIn)):
            if CheckDate(TakeDate, DateCheckIn[i], DateCheckOut[i]):
                objVisitors = {
                    'SoPhong': Number[i],
                    'TenKhach': NameVisitors[i],
                    'Sdt': PhoneNumber[i],
                    'GiayTo': Info[i],
                    'NgayDat': CheckOrder[i].date(),
                    'NgayDen': DateCheckIn[i].date(),
                    'NgayDi': DateCheckOut[i].date(),
                    'StatusCheck': 'Yes'
                }
            else:
                objVisitors = {
                    'SoPhong': Number[i],
                    'TenKhach': NameVisitors[i],
                    'Sdt': PhoneNumber[i],
                    'GiayTo': Info[i],
                    'NgayDat': CheckOrder[i],
                    'NgayDen': DateCheckIn[i],
                    'NgayDi': DateCheckOut[i],
                    'StatusCheck': 'No'
                }
            Writer.writerow(objVisitors)  # Ghi dữ liệu từng dòng

#6.Sửa thông tin khách hàng: Cập nhật thông tin của một khách hàng đã tồn tại.
def menu6(fileVisitors,fileRoom):
    System.Clear()
    NameVisitors = str(input("Nhap ten khach hang muon cap nhat: "))
    Number=[]
    NameVisitorsCheck=[]
    PhoneNumber=[]
    Info=[]
    DateTakeRoom=[]
    DateCheckIn=[]
    DateCheckOut=[]
    DateTake = datetime.now()
    status = ''
    Updated = False
    # print(len(fileVisitors)) #13
    with open(fileVisitors,'r',encoding='utf-8') as File:
        Reader = csv.DictReader(File)
        for i in Reader:
            Number.append(i['SoPhong'])
            NameVisitorsCheck.append(i['TenKhach'])
            PhoneNumber.append(i['Sdt'])
            Info.append(i['GiayTo'])
            DateTakeRoom.append(i['NgayDat'])
            DateCheckIn.append(i['NgayDen'])
            DateCheckOut.append(i['NgayDi'])
    with open(fileVisitors,'w',encoding='utf-8') as FileWrite:
        format=['SoPhong','TenKhach','Sdt','GiayTo','NgayDat','NgayDen','NgayDi','StatusCheck']
        Writer=csv.DictWriter(FileWrite,fieldnames=format)
        Writer.writeheader()
        for i in range(0,len(Number),1):
            if(NameVisitors == NameVisitorsCheck[i]):
                print("Nhap thong tin can cap nhat: ")
                NameVisitorsCheck[i] = str(input("Ten: "))
                PhoneNumber[i] = str(input("So dien thoai: "))
                Info[i] = str(input("Giay to: "))
                DateTakeRoom[i] = str(input("Nhap ngay dat moi: "))
                DateCheckIn[i] = str(input("Nhap ngay den: "))
                DateCheckOut[i] = str(input("Nhap ngay di: "))
                DateTakeRoom[i] =  datetime.strptime(DateTakeRoom[i],'%Y-%m-%d').strftime('%Y-%m-%d') # Chuyen ve dang date de check status và đưa về dạng Y/M/D
                DateCheckIn[i] = datetime.strptime(DateCheckIn[i],'%Y-%m-%d').strftime('%Y-%m-%d')
                DateCheckOut[i] = datetime.strptime(DateCheckOut[i],'%Y-%m-%d').strftime('%Y-%m-%d')
                if(CheckDate(DateTake,DateCheckIn[i],DateCheckOut[i])):
                    status = 'Yes'
                else:
                    status = 'No'
                objUser={
                    'SoPhong': Number[i],
                    'TenKhach': NameVisitorsCheck[i],
                    'Sdt': PhoneNumber[i],
                    'GiayTo': Info[i],
                    'NgayDat': DateTakeRoom[i],
                    'NgayDen': DateCheckIn[i],
                    'NgayDi': DateCheckOut[i],
                    'StatusCheck': status
                }
                Updated = True
            else:
                if(CheckDate(DateTake,DateCheckIn[i],DateCheckOut[i])):
                    status = 'Yes'
                else:
                    status = 'No'
                objUser={
                    'SoPhong': Number[i],
                    'TenKhach': NameVisitorsCheck[i],
                    'Sdt': PhoneNumber[i],
                    'GiayTo': Info[i],
                    'NgayDat': DateTakeRoom[i],
                    'NgayDen': DateCheckIn[i],
                    'NgayDi': DateCheckOut[i],
                    'StatusCheck': status #Giả sử cho Status bằng yes
                }
            Writer.writerow(objUser)
# 17 Xem báo cáo doanh thu. Hiển thị báo cáo doanh thu chi tiết.
def menu17(fileRoom,fileVisitors):
    System.Clear()
    Number=[]
    Type=[]
    Cost=[]
    TakeDate = datetime.now()

    Number_RoomVisitors =[]
    Name=[]
    PhoneNumber=[]
    Info=[]
    DateCheckIn=[]
    DateCheckOut=[]
    Status =[]
    DateTake = datetime.now()
    with open(fileRoom,'r',encoding='utf-8') as File:
        Reader = csv.DictReader(File)
        for i in Reader:
            Number.append(i['Số phòng'])
            Type.append(i['Loại'])
            Cost.append(i['Giá'])
    with open(fileVisitors,'r',encoding='utf-8') as File:
        Reader = csv.DictReader(File)
        for i in Reader:
            Number_RoomVisitors.append(i['Số phòng'])
            Name.append(i['TenKhach'])
            PhoneNumber.append(i['Sdt'])
            Info.append(i['GiayTo'])
            DateCheckIn.append(i['NgayDen'])
            DateCheckOut.append(i['NgayDi'])
            Status.append(i['StatusCheck'])
        with open (fileRoom, 'w', encoding='utf-8') as file:
            format =['Số phòng','Loại','Giá','Trạng thái']
            writer = csv.DictWriter (file, fieldnames=format)
            writer.writeheader()
            for i in range(len(Number)):
                if (Number[i] in Number_RoomVisitors and Status[i] == 'Yes' ):
                    objRoom = {
                        'Số phòng': Number[i],
                        'Loại': Type[i],
                        'Giá': Cost[i],
                        'Trạng thái': 'Yes'
                    }
                else:
                    objRoom = {
                        'Số phòng': Number[i],
                        'Loại': Type[i],
                        'Giá': Cost[i],
                        'Trạng thái': 'No'
                    }
                writer.writerow(objRoom) #Cập nhật trạng thái của Phong.csv
    print(f'Doanh Thu la: {Income(fileRoom)}$')
def Income(fileRoom):
    Cost = []
    Return = 0
    with open(fileRoom,'r',encoding='utf-8') as File:
        Reader = csv.DictReader(File)
        for i in Reader:
            if i['Trạng thái'] == 'Yes':
                Cost.append(i['Giá'])
        for i in Cost:
            Return += int(i)
        return Return


def Main():
    fileRoom = 'Phong.csv'
    fileVisitors = 'KhachHang.csv'
    # menu11(fileRoom,fileVisitors)
    # Menu3(fileRoom)
    # Menu10(fileVisitors)
    # Menu6(fileVisitors,fileRoom)
    # Menu17(fileRoom,fileVisitors)
    print('Chương trình đã hoàn thành. Nên mở cmt để chạy test, Kiểm tra các fieldName có đồng nhất với file hay không trước khi test')
# Main()
