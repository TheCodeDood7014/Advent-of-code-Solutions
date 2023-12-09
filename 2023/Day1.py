import re, math
rep = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
finds = [str(i) for i in range(10)] + ["zero","one","two","three","four","five","six","seven","eight","nine"]
with open("in.txt","r") as f:
    c = f.read()
    content = c.split("\n")

def check(part):
    global content
    _sum = 0
    if part==1:
        for i in content:
            result = re.findall("[0-9]",i)
            print(result,result[0],result[-1])
            _sum += eval(result[0]+result[-1])
        return _sum
    elif part==2:
        result = {}
        for i in content:
            for n,f in enumerate(finds):
                search_result = [i.find(f),i.rfind(f)]
                if n>=10 and ((search_result[0]<result[n%10][0] and search_result[0]!=-1) or result[n%10][0]<0):
                    result[n%10][0] = search_result[0]
                elif n<=9:
                    result[n] = search_result
                    continue
                if n>=10 and ((search_result[1]>result[n%10][1] and search_result[1]!=-1) or result[n%10][1]<0):
                    result[n%10][1] = search_result[1]
                elif n<=9:
                    result[n] = search_result
                    continue
            min_index = max([i[1] for i in result.values()])
            min_val = -1
            max_index = 0
            max_val = -1
            for key, value in result.items():
                if value[0]<=min_index and value[0]!=-1:
                    min_index = value[0]
                    min_val = key
                if value[1]>=max_index and value[1]!=-1:
                    max_index = value[1]
                    max_val = key
            if min_val == -1:
                min_val = max_val
            if max_val == -1:
                max_val = min_val
            print(min_val,max_val)
            _sum += min_val*10+max_val
        return _sum
print("Part 1:", check())
content = c.split("\n")
print("Part 2:", check(2))