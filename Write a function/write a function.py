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

# ð»ï¼= ã¯ä»£å¥ã§ ==ã¯å·¦å³ãåãã§ããã¨ãããã¨ãç¤ºãæ¼ç®å­ï¼
# ð»ï¼True / Falseã¯æå­åæ±ãããªãã¦ããï¼
