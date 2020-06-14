Assembly_Mnemonic={"ADD":"24" ,"ADDF":"88" ,"ADDR":"144" ,"AND":"64" ,"CLEAR":"180" ,"COMP":"40" ,"COMPF":"136" 
,"COPMR":"160" ,"DIV":"36" ,"DIVF":"100" ,"DIVR":"156" ,"FIX":"196" ,"FLOAT":"192" ,"HIO":"244" ,"J":"60" 
,"JEQ":"48" ,"JGT":"52" ,"JLT":"56" ,"JSUB":"72" ,"LDA":"0" ,"LDB":"104" ,"LDCH":"80" ,"LDF":"112" ,"LDL":"8" 
,"LDS":"108" ,"LDT":"116" ,"LDX":"4" ,"LPS":"224" ,"UML":"32" ,"MULF":"96" ,"MULR":"152" ,"NORM":"200" 
,"OR":"68" ,"RD":"216" ,"RMO":"172" ,"RSUB":"76" ,"SHIFTL":"164" ,"SHIFTR":"168" ,"SIO":"240" ,"SSK":"236" 
,"STA":"12" ,"STB":"120" ,"STCH":"84" ,"STF":"128" ,"STI":"212" ,"STL":"20" ,"STS":"124" ,"STSW":"232" 
,"STT":"132" ,"STX":"16" ,"SUB":"28" ,"SUBF":"92" ,"SUBR":"148" ,"SVC":"176" ,"TD":"224" ,"TIO":"248" 
,"TIX":"44" ,"TIXR":"184" ,"WD":"220" ,"+ADD":"24" ,"+ADDF":"88" ,"+AND":"64" ,"+COMP":"40" ,"+COMPF":"136" 
,"+FIX":"196" ,"+FLOAT":"192" ,"+HIO":"244" ,"+J":"60" ,"+JEQ":"48" ,"+JGT":"52" ,"+JLT":"56" ,"+JSUB":"72" 
,"+LDA":"0" ,"+LDB":"104" ,"+LDCH":"80" ,"+LDF":"112" ,"+LDL":"8" ,"+LDS":"108" ,"+LDT":"116" ,"+LDX":"4" 
,"+LPS":"224" ,"+UML":"32" ,"+MULF":"96" ,"+OR":"68" ,"+RD":"216" ,"+RSUB":"76" ,"+SSK":"236" ,"+STA":"12" 
,"+STB":"120" ,"+STCH":"84" ,"+STF":"128" ,"+STI":"212" ,"+STL":"212" ,"+STS":"124" ,"+STSW":"232" ,"+STT":"132" 
,"+STX":"16" ,"+SUB":"28" ,"+SUBF":"92" ,"+TD":"224" ,"+TIX":"44" ,"+WD":"220"} 

