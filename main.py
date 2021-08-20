import binascii


# coding = utf-8

def f(nx, x1, x):
    # n为待转换的十进制数，x为机制，取值为2-49
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', '-', '/', '!', '$', '&', '(', ')',
         ';', ':', '\'', '\"', ',', '.']
    nx = str(nx)
    b1 = list(nx)
    b2 = []
    for k in b1:
        for i1 in range(0, 49):
            if a[i1] == k:
                b2 = b2 + [i1]
    b2.reverse()
    # print(b2)
    n1 = 0
    n2 = 1
    for k in b2:
        n1 = n1 + int(k) * (pow(x1, n2 - 1))  # pow(x, n)，即计算 x 的 n 次幂函数
        n2 = n2 + 1
        # print (n1,n2)
    n = n1
    # print(n)
    b = []
    while True:
        s = n // x  # 商
        y = n % x  # 余数
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()  # reverse() 函数用于反向列表中元素,由个，十百转为百十个
    bd = ""
    for k in b:
        # print(a[k],end='')
        bd = bd + a[k]
    return bd


print('请输入模式序号 1:文件转十六进制文本 2：十六进制文本转文件 3:文件转五十进制文本 4:五十进制文本转文件')
Mode = int(input())
print('请输入源文件路径（不含文件名）')
L = input()
print('请输入源文件名（不含后缀）')
N = input()
print('请输入源文件后缀（例如.txt)')
H = input()
print('请输入目的文件后缀（例如.txt)')
HH = input()
File = open(L + '\\' + N + H, 'rb')

if Mode == 1:
    Text = str(File.read())
    Text_hex = Text.encode("utf8", "ignore").hex()
    FileHEX = open(L + '\\' + N + '_HEX' + HH, 'w')
    FileHEX.write(Text_hex)
    print('完成。目的文件 ' + L + '\\' + N + '_HEX' + HH)

if Mode == 2:
    Text = str(File.read())
    Text_raw = binascii.a2b_hex(Text).decode("utf8", "ignore")
    FileRAW = open(input(L + '\\' + N + '_RAW' + HH), 'w')
    FileRAW.write(Text_raw)
    print('完成。目的文件 ' + L + '\\' + N + '_RAW' + HH)

if Mode == 3:
    print('载入数据中')
    Text_INT = list(File.read())
    print('载入数据完成')
    INT2Fifty = {}
    Text_FiftyA = []
    Text_Fifty = []
    Text_Fif = ''
    i = 0
    le = len(Text_INT)
    print('初始化完成，共有' + str(le) + '字节数据')
    if le % 2:
        for i in range(le):
            for z in range(le):
                Text_FiftyA.append(0)
            z = 0
            if i % 2:
                A = hex(Text_INT[i])
                if len(hex(Text_INT[i])) != 4:
                    A = '0x0' + hex(Text_INT[i]).lstrip('0x')
                B = hex(Text_INT[i + 1])
                if len(hex(Text_INT[i + 1])) != 4:
                    B = '0x0' + hex(Text_INT[i + 1]).lstrip('0x')
                Text_FiftyA[i] = A + B.lstrip('0x')
                A = 0
                B = 0
            print('进度:' + str(round(i/le*100,2)) + '%' + '('+ str(i) + '/' + str(le) + ')')
        i = 0
        Text_FiftyA = [i for i in Text_FiftyA if i != '']
        Text_FiftyA[le] = Text_FiftyA[le] + '00'
        A = len(Text_FiftyA)
        for i in range(A):
            Text_Fifty[i] = f(str(int(Text_FiftyA[i], 16)), 10, 49)
            if len(Text_Fifty[i]) != 3:
                Text_Fifty[i] = '0' + Text_Fifty[i]
            if len(Text_Fifty[i]) != 3:
                Text_Fifty[i] = '0' + Text_Fifty[i]
            print('进度:' + str(round(i/le*100,2)) + '%' + '('+ str(i) + '/' + str(le) + ')')
        Text_Fifty[len(Text_FiftyA) + 1] = '??'
    else:
        for i in range(le):
            for z in range(le):
                Text_FiftyA.append(0)
            z = 0
            if i % 2:
                A = hex(Text_INT[i])
                if len(hex(Text_INT[i])) != 4:
                    A = '0x0' + hex(Text_INT[i]).lstrip('0x')
                B = hex(Text_INT[i + 1])
                if len(hex(Text_INT[i + 1])) != 4:
                    B = '0x0' + hex(Text_INT[i + 1]).lstrip('0x')
                Text_FiftyA[i] = A + B.lstrip('0x')
                A = 0
                B = 0
            print('进度:' + str(round(i/le*100,2)) + '%' + '('+ str(i) + '/' + str(le) + ')')
        i = 0
        Text_FiftyA = [i for i in Text_FiftyA if i != '']
        A = len(Text_FiftyA)
        for i in range(A):
            Text_Fif = Text_Fif + f(int(Text_FiftyA[i], 16), 10, 49)
            print('进度:' + str(round(i/le*100,2)) + '%' + '('+ str(i) + '/' + str(le) + ')')
    FileFif = open(L + '\\' + N + '_Fif' + HH, 'w')
    FileFif.write(Text_Fif)
    print('完成。目的文件 ' + L + '\\' + N + '_Fif' + HH)
