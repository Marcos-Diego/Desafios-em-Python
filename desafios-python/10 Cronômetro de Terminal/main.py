import time

seg = 0
min = 0
while True:
    time.sleep(1)
    
    seg += 1
    if seg // 60 == 1:
        seg -= seg
        #seg %= 60
        min += 1
    if min <= 9 and seg <= 9:
        print(f"\r0{min}:0{seg}", end = "")
    elif min <= 9:
        print(f"\r0{min}:{seg}", end = "")
    else:
        print(f"\r{min}:{seg}", end = "")
    #print(f"\r\r ola", end = "")