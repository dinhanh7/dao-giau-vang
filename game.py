while(1):
    check1=False
    print("""Chào mừng đến với Đảo giấu vàng.
Nhiệm vụ của bạn là tìm kho báu.
Bạn đang ở ngã ba đường. Bạn muốn đi đâu?
Nhập \"left\"(trái) hoặc \"right\"(phải)\n""")
    while check1==False:
        luaChon1=input()
        if luaChon1=="left" or luaChon1=="right":
            check1=True
        else:
            print("Bạn vừa nhập lựa chọn không thoả mãn, vui lòng nhập lại")
    if luaChon1=="right":
        print("Bạn đã rơi xuống bẫy. YOU LOSE!\n\n\n")
    else:
        print("""Bạn đang ở bờ sông. Bạn muốn đi đâu?
Nhập: \n\"swim\"(bơi qua sông)\n\"wait\"(chờ tàu)\n""")
        check2=False
        while check2==False:
            luaChon2=input()
            if luaChon2=="swim" or luaChon2=="wait":
                check2=True
            else:
                print("Bạn vừa nhập lựa chọn không thoả mãn, vui lòng nhập lại")
        if luaChon2=="swim":
            print("Bạn đã rơi xuống bẫy. YOU LOSE!\n\n\n")
        else:
            print("""Bạn đã qua sông thành công. Bạn chọn cửa nào?
Nhập: \n\"blue\"(cửa xanh)\n\"red\"(cửa đỏ)\n\"yellow\"\n""")
            check3=False
            while check3==False:
                luaChon3=input()
                if luaChon3=="blue" or luaChon3=="red" or luaChon3=="yellow" :
                    check3=True
                else:
                    print("Bạn vừa nhập lựa chọn không thoả mãn, vui lòng nhập lại")
            if luaChon3=="green":
                print("Bạn đã dính bẫy. YOU LOSE!\n\n\n")
            elif luaChon3=="red":
                print("Bạn đã dính bẫy. YOU LOSE!\n\n\n\n\n\n")
            else:
                print("CHÚC MỪNG BẠN ĐÃ TÌM ĐƯỢC KHO BÁU\n\n\n")
