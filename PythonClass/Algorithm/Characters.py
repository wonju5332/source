def isUniqChars(str):
    # 모든 문자는 ASCII코드로서, 256개의 문자가 있다고 가정한다.
    # 만일 문자가 256보다 크면, 그것은 중복일 것이다.
    if len(str) > 256:
        return False
    #boolean array 를 초기화한다.
    # 즉, 256개의 문자열이 있는 hash라는 배열의 모든 칸에 False로 초기화.
    hash = [False] + 256
    # input 받은 문자열을 순회하면서 회전한다.
    for ch in str:
        # 만일, hash배열에(boolean array)에 값이 들어갔으면 True를, 아니라면 False를 반환.
        if hash[ord(ch)] is True:  #값이 들어갔다는 것은 중복되지 않았다는 것이다. 첫째줄 if조건에 1단계 정제되었을 것
            return False
        # 만약, 값이 없다면, (false)라면 그 값은 중복되지 않았다는 것이다.
        else:
            hash[ord(ch)] = True
    return True


