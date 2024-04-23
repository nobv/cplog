# https://app.codility.com/programmers/lessons/1-iterations/
def solution(N):
    b = format(N, "b")
    f = False
    res = []
    tmp = ""
    for s in b:
        f = s == "1"
        if f and tmp != "":
            res.append(tmp)
            tmp = ""
            continue
        if not f:
            tmp += s
    print(len(max(res)))
