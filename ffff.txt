import re

# re.search it will match all string until find a matchs
def test1():
    f=open('log.txt','r', encoding='UTF-8')
    print("====search====")
    for line in f.readlines():
        support = re.search(r"Supported",line)
        if support != None:
            ss =support.group()
            print(ss)
        else:
            print("fail")
    f.close()


def test2():
    f=open('log.txt','r', encoding='UTF-8')
    print("====findall====")
    for line in f.readlines():
        support = re.findall(r"\s*\d+",line)# /[F|H]
        for i in support:
            print(i)
    f.close()

# re.match only match the start of string if match fail, the function will return None
def test3():
    f=open('log.txt','r', encoding='UTF-8')
    print("====match====")
    c = 0
    for line in f.readlines():
        support = re.match(r"\s*(\d+)", line)
        if support != None:
            print(support.group())
        else:
            print("fail")
    f.close()

def speed():
    f=open('log.txt','r', encoding='UTF-8')
    print("====speed====")
    for line in f.readlines():
        support = re.findall(r"Speed:\s*(\d+)", line);
        for i in support:
            print(i)
    f.close()

def full():
    f=open('log.txt','r', encoding='UTF-8')
    print("====Full====")
    for line in f.readlines():
        support = re.findall(r"Duplex:\s*(\w+)", line);
        for i in support:
            print(i)
    f.close()

def AN():
    f=open('log.txt','r', encoding='UTF-8')
    print("====autoneg====")
    for line in f.readlines():
        support = re.findall(r"Auto-negotiation:\s*(\w+)", line);
        for i in support:
            print(i)
    f.close()

def link():
    f=open('log.txt','r', encoding='UTF-8')
    print("====link flag====")
    for line in f.readlines():
        support = re.findall(r"Link detected:\s*(\w+)", line);
        for i in support:
            print(i)
    f.close()

def support():
    flag =""
    l =[]
    f=open('log.txt','r', encoding='UTF-8')
    print("====support====")
    for line in f.readlines():
        support = re.findall(r"(?<=Supported link modes:)\s*(.+)", line);
        if len(support):
            flag = "support"
        if flag == "support" and re.match(r"\s*(\d+)", line) != None:
            support = (re.findall("\s*(.+)", line))
        l = l + support
        if re.search(r"Supported pause frame use:", line) != None:
            print(l)
            break
    f.close()


def advertised():
    flag = ""
    l = []
    f=open('log.txt','r', encoding='UTF-8')
    print("====advertised====")
    for line in f.readlines():
        ad = re.findall(r"(?<=Advertised link modes:)\s*(.+)", line);
        if len(ad):
            flag = "advertised"
        if  flag == "advertised" and re.match(r"\s*(\d+)", line) != None:
            ad = (re.findall("\s*(.+)", line))
        l = l + ad
        if re.search(r"Advertised pause frame use:", line) != None:
            print(l)
            break
    f.close()

def lp_advertised():
    flag = ""
    l = []
    f=open('log.txt','r', encoding='UTF-8')
    print("====lp_advertised====")
    for line in f.readlines():
        lp_ad = re.findall(r"(?<=Link partner advertised link modes:)\s*(.+)", line);
        if len(lp_ad):
            flag = "lp_advertised"
        if flag == "lp_advertised" and re.match(r"\s*(\d+)", line) != None:
            lp_ad = (re.findall("\s*(.+)", line))
        l = l + lp_ad
        if re.search(r"Link partner advertised pause frame use:", line) != None:
            return l
    f.close()

def division_log(log_list: list):
    def do(i):
        s = i.split(" ")
        l= [x.strip() for x in s if x.strip() != ""]
        return l

    r = map(do, log_list)
    return list(r)


def test0():
    a = ["aaaa"]
    b = ["bbbb"]
    s = ["hello world"]
    s.extend(a)
    s.extend(b)
    print(s)
    for i in s:
        print(i)

def main():
    test1()
    test2()
    test3()
    speed()
    full()
    AN()
    link()
    support()
    advertised()
#    lp_advertised()
    print(division_log(lp_advertised()))
#    test0()

if __name__ == "__main__":
    main()
