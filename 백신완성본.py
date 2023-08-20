import hashlib
import os
import sys

VirusDB = []

def dec(file_fath):
    # 암호화된 파일 읽기
    with open(file_fath, "rb") as file_in:
        encrypted_data = file_in.read()

    # 데이터 복호화
    decrypted_data = cipher.decrypt(encrypted_data)

    # 복호화된 데이터를 파일로 저장
    with open("C:/Users/82104/Desktop/virus.db.txt.dec", "wb") as file_out:
      file_out.write(decrypted_data)

def LoadVirusDB(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    VirusDB = data.split(',') # 쉼표(,)를 기준으로 문자열 분리하여 리스트에 저장
    return VirusDB

VirusDB = LoadVirusDB('C:/Users/82104/Desktop/virus.db.txt')

vdb = [] # 가공된 악성코드 DB가 저장된다
vs = []

def MakeVirusDB():
    for i in VirusDB:
        t = []
        v = i.split(':') # 세미콜론을 기준으로 자른다
        t.append(v[0]) # MD5 해시를 저장한다
        t.append(v[1]) # 악성코드 이름을 저장한다
        vs.append(v[2]) # 악성파일 사이즈를 저장
        vdb.append(t) # 최종 vdb에 저장한다

def SearchVDB(fmd5):
    for i in range(0, len(vdb)):
        if vdb[i][0] == fmd5 : # MD5 해시가 같은지 비교
            print("악성코드 탐지")
            return True, vdb[i][1] # 악성코드 이름을 리턴

    print("악성코드 발견 X")
    return '', '' # 악성코드가 발견되지 않음

def vsize(size):
    for i in range(0, len(vdb)):
          if int(vs[i]) == int(size):
            print("악성코드일 확률 존재")
            return True

if __name__ == '__main__': # 메인함수의 선언 및 시작을 의미한다고 이해하고 넘어가자
    while(True):
        MakeVirusDB() # 악성코드 DB를 가공한다
        print("조사할 악성파일 주소를 입력하시오: ")
        fname = input()
        #fname = 'C:/Users/82104/Desktop/dummy.txt' # 악성코드 검사 대상 파일
        size = os.path.getsize(fname)
        result = vsize(size)
    
        if result:
            print("검사 중입니다 ▶ ▶ ▶")
            fp = open(fname, 'rb') # 바이너리 모드로 읽기
            buf = fp.read()
            fp.close()

            m = hashlib.md5()
            m.update(buf)
            fmd5 = m.hexdigest()

            ret, vname = SearchVDB(fmd5) # 악성코드를 검사한다

            if ret == True:
                print('%s : %s' % (fname, vname)) 
                os.remove(fname) #파일을 삭제해서 치료
                print("또 다른 파일을 조사하실 건가요?: (y/n)")
                a = input()
                print('\n')
                if a != 'y':
                    break
            else:
                print('%s : ok' % (fname))
                print("또 다른 파일을 조사하실 건가요?: (y/n)")
                a = input()
                print('\n')
                if a != 'y':
                    break