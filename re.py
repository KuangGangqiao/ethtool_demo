import re
#f=open('log.txt','r', encoding='UTF-8')
#f1=open('result.txt','w')
#
#for line in f.readlines():
#    ss = line.split('|||')
#    s = ss[0].strip()
#    if((re.search("speed",s) or re.match("speed",s))and len(s) > 4 and (not re.search("off",s)) ):
#        f1.write(line)
#        print(line)
#f.close()
#f1.close()


def test():
    f=open('log.txt','r', encoding='UTF-8')
    for line in f.readlines():
        print(line)

def main():
    test()


if __name__ == "__main__":
    main()
