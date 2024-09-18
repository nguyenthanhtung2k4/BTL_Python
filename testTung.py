import csv

file=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Phong.csv'
def vd(file):
     c=input("Nhap so phong can xoa: ")
     So=[]
     loai=[]
     gia=[]
     tt=[]
     dem=0
     with open(file,'r', encoding='utf-8')as r:
               render=csv.DictReader(r)
               for row in render:
                    if row['Số phòng']!=c:
                         So.append(row['Số phòng'])
                         loai.append(row['Loại'])
                         gia.append(row['Giá'])
                         tt.append(row['Trạng thái'])
                    else:
                         dem=1
     if dem==0:
          print("So phong ban nhap khong ton tai, moi nhap lai!")
          return vd(file)
     else:
          print(So)
          # with open(file,'w', encoding='utf-8')as w:
          #      format=['Số phòng','Loại','Giá','Trạng thái']
          #      wite=csv.DictWriter(w,fieldnames=format)
          #      wite.writeheader()
          #      for i in range(len(So)):
          #           ob={
          #                'Số phòng':So[i],
          #                'Loại':loai[i],
          #                'Giá':gia[i],
          #                'Trạng thái':tt[i]
          #           }
          #           wite.writerow(ob)
               
vd(file)           
     
          