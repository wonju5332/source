def gdc(small,big):
    temp = 0
    if small > big:   
        temp = small   #temp = 16
        small = big   #16 -> 24
        big = temp   #24 -> 16
        
   
    if big%small == 0:      ##0이라면, 바로 small값을 출력하고,
        return small
    gdc = big%small 
    while small > 0:      ##1번이상 더 나뉘어진다면,아래와 같이.
        wow = gdc
        gdc = small%gdc
        return wow

