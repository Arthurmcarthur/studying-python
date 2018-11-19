import re
def unicodepad(u_str):                          #読入字符串
    l_str = len(u_str)                          #読取字符串仧度
    for i in range(0, l_str):
        u_cha = ord(u_str[i])                   #読取Unicode編碼(十進制)
        pu_cha = re.match(r'0x(.+)', hex(u_cha)).group(1)  #爲簡潔用正則去掉前方的0x
        if len(pu_cha) <= 4:
            pu_cha = '0' * (4 - len(pu_cha)) + pu_cha
        if 13313 <= u_cha <= 19893:           #判斷Unicode編碼所在的區塊
            block_cha = 'Unicode CJK擴展A區'
        elif 19968<= u_cha <= 40943:
            block_cha = 'Unicode CJK基本區'
        elif 131072 <= u_cha <= 173782:
            block_cha = 'Unicode CJK擴展B區'
        elif 173824 <= u_cha <= 177972:
            block_cha = 'Unicode CJK擴展C區'
        elif 177984 <= u_cha <= 178205:
            block_cha = 'Unicode CJK擴展D區'
        elif 178208 <= u_cha <= 183969:
            block_cha = 'Unicode CJK擴展E區'
        elif 183984 <= u_cha <= 191456:
            block_cha = 'Unicode CJK擴展F區'
        else:
            block_cha = '不是漢字或是位於兼容區的漢字'
        try:
            g_cha = u_str[i].encode('GB2312')         #嘗試獲取字符的GB2312編碼
            pg_cha = (re.match(r'b\'\\x(.+?)\\x(.+)', str(g_cha)).group(1) + ' ' + re.match(r'b\'\\x(.+?)\\x(.+?)\'', str(g_cha)).group(2)).upper()
        except:
            g_cha = None
            pg_cha = '此字符不在GB/T 2312中。'
        try:
            b_cha = u_str[i].encode('BIG5')
            if str(b_cha).count('\\x') == 2:          #若無出現許蓋功問題則會出現兩次\x
                pb_cha = (re.match(r'b\'\\x(.+?)\\x(.+)', str(b_cha)).group(1) + ' ' + re.match(r'b\'\\x(.+?)\\x(.+?)\'', str(b_cha)).group(2)).upper()
            else:                                     #若出現許蓋功問題
                if str(b_cha)[-2] == 92:               #如果倒数第二箇字符是\
                    pb_cha = (re.match(r'b\'\\x(.+?)\\\\', str(b_cha)).group(1) + ' 7c').upper()
                else:                                 #否則
                    pb_cha = (re.match(r'b\'\\x(.{2})(.+)', str(b_cha)).group(1) + ' ' + re.match(r'0x(.+)', hex(ord(str(b_cha)[-2]))).group(1)).upper()
        except:
            b_cha = None
            pb_cha = '此字符不在BIG5中。'
        print(str(i + 1), '.', u_str[i], '\n', 'Unicode: ', pu_cha.upper(), '\n', '區塊: ', block_cha, '\n', 'GB/T 2312: ', pg_cha, '\n', 'BIG5: ', pb_cha, '\n')