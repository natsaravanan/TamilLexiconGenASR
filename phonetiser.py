import codecs
import os
def tam2arpabet(text):
    eng_phone=['AH','AA','IH','IY','UH','UW','EH','EY','AY','AO','OH','AW','K','G','HH','NG','CH','J','NC','T','D','NX','TH','DH','NH','P','B','M','Y','RR',
               'L','V','Z','LL','R','N','AA','IH','IY','UH','UW','EH','EY','AY','AO','OH','AW',
               'K AH','HH AH','NG AH','CH AH','S AH','J AH','NC AH','T AH','D AH','NX AH','TH AH','NH AH','P AH','B AH','M AH','Y AH','RR AH',
               'L AH','V AH','Z AH','LL AH','R AH','N AH','SH AH','KSH AH','SR','AK','KS AH'] 
    tam_phone=['அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ','க்','க்','ஹ்','ங்','ச்','ஜ்','ஞ்','ட்','ட்','ண்','த்','த்','ந்','ப்','ப்','ம்','ய்','ர்',
               'ல்','வ்','ழ்','ள்','ற்','ன்',u'\u0bbe',u'\u0bbf', u'\u0bc0', u'\u0bc1', u'\u0bc2',u'\u0bc6', u'\u0bc7', u'\u0bc8', u'\u0bca',u'\u0bcb', u'\u0bcc',
               'க','ஹ','ங','ச','ஸ','ஜ','ஞ','ட','ட','ண','த','ந','ப','ப','ம','ய','ர',
               'ல','வ','ழ','ள','ற','ன','ஷ','க்ஷ','ஸ்ரீ','ஃ','ஶ']  
    signs = [u'\u0b81', u'\u0b82', u'\u0bbd', u'\u0bbe',
                 u'\u0bbf', u'\u0bc0', u'\u0bc1', u'\u0bc2', u'\u0bc3',
                 u'\u0bc4', u'\u0bc6', u'\u0bc7', u'\u0bc8', u'\u0bca',
                 u'\u0bcb', u'\u0bcc', u'\u0bcd', u'\u0bd7']
    arpa=''

    #for x in signs:
        #print (x)
    #print(len(eng_phone))
    #print(len(tam_phone))
    l=len(text)
    lst=list(text)
    t=[]
    virama = u'\u0bcd'
    #print(l)
    #print(lst)
    count=1
    for idx,x in enumerate(lst):
     #   print("Iteration - "+str(count))
        count=count+1
        if x in signs:
            #print( x in signs)
            j=idx-1
            #print(text[j])
            #print('text[i]'+text[j])
            try:
                i=tam_phone.index(text[j])
            #print(eng_phone[i])
            #print(j)
            #print(lst[i-1])
            #print(tam_phone[i])
            #print(t)
                del t[len(t)-1]
            #print(t)
                t.append(eng_phone[i].split(' ')[0])
            except ValueError:
                pass
            #print(t)
        if x in tam_phone:
            i=tam_phone.index(x)
            #print(x)
            #print(i)
            #print(eng_phone[i])
            t.append(eng_phone[i])
         
    #print(t)
    #print(text)
    
    for x in t:
        arpa=arpa+" "+str(x)
    
    #print(arpa)
    return arpa
#tam2arpabet("சரவணன்")
def writetofile(filename):
    t=[]
    s=[]
    snew=[]
    newfilename="new_"+filename
    phonefilename="ph_"+filename
    print(os.listdir()) 
    with open(filename, encoding='utf-8') as f:
        for line in f:
            #print(line.replace("\n", ""))
            text=line.replace("\n", "")            
            #print(tam2arpabet(text))
            t.append(text)
            t.append(tam2arpabet(text))
            s.append(tam2arpabet(text).split(' '))
    print(t)
    for y in s:
        #print(y)
        for z in y:
            snew.append(z)
    k=list(set(snew))
            
    f=open(newfilename,'w',encoding="utf-8")
    for i in range(0,len(t),2):
        f.write(t[i])
        f.write(t[i+1])
        f.write("\n")
    f.close()
    f1=open(phonefilename,'w',encoding="utf-8")
    f1.write('SIL')
    f1.write('\n')
    for x in k:
        if x=='':
            continue
        
        f1.write(x)
        #f.write(t[i+1])
        f1.write("\n")
    f1.close()
    
tam2arpabet("அஞ்சல்")
writetofile("tamil.dic")
