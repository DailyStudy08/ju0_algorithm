def solution(hp):
    jang = hp // 5
    beong = (hp - jang * 5) // 3
    il = hp - hp // 5 * 5 - beong * 3
    answer = jang + beong + il
    return answer