ASIC={"NULL":"0" ,"SOH":"1" ,"STX":"2" ,"ETX":"3" ,"EOT":"4" ,"ENQ":"5" ,"ACK":"6" ,"BEL":"7" ,"BS":"8" ,"HT":"9" 
,"LF":"10" ,"VT":"11" ,"FF":"12" ,"CR":"13" ,"SO":"14" ,"SI":"15" ,"DLE":"16" ,"DC1":"17" ,"DC2":"18" ,"DC3":"19" 
,"DC4":"20" ,"NAK":"21" ,"SYN":"22" ,"ETB":"23" ,"CAN":"24" ,"EM":"25" ,"SUB":"26" ,"ESC":"27" ,"FS":"28" ,"GS":"29" 
,"RS":"30" ,"US":"31" ,"SP":"32" ,"!":"33" ,"''":"34" ,"#":"35" ,"$":"36" ,"%":"37" ,"&":"38" ,"'":"39" ,"(":"40" 
,")":"41" ,"*":"42" ,"+":"43" ,",":"44" ,"-":"45" ,".":"46" ,"/":"47" ,"0":"48" ,"1":"49" ,"2":"50" ,"3":"51" ,"4":"52" 
,"5":"53" ,"6":"54" ,"7":"55" ,"8":"56" ,"9":"57" ,":":"58" ,";":"59" ,"<":"60" ,"=":"61" ,">":"62" ,"?":"63" ,"@":"64" 
,"A":"65" ,"B":"66" ,"C":"67" ,"D":"68" ,"E":"69" ,"F":"70" ,"G":"71" ,"H":"72" ,"I":"73" ,"J":"74" ,"K":"75" ,"L":"76" 
,"M":"77" ,"N":"78" ,"O":"79" ,"P":"80" ,"Q":"81" ,"R":"82" ,"S":"83" ,"T":"84" ,"U":"85" ,"V":"86" ,"W":"87" ,"X":"88" 
,"Y":"89" ,"Z":"90" ,"[":"91" ,"\\":"92" ,"]":"93" ,"^":"94" ,"_":"95" ,"`":"96" ,"a":"97" ,"b":"98" ,"c":"99" 
,"d":"100" ,"e":"101" ,"f":"102" ,"g":"103" ,"h":"104" ,"i":"105" ,"j":"106" ,"k":"107" ,"l":"108" ,"m":"109" ,"n":"110" 
,"o":"111" ,"p":"112" ,"q":"113" ,"r":"114" ,"s":"115" ,"t":"116" ,"u":"117" ,"v":"118" ,"w":"119" ,"x":"120" ,"y":"121" 
,"z":"122" ,"{":"123" ,"|":"124" ,"}":"125" ,"~":"126" ,"DEL":"127"}
#在這邊輸入組合語言，轉成機器語言
# opcode需要大寫
#第一步：讀入字串
#第二步：將字串分割儲存
#第三步：確定 opcode存在於 optable
#第四步：確定 oprand的值有被宣告於 lable，另確定 lable中沒有重複宣告的
#第五步：進位的轉換以及， PC程式計數器的建立
#第六步：輸出目的碼
      
ch=[]       #存格式正確的組合語言程式
lable=[]        #存 lable值
opcode=[]       #存 opcode值
oprand=[]       #存所有的 oprand值
oprW=[]     #存只為字串的 oprand
oprN=[]     #存只有數字的 oprand
PC=[]       #程式計數器，紀錄下個記憶體位址應該在哪
s=0     #以 s這個字元做開關，判斷何時開始讀字串
print("輸入 s以開始寫程式， c以開始組譯 :\n")

while True:     #持續輸入。輸入 s以開始讀取組合語言， END以結束
    code=input("input: ")
    if code == "c":       #如果輸入為 c代表停止輸入程式碼
        break

    if code == "s":     #如果輸入為 s，代表可以開始輸入程式

        while True:
            code=input("here: ")            
            st=code.split()     # split()做字串的分割

            if len(st) == 2:        #如果字串分割後只有兩個，及只有 opcode和 oprand的話

                if st[0] == "END":       #若 END字串存在，則結束本段組合語言
                    ch.append(st)
                    s=0
                    break
                elif Assembly_Mnemonic.get(st[0]) == None:     #如果 opcode沒有被找到，輸出錯誤訊息
                    print("Your opcode have something wrong !\n")

                elif s==1:      #當 s為1時，代表已經找到 START，可以開始紀錄程式
                    ch.append(st)       #將所有程式碼存至 ch    
                    oprand.append(st[1])        #把 oprand獨立再紀錄
                    opcode.append(st[0])
                    lable.append(' ')

                    if st[0].find('+') != -1:       #若有 +字元出現，PC位置加四
                        PC.append(PC[-1])
                        num=PC[-1]+4
                        PC[-1]=num
                    else:       #否則 PC位置加三
                        PC.append(PC[-1])
                        num=PC[-1]+3
                        PC[-1]=num

                    if st[1].isalpha() == True:     #若 oprand為全字元，及有使用到 lable，記錄到 oprW裡面
                        oprW.append(st[1])
                        
            elif len(st) == 3:      #字串分割後有三個，及有 lable、 opcode和 oprand

                if st[1] == "START":       #若 START字串存在，則開始紀錄程式
                    ch.append(st)
                    oprand.append(st[2])
                    s=1
                    PC.append(int('0x'+st[2] ,16))      #將輸入的數字從十進位的值變成十六進位的值，也就是 10 =16，及使用者輸入十進位 1000，儲存時自動變為 4096

                elif st[1] =='BYTE' or st[1] =='WORD' or st[1]=='RESB' or st[1] =='RESW':       #下面這一串，是用來計算字組、位元組，計算 PC位置要加多少
                    ch.append(st)
                    lable.append(st[0])
                    oprand.append(st[2])
                    PC.append(PC[-1])
                    
                    if st[1]=='BYTE':
                        num=PC[-1]+len(st[2])-3
                        PC[-1]=num
                    
                    elif st[1]=='WORD':
                        num=PC[-1]+3
                        PC[-1]=num

                    elif st[1]=='RESB':
                        num=PC[-1]+int(st[2])
                        PC[-1]=num
                    
                    elif st[1]=='RESW':
                        num=PC[-1]+int(st[2])*3
                        PC[-1]=num

                elif Assembly_Mnemonic.get(st[1]) == None:
                    print("Your opcode have something wrong !\n")

                elif s==1:
                    ch.append(st)
                    lable.append(st[0])     #把 lable獨立再紀錄
                    opcode.append(st[1])
                    oprand.append(st[2])

                    if st[0].find('+') != -1:       #如果找到 +這個字元，代表使用擴增格式
                        PC.append(PC[-1])       #下面三行做這件事情，新增一個值，並加四
                        num=PC[-1]+4
                        PC[-1]=num
                    else:   
                        PC.append(PC[-1])       #下面三行做這件事情，新增一個值，並加3
                        num=PC[-1]+3
                        PC[-1]=num

                    if st[2].isalpha() == True:
                        oprW.append(st[2])
            else:
                print("Your code have something wrong !\n")

