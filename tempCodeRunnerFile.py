 if phong in dataPhong['Số phòng']:
            phong= int(phong);
            indexPhong=dataPhong['Số phòng'].index();
            print(indexPhong)
            dataPhong['Trạng thái'][indexPhong]="NO";
            print(erB,'Đã hủy phòng thành công!',RESETs)