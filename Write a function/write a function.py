def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True        
            else:
                leap = False
        else:
            leap = True     
    else:
        leap = False
                
    return leap

year = int(input())

# 🐻＜= は代入で ==は左右が同じであるということを示す演算子！
# 🐻＜True / Falseは文字列扱いしなくていい！
