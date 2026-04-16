while True:
    idd = input("아이디 입력해라")
    psd = input("비번 빨리 입력해라")
    if idd == "admin" and psd == "1234":
        print("로그인 성공했으나, 게임은 그만합시다.")
        print("오늘부터 공부하면, 착한 어린이에요")
        break
    elif idd == "admin" and psd != "1234":
        print("비번이 틀렸으니, 게임 접으세요")
    elif idd != "admin" and psd == "1234":
        print("아이디 틀림, 아이디 찾아 와라")
    else:
        print("로그인 실패했으니, 게임 끊으세요.....")
        print("게임만 하면, 나쁜 어린이에요....")
