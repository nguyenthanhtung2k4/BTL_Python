import math
from datetime import datetime #Lấy date
import csv
# vuong:  11,3,10,6,17

# 11.Trả phòng: Xác nhận khách đã trả phòng, tính toán số tiền cần thanh toán.
def CheckOut(fileRoom,fileVisitors):
    with open(fileVisitors,'r', encoding='utf-8') as File:
        RoomArr =[]
        CostArr = []
        with open(fileRoom,'r',newline='',encoding='utf-8') as FileRoom:
            Check = csv.DictReader(FileRoom)
            # next(Check)
            for row in Check:
                Cost = row['Giá']
                Number_Room = row['Số phòng']
                RoomArr.append(Number_Room)
                CostArr.append(Cost)

        reader = csv.DictReader(File)
        # next(reader)
        # print(f'SoPhong\t TenKhach\t Sdt\t GiayTo\t NgayDat\t NgayDen\t NgayDi') Không in được do sẽ gây lệch các cột
        i=0
        sum=0
        for row in reader:
            NumberRoom = row['SoPhong']
            NameVisitors = row['TenKhach']
            PhoneNumber = row['Sdt']
            info = row['GiayTo']
            DateTake = row['NgayDat']
            DateCheckIn = row['NgayDen']
            DateCheckOut = row['NgayDi']
            if(RoomArr[i] == NumberRoom):
                date_Format = '%Y-%m-%d'
                CostTrans = float(CostArr[i])

                Date_Check_In = datetime.strptime(DateCheckIn,date_Format)
                Date_Check_Out = datetime.strptime(DateCheckOut,date_Format)
                Days = (Date_Check_Out-Date_Check_In).days #Lấy ngày của thời gian (2024-26-9) Chẳng hạn là như này

                sum+= Days*CostTrans
                i+=1
                print(f'So Phong: {NumberRoom}\t Ten khach: {NameVisitors}\t SDT: {PhoneNumber}\t Giay To: {info}\t Ngay dat phong: {DateTake}\t Ngay Den: {DateCheckIn}\t Ngay di: {DateCheckOut}')
                #Tôi in như này để nó tiện lợi hơn và không bị tình trạng lệch các cột
                print(f'So tien phai tra sau {Days} ngay la : {sum}$')


def DeleteRoom(NumberDel,fileRoom):
    Number=[]
    cost=[]
    TypeRoom=[]
    status=[]
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
                
        for i in range(0,len(Number),1):
            print(Number[i])


def Main():
    fileRoom = 'Phong.csv'
    fileVisitors = 'KhachHang.csv'
    # CheckOut(fileRoom, fileVisitors)
    DeleteRoom(101,fileRoom)
Main();

#3 Xóa phòng: Xóa thông tin một phòng khỏi hệ thống.