len_of_lable=len(lable)     # lable裡面總共有幾個字串
len_of_oprW=len(oprW)        # oprW裡面總共有幾個字串
set_of_lable=set(lable)     #將 lable從 list轉變成集合
num_of_oprW=0

while True:     #確定oprand 存在於 lable

    if num_of_oprW == len_of_oprW:      #已經從頭找到尾的話
        break

    elif (oprW[num_of_oprW] in set_of_lable) == True:       #如果 oprW中的字串存在於 lable
        num_of_oprW+=1
    
    elif (oprW[num_of_oprW] in set_of_lable) == False:      #如果不存在的話
        print("Your oprand or lable have something wrong !")
        break
#下面做 oprW連結 lable對應到的 PC位置，並做最後的目的碼輸出
#指向現在對應到的 ch
# ch裡面總共有多少字串
num_of_ch=1     
len_of_ch=len(ch)       
if num_of_ch<=len_of_ch:
    while True:     
        if len_of_ch == num_of_ch+1:      
            break
        
        else:
            part_of_ch=ch[num_of_ch]              
            if len(part_of_ch) == 2: 
                while True:                        
                    if part_of_ch[0] =='END':        
                        num_of_ch+=1
                        break
                    else:
                        ans_of_code=hex(int(Assembly_Mnemonic[part_of_ch[0]])) 
                        fin_lable=0
                        dif_of_pc=6                            
                        if len(ans_of_code) == 3:       #為了格式，補上一個 0字元
                            print("0" ,end='')
                            print(ans_of_code[2:] ,end='')
                        else:
                            print(ans_of_code[2:] ,end='')

                        if part_of_ch[1].isalpha() == True:     #如果這邊的 oprand有引用 lable的話   
                            while True:
                                if part_of_ch[1] == lable[fin_lable]:
                                    store_of_pc=hex(int(PC[fin_lable]))     #將此 PC位置轉成十六進位數字，0X.....
                                    len_of_pc=len(store_of_pc)

                                    if len_of_pc == 3:
                                        print("000" ,end='')
                                        print(store_of_pc[2:])
                                    elif len_of_pc == 4:
                                        print("00" ,end='')
                                        print(store_of_pc[2:])
                                    elif len_of_pc == 5:
                                        print("0" ,end='')
                                        print(store_of_pc[2:])
                                    elif len_of_pc == 6:
                                        print(store_of_pc[2:]) 
                                    num_of_ch+=1
                                    break
                                else:
                                    fin_lable+=1
                            break

                        else:
                            ans_of_rand=hex(int(part_of_ch[1]))       #將 oprand轉成十六進位的目的碼
                            len_of_rand=len(ans_of_rand)        # ans_of_rand的總長度，0x......
                            dif_of_rand=6-len_of_rand

                            if  dif_of_rand > 0:       #判斷還需要幾個 0，當然又是為了格式正確
                                while True:
                                    if dif_of_rand > 0:     #當還需要追加 0得時候
                                        print("0" ,end='')
                                        dif_of_rand-=1
                                    elif dif_of_rand == 0:                             
                                        print(ans_of_rand[2:])
                                        dif_of_rand-=1
                                        num_of_ch+=1        #輸出後，指標往後     
                                        break
                            break                                    

            if len(part_of_ch) == 3:      
                while True:
                    if part_of_ch[1] == "BYTE":     
                        part_of_byte=part_of_ch[2]      
                        part_of_byte=part_of_byte.split("'")        
                        byte=part_of_byte[1]        
                        len_of_byte=len(byte)
                        point_of_byte=0

                        if len_of_byte > point_of_byte:
                            while True:
                                if len_of_byte == point_of_byte:
                                    print()
                                    point_of_byte+=1
                                    num_of_ch+=1
                                    break
                                else:
                                    store_of_byte=byte[point_of_byte:point_of_byte+1]
                                    store_of_byte=hex(int(ASIC[store_of_byte]))
                                    print(store_of_byte[2:] ,end='')
                                    point_of_byte+=1  
                        break

                    elif part_of_ch[1] == "WORD":        
                        word=part_of_ch[2]   
                        len_of_word=len(word)       
                        point_of_word=0

                        if len_of_word == 1:
                            print("00000" ,end='')
                            print(word)
                        elif len_of_word == 2:
                            print("0000" ,end='')
                            print(word)
                        elif len_of_word == 3:
                            print("000" ,end='')
                            print(word)
                        elif len_of_word == 4:
                            print("00" ,end='')
                            print(word)
                        elif len_of_word == 5:
                            print("0" ,end='')
                            print(word)
                        elif len_of_word == 6:
                            print(word)        

                        num_of_ch+=1
                        break  

                    elif part_of_ch[1] == "RESW" or part_of_ch[1] == "RESB":        
                        num_of_ch+=1
                        break

                    else:       
                        ans_of_code=hex(int(Assembly_Mnemonic[part_of_ch[1]]))      
                        fin_lable=0
                        if len(ans_of_code) == 3:       
                            print("0" ,end='')
                            print(ans_of_code[2:] ,end='')
                        else:
                            print(ans_of_code[2:] ,end='')
                        
                        if part_of_ch[2].isalpha() == True:     #如果這邊的 oprand有引用 lable的話   
                            while True:
                                if part_of_ch[2] == lable[fin_lable]:
                                    store_of_pc=hex(int(PC[fin_lable]))     #將此 PC位置轉成十六進位數字，0X.....
                                    len_of_pc=len(store_of_pc)

                                    if len_of_pc == 3:
                                        print("000" ,end='')
                                        print(store_of_pc[2:])
                                    elif len_of_pc == 4:
                                        print("00" ,end='')
                                        print(store_of_pc[2:])
                                    elif len_of_pc == 5:
                                        print("0" ,end='')
                                        print(store_of_pc[2:])
                                    elif len_of_pc == 6:
                                        print(store_of_pc[2:]) 
                                    num_of_ch+=1
                                    break
                                else:
                                    fin_lable+=1
                            break

                        else:
                            ans_of_rand=hex(int(part_of_ch[2]))       
                            len_of_rand=len(ans_of_rand)        
                            dif_of_rand=6-len_of_rand

                            if  dif_of_rand > 0:       
                                while True:
                                    if dif_of_rand > 0:
                                        print("0" ,end='')
                                        dif_of_rand-=1
                                    elif dif_of_rand == 0:
                                        print(ans_of_rand[2:])
                                        dif_of_rand-=1
                                        num_of_ch+=1         
                                        break
                            break