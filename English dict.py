d={}
print("歡迎來到我的字典")

while True:
    print("1建立字典")
    print("2列出所有單字")
    print("3英翻中") 
    print("4中翻英")
    print("5測驗")
    print("6離開")
    option=input("請輸入選項")
    
    if option=='6':
        break
    elif option=='1':
        while True:
            voc=input('請輸入新英文單字(按0退出):')
            if voc == '0':
                break
            if voc not in d:
                voc_ch=input('輸入中文')
                d[voc]=voc_ch
            else:
                print('已存在')
    elif option=='2':
            s=sorted(d)
            
            for i in s:
                print(i,':',d[i])
    elif option=='3':
        while True:
            voc=input('請輸入新英文單字(按0退出):')
            if voc=='0':
                break
            if voc in d:
                print("有這個單字")
            else:
                 print("沒有這個單字")
    elif option=='4':
        while True:
            got=False
            ch=input('請輸入中文單字(按0退出):')            
            if ch=='0':
                break
            for k,v in d.items():
                if ch==v:
                    print(ch,'的英文是',k)
                    got=True
            if got==False:
                print('沒有這個單字')
    elif option =='5':
        score=0
        
        for k,v in d.items():
        
            print(v)
            ans=input(':')
            
            if ans== k:
                print('恭喜答對')
                score+=1
            else:
                print("錯了")
        print('答對了',score,'分')        
                            
                    










