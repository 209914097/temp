# 题目:微信支付宝金额收款语音播报
# 参考资料：https://tool.gaodun.com/rmb.html
# 测试案例：
# 0 零元
# 0.0 零元
# 0.00 零元
# 1234567 壹佰贰拾叁万肆仟伍佰陆拾柒元
# 1234567.01 壹佰贰拾叁万肆仟伍佰陆拾柒元壹分
# 1234567.10 壹佰贰拾叁万肆仟伍佰陆拾柒元壹角
# 10 拾元
# 15 拾伍元
# 21 贰拾壹元
# 10.01 拾元壹分
# 10.10 拾元壹角
# 10.1 拾元壹角
# 100010.10 拾万零拾元壹角
# 100020.10 拾万零贰拾元壹角
# 200010.10 贰拾万零拾元壹角
# 0.1 壹角
# 0.10 壹角
# 0.01 壹分
# 10001000 壹仟万零壹仟元
a=200010.10
intnum = str(a).split('.')[0]
try:floatnum=str(a).split('.')[1]
except:floatnum=''

l = len(intnum)
intnum=list(intnum)
ans=''
money = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
pos = ['','','拾','佰','仟','万','拾','佰','仟','亿']
zero=False
wan=True
for i in intnum:
    if i=='0':
        zero=True
    else:
        if zero:
            ans+='零'
            zero = False
        if pos[l]=='拾' and i=='1':  #对拾元单独处理，使之更符合日常读法，即10元读作拾元，不读作壹拾元
            ans += pos[l]            #对拾元单独处理，使之更符合日常读法，即10元读作拾元，不读作壹拾元
        else:
            ans+=money[int(i)]
            ans+=pos[l]
        if pos[l]=='万':wan=False
    l=l-1
    if l==4 and wan==True: ans+='万'

if ans=='' and (floatnum=='' or floatnum=='0'):ans='零元'
elif ans=='' and floatnum!='':ans=''
elif ans!='' and floatnum!='':ans+='元'
elif ans!='' and floatnum=='':ans+='元'
# 小数金额部分
floatzero=False
# if floatnum!='':
#     if int(floatnum)!=0:
#         ans += '点'
#         for i in floatnum:
#             if i=='0':
#                 floatzero=True
#             else:
#                 if floatzero:
#                     ans+='零'
#                     floatzero = False
#                 ans+=money[int(i)]

if floatnum!='':


    if int(floatnum)!=0:
        jiao=True
        fen=False

        floatl = len(floatnum)
        for i in floatnum:
            if i=='0':
                jiao = False
            else:
                if jiao:
                    ans += money[int(i)]
                    ans+='角'
                    jiao=False
                else:
                    ans+=money[int(i)]
                    ans += '分'

print(ans)
