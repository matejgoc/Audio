import random

outcome=["","","","","","","","","","","","","","","","","","","","","","",""]
audiologist = ["John", " Smith, M.Cl.Sc. Audiologist, Reg. CASLPO","JS"]
namea=["name","his/her","him/her","he/she"]
nameb=[""]
bnoun=["spouse"]
count=[1]
prevhas=False

def chkabcde(x,upper):
    abcde= str(list(range(1,upper)))
    if x == "/":
        count[0]-=2
        return x
    if x in abcde and x != "":
        return x
    else:
        y = input("Please input a valid number.")
        if y == "/":
            count[0]-=2
            return y
        if y in abcde and y != "":
            return y
        else:
            z= chkabcde(x,upper)
            return z

def gender(x):
    print("Patient sex?")
    print("1:Male")
    print("2:Female")
    ans = input()
    answ=chkabcde(ans,3)
    if answ == "1":
        namea[1]=" his"
        namea[2]=" him"
        namea[3]=" he"        
        bnoun[0]="wife"
    if answ == "2":
        namea[1]=" her"
        namea[2]=" her"
        namea[3]=" she"   
        bnoun[0]="husband"
    print("Please enter the patient name, press enter.")
    namea[0]= input()

def nameo(x):
    print("Please enter the name.")
    ans =input()
    return ans

def accompany(x):
    print("Accompaniment?")
    print("1: Unaccompanied")
    print("2: Accompanied by spouse")
    print("3: Accompanied by family or child")
    print("4: Accompanied by friend")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        a=[namea[0]+" was unaccompanied for"+namea[1]+" appointment.",
           namea[0]+" came in today for" +namea[1]+" appointment unaccompanied.",
           namea[0]+" came in today for their appointment unaccompanied.",
           namea[0]+" arrived on time for their appointment today by themselves."
           ]
        
        outcome[x]= a[random.randint(0,3)]
    if answ == "2":
        nameb[0]=nameo(1)
        a=[namea[0]+" was accompanied by"+namea[1]+" "+bnoun[0]+" "+nameb[0]+" for the appointment.",
           namea[0]+" came in today for" +namea[1]+" appointment accompanied by"+namea[1]+" "+bnoun[0]+" "+nameb[0]+".",
           namea[0]+" came in today for their appointment accompanied by"+namea[1]+" "+bnoun[0]+" "+nameb[0]+".",
           namea[0]+" arrived on time for their appointment today"+namea[1]+" "+bnoun[0]+" "+nameb[0]+"."
           ]
        
        outcome[x]= a[random.randint(0,3)]
    if answ == "3":
        nameb[0]=nameo(1)
        custom= input("Enter custom relation (son,daughter,family):")
        a=[namea[0]+" was accompanied by"+namea[1]+" "+custom+" "+nameb[0]+" for the appointment.",
           namea[0]+" came in today for" +namea[1]+" appointment accompanied by"+namea[1]+" "+custom+" "+nameb[0]+".",
           namea[0]+" came in today for their appointment accompanied by"+namea[1]+" "+custom+" "+nameb[0]+".",
           namea[0]+" arrived on time for their appointment today"+namea[1]+" "+custom+" "+nameb[0]+"."
           ]
        
        outcome[x]= a[random.randint(0,3)]
    if answ == "4":
        nameb[0]=nameo(1)
        a=[namea[0]+" was accompanied by"+namea[1]+" friend "+nameb[0]+" for the appointment.",
           namea[0]+" came in today for" +namea[1]+" appointment accompanied by"+namea[1]+" friend "+nameb[0]+".",
           namea[0]+" came in today for their appointment accompanied by"+namea[1]+" friend "+nameb[0]+".",
           namea[0]+" arrived on time for their appointment today"+namea[1]+" friend "+nameb[0]+"."
           ]
        
        outcome[x]= a[random.randint(0,3)]
    if answ == "5":
        nameb[0]=nameo(1)
        ohh= namea[0]+ "..."
        custom = input(ohh)
        outcome[x]=custom

def consultent(x):
    print("Consult with ENT?")
    print("1: None")
    print("2: Previous consult resolved normally")
    print("3: Issues, not surgically remediable")    
    print("4: Issues, resolved with treatment")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        a=[" There is no previous consult with an ENT specialist.",
           " "+namea[0]+" reported no previous consultation with an ENT specialist.",
           " "+namea[0]+" has not been to an ear nose and throat specialist.",
           " "+namea[0]+" did not have any prior consultation with an ENT specialist."
           ]
        
        outcome[x]= a[random.randint(0,3)]        
    if answ == "2":
        age=input("How many years ago?")
        a=[" There was a consult with ENT specialist "+age+" years ago, everything came out normal.",
           " "+namea[0]+" reported a consultation with an ENT specialist "+age+" years ago and that everything came out normal.",
           " "+namea[0]+" reports no issues after a consultation with an ENT specialist "+age+" years ago.",
           " "+age+ " years ago "+namea[0]+" went to see an ENT specialist and no issues were discovered."
           ]
        
        outcome[x]= a[random.randint(0,3)]           
    if answ == "3":
        age=input("How many years ago?")
        issue=input("Which issue was discussed?")
        a=[" There was a consult with ENT specialist "+age+" regarding "+issue+", but was informed that the issue was not surgically remediable.",
           " "+namea[0]+" reported a consultation with an ENT specialist "+age+" years ago and discussed "+issue+". The ENT specialist informed them that it was not surgically remediable.",
           " "+age+ " years ago "+namea[0]+" went to see an ENT specialist and discussed "+issue+" but they were told surgery would not help."
           ]
                
        outcome[x]= a[random.randint(0,2)]
    if answ == "4":
        age=input("How many years ago?")
        issue=input("Which issue was discussed?")
        a=[" There was a consult with ENT specialist "+age+" regarding "+issue+", and the issue was resolved with treatment.",
           " "+namea[0]+" reported a consultation with an ENT specialist "+age+" years ago and discussed "+issue+". They were treated for the issue.",
           " "+age+ " years ago "+namea[0]+" went to see an ENT specialist and discussed "+issue+" and they were treated for the issue."
           ]
                
        outcome[x]= a[random.randint(0,2)]
    if answ == "5":
        woo=input(" There was a consult with ENT specialist:")
        outcome[x]=" There was a consult with ENT specialist" +woo

def surgeries(x):
    print("Previous surgeries or ear infections?")
    print("1: None")
    print("2: Previous surgery but no ear infections")
    print("3: Previous ear infections but no surgery")    
    print("4: Both")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        a=[" There are no reported surgeries or recent middle ear infections.",
           " "+namea[0]+" reported no surgeries or recent middle ear infections.",
           " There are no reported surgeries on the ear or infections."
           ]
        
        outcome[x]= a[random.randint(0,2)]   
    if answ == "2":
        age=input("How many years ago?")
        surgery = input("What issue was resolved with surgery?")
        a=[" "+age+" years ago a surgery was performed to remedy "+surgery+". There are no reports of recent middle ear infections.",
           " "+namea[0]+" reported that they had a surgery "+age+" years ago to remedy "+surgery+" but that recently they have had no problems with middle ear infections."
           ]
        
        outcome[x]= a[random.randint(0,1)] 
    if answ == "3":
        age=input("How many years ago for most recent ear infection?")
        surgery = input("How many ear infections have they had (write it out)?")
        a=[" "+age+" years ago "+namea[0]+" had "+surgery+" ear infection. There are no reports of surgeries on the ear.",
           " "+namea[0]+" reported that they had "+surgery+" ear infection "+age+" years ago but that they have had no surgeries on the ears."
           ]
        
        outcome[x]= a[random.randint(0,1)] 
    if answ == "4":
        age=input("Surgery: How many years ago?")
        surgery = input("What issue was resolved with surgery?")
        age1=input("How many years ago for most recent ear infection?")
        surgery1 = input("How many ear infections have they had (write it out)?")
        a=[" "+age+" years ago a surgery was performed to remedy "+surgery+". The patient reports "+surgery1+" ear infections "+age1+" years ago.",
           " "+namea[0]+" reported that they had a surgery "+age+" years ago to remedy "+surgery+" and that they have had "+surgery1+" ear infections "+age1+" years ago.."
           ]
        
        outcome[x]= a[random.randint(0,1)] 
    if answ == "5":
        custom = input("Input custom:")
        outcome[x]= custom
        
def exposure(x):
    print("Noise exposure?")
    print("1: None")
    print("2: Previous occupational")
    print("3: Current occupational")    
    print("4: Hobby")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        a=[" There is no reported history of noise exposure.",
           " "+namea[0]+" reported no history of noise exposure.",
           " There are no reported excessive noise exposure occupationally or in their hobbies."
           ]
        
        outcome[x]= a[random.randint(0,2)]  
    if answ == "2":
        age=input("How many years ago?")
        length=input("For how many years?")
        job=input("What occupation?")
        a=[" There is a reported history of occupational noise exposure "+age+" years ago for "+length+" years as they worked as a "+job+".",
           " "+namea[0]+" reports that they "+age+" years ago they worked as a "+job+" for "+length+" years."
           ]
        
        outcome[x]= a[random.randint(0,1)]  
    if answ == "3":
        length=input("For how many years?")
        job=input("What occupation?")
        a=[" There is a reported current occupational noise exposure that has been ongoing for "+length+" years as they work as a "+job+".",
           " "+namea[0]+" reports that they have been working as a "+job+" for "+length+" years where they are exposed to excessive noise."
           ]
        
        outcome[x]= a[random.randint(0,1)] 
    if answ == "4":
        hobby=input("What hobby?")
        a=[" There is a reported current recreational activity with excesssive noise exposure as they enjoy "+hobby+".",
           " "+namea[0]+" reports that they have a hobby "+hobby+" where they are exposed to excessive noise."
           ]
        
        outcome[x]= a[random.randint(0,1)] 
    if answ == "5":
       custom=input("History of noise exposure includes:")
       outcome[x]=" History of noise exposure includes" +custom
     
def tinnitus(x):
    print("Tinnitus or vestibular concern?")
    print("1: None")
    print("2: Tinnitus only")
    print("3: Vestibular concerns only")    
    print("4: Both")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        a=[" There is no reported tinnitus nor vestibular concerns.",
           " "+namea[0]+" reports no tinnitus nor vestibular concerns."
           ]
        
        outcome[x]= a[random.randint(0,1)] 
    if answ == "2":
        constant=input("Constant or other (not bothersome?)")
        age= input("For how many years?")
        a=[" There is a reported "+constant+" tinnitus for "+age+" years, but no significant vestibular concerns.",
           " "+namea[0]+" reports "+constant+" tinnitus for "+age+" years, but no significant vestibular concerns.",
           " There is a reported "+constant+" tinnitus for "+age+" years, but no significant vestibular concerns."
           ]
        
        outcome[x]= a[random.randint(0,2)] 
    if answ == "3":
        constant=input("What kind of vestibular concerns?")
        age= input("For how many years?")
        a=[" There is a reported vestibular concern regarding "+constant+" for "+age+" years, but no tinnitus.",
           " "+namea[0]+" reports vestibular concerns regarding "+constant+" for "+age+" years, but no tinnitus.",
           " There is a reported vestibular concern regarding "+constant+" for "+age+" years, but no tinnitus."
           ]
        
        outcome[x]= a[random.randint(0,2)] 
    if answ == "4":
        constant=input("Tinnitus: Constant or other (not bothersome?)")
        age= input("Tinnitus: For how many years?")
        constant1=input("Vestibular: What kind of vestibular concerns?")
        age1= input("Vestibular: For how many years?")
        a=[" There is a reported "+constant+" tinnitus for "+age+" years, and a reported vestibular concern regarding "+constant1+" for "+age1+" years.",
           " "+namea[0]+" reports "+constant+" tinnitus for "+age+" years, and a reported vestibular concern regarding "+constant1+" for "+age1+" years.",
           " There is a reported "+constant+" tinnitus for "+age+" years, and a reported vestibular concern regarding "+constant1+" for "+age1+" years."
           ]
        
        outcome[x]= a[random.randint(0,2)]        
    if answ == "5":
        custom = input("Input custom:")
        outcome[x]= custom

def hlchange(x):
    print("Hearing loss observed as?")
    print("1: None")
    print("2: Gradual change")
    print("3:")    
    print("4:")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= " "+namea[0]+" has not observed a hearing loss."
    if answ == "2":
        outcome[x]=" "+namea[0]+" observed that the hearing loss has been a gradual change."
    if answ == "3":
        outcome[x]=""
    if answ == "4":
        outcome[x]=""
    if answ == "5":
        custom = input()
        outcome[x]= custom

def prevha(x):
    print("Previous hearing aids?")
    print("1: None")
    print("2: Wore bilateral custom hearing aids")
    print("3: Wore hearing aids which they did/ do not wear")    
    print("4: Wore hearing aids and not suitable")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= " "
    if answ == "2":
        age= input("Age of hearing aids in years?")
        prevhas=True
        outcome[x]=" "+namea[0]+" wore bilateral custom hearing aids which are " +age+ " years old."
    if answ == "3":
        age= input("Age of hearing aids in years?")
        prevhas=True
        outcome[x]=" "+namea[0]+" purchased bilateral custom hearing aids which are " +age+ " years old but reportedly did not wear them."
    if answ == "4":
        age= input("Age of hearing aids in years?")
        outcome[x]=" "+namea[0]+" wore hearing aids which are " +age+ " years old. They no longer provide optimal amplification."
    if answ == "5":
        custom=input("Please enter a description of the hearing aids.")
        prevhas=True
        outcome[x]= custom

def difficulty(x):
    print("Difficulty?")
    print("1: No more to list")
    print("2: In group situations")
    print("3: In background noise")
    print("4: On the telephone")    
    print("5: In meetings")
    print("6: In everyday communication")
    print("7: In the theatre")
    print("8: At a sporting event")
    print("9: At church")
    print("10: Custom")
    ans = input()
    answ=chkabcde(ans,11)    
    if answ == "1":
        inten= ""
    if answ == "2":
        inten= "in group situations,"
    if answ == "3":
        inten ="in background noise,"
    if answ == "4":
        inten ="on the telephone,"
    if answ == "5":
        inten = "in meetings,"
    if answ == "6":
        inten = "in everyday communication,"
    if answ == "7":
        inten = "in the theatre,"
    if answ == "8":
        inten = "at a sporting event,"
    if answ == "9":
        inten = "at church,"
    if answ == "10":
        custom = input()
        inten = custom+","
    return inten    

def difficult(x):
    count=10
    made= ["","","","","","","","",""]
    while count >0:
        response = difficulty(x)
        count-=1
    made= "difficulty hearing in "+""
        

def cosi(x):
    print("COSI?")
    print("1: Everyday effective communication with previous hearing aids.")
    print("2: Difficulty in groups")
    print("3: Select some difficulties(Not done)")    
    print("4: Accompaniment acknowledgees hearing loss")
    print("5: Custom input")
    ans = input()
    answ=chkabcde(ans,6)

    if answ == "1":
        outcome[x]= " COSI: "+namea[0]+" uses" +namea[1]+" hearing aids for everyday effective communication."
    if answ == "2":
        outcome[x]=" COSI: "+namea[0]+" notices difficulty hearing in group situations, background noise and on the telephone."
    if answ == "3":
        outcome[x]=""
    if answ == "5":
        cozy=input("Please input custom COSI:")
        outcome[x]=" COSI: "+cozy
    if answ == "4":
        outcome[x]=" COSI: "+nameb[0]+" reports that "+namea[0]+" no longer hears well anymore."

def otoscopy(x):
    print("Otoscopy Results?")
    print("1: R, L - Clear EAM with good view of TM.")
    print("2: R, L - Slight cerumen in EAM, non-occluding, with good view of TM.")
    print("3: ")    
    print("4: ")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= "R, L - Clear EAM with good view of TM."
    if answ == "2":
        outcome[x]= "R, L - Slight cerumen in EAM, non-occluding, with good view of TM "
    if answ == "3":
        outcome[x]=""
    if answ == "4":
        outcome[x]=""
    if answ == "5":
        custom = input()
        outcome[x]= custom

def intensity(x):
    print("Intensity?")
    print("1: No loss")
    print("2: Mild")
    print("3: Mild to moderate")
    print("4: Moderate")    
    print("5: Moderate to severe")
    print("6: Severe")
    print("7: Profound")
    print("8: Custom")
    ans = input()
    answ=chkabcde(ans,9)    
    if answ == "1":
        inten="no"
    if answ == "2":
        inten="mild"
    if answ == "3":
        inten ="mild to moderate"
    if answ == "4":
        inten ="moderate"
    if answ == "5":
        inten = "moderate to severe"
    if answ == "6":
        inten = "severe"
    if answ == "7":
        inten = "profound"
    if answ == "8":
        custom = input()
        inten = custom
    return inten

def losstype(x):
    print("Loss type?")
    print("1: Sensorineural")
    print("2: Conductive")
    print("3: Mixed")    
    print("4: Custom")
    ans = input()
    answ=chkabcde(ans,5)
    if answ == "1":
        nub = "sensorineural"
    if answ == "2":
        nub = "conductive"
    if answ == "3":
        nub = "mixed"
    if answ == "4":
        nub = input("Enter custom type:")

    return nub

def loss(x):
    print("Hearing loss?")
    print("1: No loss bilaterally")
    print("2: Bilateral loss")
    print("3: Sloping bilateral loss")    
    print("4: Asymmetrical loss")
    print("5: Sloping asymmetrical loss")    
    print("6: Custom")
    ans = input()
    answ=chkabcde(ans,7)
    if answ == "1":
        outcome[x]= " Normal hearing bilaterally."
    if answ == "2":
        losstyp = losstype(0)
        intensit = intensity(0)
        outcome[x]= "Bilaterally, "+intensit+ " " +losstyp+" hearing loss was found."
    if answ == "3":
        losstyp = losstype(0)        
        print("Starts at which...")
        slopa = intensity(0)
        freq= input("At what frequency does it slope?")
        print("To what...")
        slopb = intensity(0)
        outcome[x]=" "+slopa+" sloping to "+slopb+" "+losstyp+" hearing loss starting at "+freq+" bilaterally."
    if answ == "4":
        print("For the right ear:")
        losstypr = losstype(0) 
        right=intensity(0)
        print("For the left ear:")
        losstypl = losstype(0)
        left=intensity(0)
        outcome[x]=" "+right+" "+losstypr+" hearing loss in the right ear. " +left+" "+losstypl+" hearing loss in the left ear."
    if answ == "5":
        print("For the right ear:")
        losstypr = losstype(0) 
        print("Starts at which...")
        slopar = intensity(0)
        freqr= input("At what frequency does it slope?")
        print("To what...")
        slopbr = intensity(0)
        print("For the left ear:")
        losstypl = losstype(0)
        print("Starts at which...")
        slopal = intensity(0)
        freql= input("At what frequency does it slope?")
        print("To what...")
        slopbl = intensity(0)
        outcome[x]=" "+slopar+" sloping to "+slopbr+" "+losstypr+" hearing loss starting at "+freqr+" in the right ear. "+slopal+" sloping to "+slopbl+" "+losstypl+" hearing loss starting at "+freql+" in the left ear."

    if answ == "6":
        custom=input("Please enter your custom audiometry.")
        outcome[x]=custom

def warrantsent(x):
    print("Warrant ENT consult?")
    print("1: None")
    print("2: May warrant for asymmetry")
    print("3: ")    
    print("4: ")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= ""
    if answ == "2":
        outcome[x]=" May warrant ENT consult re: asymmetry of loss L>R,if not previously done."
    if answ == "3":
        outcome[x]=""
    if answ == "4":
        outcome[x]=""
    if answ == "5":
        custom = input(" May warrant ENT consult re:")
        outcome[x]= " May warrant ENT consult re: "+custom

def middleear(x):
    print("Middle ear function?")
    print("1: Normal bilaterally")
    print("2: ")
    print("3: ")    
    print("4: ")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= " Middle ear function essentially normal, bilaterally."
    if answ == "2":
        outcome[x]=""
    if answ == "3":
        outcome[x]=""
    if answ == "4":
        outcome[x]=""
    if answ == "5":
        custom = input()
        outcome[x]= custom

def wds(x):
    print("Word discrimination?")
    print("1: Excellent bilaterally")
    print("2: Fair bilaterally")
    print("3: Poor bilaterally")    
    print("4: Asymmetrical")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= " R,L - excellent"
    if answ == "2":
        outcome[x]= " R,L - fair"
    if answ == "3":
        outcome[x]= " R,L - poor"
    if answ == "4":
        r = input("R :")
        l = input("L :")
        outcome[x]= " R - "+r+", L - "+l
    if answ == "5":
        custom = input()
        outcome[x]= custom

def quicksin(x):
    print("QuickSIN")
    print("What intensity in dB?")
    inte = input()
    print("Loss?")
    loss = input()
    outcome[x]= "QuickSIN at "+inte+"dB, binaurally:" +loss+" SNR loss."

def sides(x):
    print("Hearing aids prescribed for?")
    print("1: Bilaterally")
    print("2: Right ear only needed")
    print("3: Left ear only needed")    
    print("4: Right ear only, but both ears needed")
    print("5: Left ear only, but both ears needed")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        sid= " bilaterally"
    if answ == "2":
        sid=" in the right ear"
    if answ == "3":
        sid=" in the left ear"
    if answ == "4":
        sid=" in the right ear only, even though both would be beneficial to the patient"
    if answ == "5":
        sid=" in the left ear only, even though both would be beneficial to the patient"
    return sid

def prescription(x):
    print("Prescription given for?")
    print("1: Performance and suitability")
    print("2: Cosmetics and discretion")
    print("3: Good value and affordability")    
    print("4: Ease of cleaning and use")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        sid= " performance and suitability"
    if answ == "2":
        sid=" cosmetics and discretion"
    if answ == "3":
        sid=" good value and affordability"
    if answ == "4":
        sid=" ease of cleaning and use"
    if answ == "5":
        custom = input()
        sid= custom
    return sid

def results(x):
    print("Result of appointment")
    print("1: No hearing aids needed")
    print("2: Not interested in hearing aids")
    print("3: Will consult with family and come back")    
    print("4: Custom")
    print("5: Decided to go with prescription.")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]=" No further testing recommended at this time."
    if answ == "2":
        outcome[x]=" Reviewed results with "+namea[0]+" and counseled re: communicative effects of hearing loss and possible use of amplification. Performed hearing aid evaluation and discussed 1vs2, styles, and technology. "+namea[0]+" has decided not to pursue amplification at this time."

    if answ == "3":
        outcome[x]=" Reviewed results with "+namea[0]+" and counseled re: communicative effects of hearing loss and possible use of amplification. Performed hearing aid evaluation and discussed 1vs2, styles, and technology. "+namea[0]+" may decide to pursue amplification after consultation with family."

    if answ == "4":
        custom = input("Please input custom results:")
        outcome[x]= custom
    if answ == "5":
        hearingaids=input("Please input the name of the hearing aids.")
        sid = sides(1)
        pre = prescription(1)
        outcome[x]=" Reviewed results with "+namea[0]+" and counseled re: communicative effects of hearing loss and possible use of amplification. Performed hearing aid evaluation and discussed 1vs2, styles, and technology. "+namea[0]+" decided to pursue amplification and prescription for "+hearingaids+sid+". Prescription was given for "+pre+"."

def nextapptht(x):
    print("Next appointment?")
    print("1: Fitting booked")
    print("2: Will call to book fitting")
    print("3: Booked appointment to discuss")    
    print("4: Will call to discuss")
    print("5: Will recheck as requested")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= " Fitting appointment is already scheduled."
    if answ == "2":
        outcome[x]= " "+namea[0]+" will call to book a fitting appointment when convenient."
    if answ == "3":
        outcome[x]= " Hearing aid evaluation has been booked to discuss the topic further."
    if answ == "4":
        outcome[x]= " "+namea[0]+" may call to book an appointment to discuss further."
    if answ == "5":
        outcome[x]= " Will recheck as requested."

def nextapptfit(x):
    print("Next appointment?")
    print("1: Followup booked")
    print("2: Will call to book followup")
    print("3: ")    
    print("4: ")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= "  Follow up was booked to monitor progress."
    if answ == "2":
        outcome[x]= " "+namea[0]+" will call to book a follow-up appointment when convenient."
    if answ == "3":
        outcome[x]= " "
    if answ == "4":
        outcome[x]= " "
    if answ == "5":
        custom = input("Input Custom")
        outcome[x]= custom

def outcomht(x):
    rando= [2,3,4,5,6,7]
    w= random.sample(rando,len(rando))

    print("HT:"+outcome[1]+outcome[w[0]]+outcome[w[1]]+outcome[w[2]]+outcome[w[3]]+outcome[w[4]]+outcome[w[5]]+outcome[8])
    print("")
    print("Otoscopy: "+outcome[9])
    print("")
    print("Audiometry: "+outcome[10]+outcome[11]+outcome[12])
    print("")
    print("WDS: "+outcome[13])
    print("")
    print(outcome[14])
    print("")
    print(outcome[15]+outcome[16]+" - "+audiologist[0]+audiologist[1])

def outcomhtaud(x):
    rando= [2,3,4,5,6,7]
    w= random.sample(rando,len(rando))

    print("HT:"+outcome[1]+outcome[w[0]]+outcome[w[1]]+outcome[w[2]]+outcome[w[3]]+outcome[w[4]]+outcome[w[5]]+outcome[8])
    print("")
    print("Otoscopy: "+outcome[9])
    print("")
    print("Audiometry: "+outcome[10]+outcome[11]+outcome[12])
    print("")
    print("WDS: "+outcome[13])
    print("")
    print(outcome[14])
    print("")
    print(outcome[15]+outcome[16]+" - "+audiologist[0]+audiologist[1])
    print("")
    print("+++++AUDIOGRAM REPORT+++++")
    print("")
    print("Otoscopy: "+outcome[9])
    print("Audiometry: "+outcome[10]+outcome[12])
    print(outcome[14])
    print(outcome[15]+outcome[16]+" - "+audiologist[2])

nonbilateral = [False]
rightistrue = [False]

def rorl(x):
    print("Fitted: Right, left or bilateral?")
    print("1: Right")
    print("2: Left")
    print("3: Bilateral")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= "right "
        nonbilateral[0] = True
        rightistrue[0] = True
    if answ == "2":
        outcome[x]= "left "
        nonbilateral[0] = True
        rightistrue[0] = False
    if answ == "3":
        outcome[x]= "bilateral "
        nonbilateral[0] = False

def fitha(x):
    print("Hearing aid fitted?")
    print("1: Rexton KS 7")
    print("2: Phonak Brio 2R-312")
    print("3: Resound Cala 8")    
    print("4: ")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= "Rexton KS 7"
    if answ == "2":
        outcome[x]= "Phonak Brio 2R-312"
    if answ == "3":
        outcome[x]= "Resound Cala 8"
    if answ == "4":
        outcome[x]= ""
    if answ == "5":
        custom = input("Input Custom")
        outcome[x]= custom

def programs(x):
    print("Programs Included?")
    print("1: Automatic/Normal")
    print("2: ")
    print("3: ")    
    print("4: ")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= "1)Automatic/Normal"
    if answ == "2":
        outcome[x]= ""
    if answ == "3":
        outcome[x]= ""
    if answ == "4":
        outcome[x]= ""
    if answ == "5":
        custom = input("Input Custom")
        outcome[x]= custom

def controls(x):
    print("Manual Controls?")
    print("1: Volume Control")
    print("2: ")
    print("3: ")    
    print("4: ")
    print("5: Custom")
    ans = input()
    answ=chkabcde(ans,6)
    if answ == "1":
        outcome[x]= "Volume Control"
    if answ == "2":
        outcome[x]= ""
    if answ == "3":
        outcome[x]= ""
    if answ == "4":
        outcome[x]= ""
    if answ == "5":
        custom = input("Input Custom")
        outcome[x]= custom

def receivers(x):
    print("Length?")
    print("1: Length 1")
    print("2: Length 2")
    print("3: Length 3")
    print("4: Length 4")    
    print("5: Length 0")
    print("6: Custom")
    ans = input()
    answ=chkabcde(ans,7)    
    if answ == "1":
        inten="1"
    if answ == "2":
        inten="2"
    if answ == "3":
        inten ="3"
    if answ == "4":
        inten ="4"
    if answ == "5":
        inten = "0"
    if answ == "6":
        custom = input()
        inten = custom
    return inten


def gains(x):
    print("Enter adjustments done to match target:")
    outcome[x]= input()

def rece(x):
    if nonbilateral[0] == False:
        print("Right receiver?")
        right = receivers(0)
        powerr = input("Power?")
        domer = input("Dome?")
        print("Left receiver?")
        left = receivers(0)
        powerl = input("Power?")
        domel = input("Dome?")
        outcome[x]= "The receiver on the right is a #"+right+powerr+" with "+domer+" domes. The receiver on the left is a #" + left + powerl + " with "+domel+" domes."
    if nonbilateral[0] == True and rightistrue[0] == True:
        right = receivers(0)
        powerr = input("Power?")
        domer = input("Dome?")
        outcome[x]= "The receiver on the right is a #"+right+powerr+" with "+domer+" domes."
    if nonbilateral[0] == True and rightistrue[0] == False:
        right = receivers(0)
        powerr = input("Power?")
        domer = input("Dome?")
        outcome[x]= "The receiver on the left is a #"+right+powerr+" with "+domer+" domes."

def color(x):
    print("Color?")
    print("1: Pearl White")
    print("2: Silver")
    print("3: Gray")
    print("4: Granite")    
    print("5: Black")
    print("6: Beige")
    print("7: Medium Brown")
    print("8: Brown")
    print("9: Custom")
    ans = input()
    answ=chkabcde(ans,9)    
    if answ == "1":
        outcome[x]="pearl white colour"
    if answ == "2":
        outcome[x]="silver colour"
    if answ == "3":
        outcome[x] ="gray colour"
    if answ == "4":
        outcome[x] ="granite colour"
    if answ == "5":
        outcome[x] = "black colour"
    if answ == "6":
        outcome[x] = "beige colour"
    if answ == "7":
        outcome[x] = "medium brown colour"
    if answ == "8":
        outcome[x] = "brown colour"
    if answ == "9":
        custom = input()
        outcome[x] = custom

def ht(x):
    count[0]=0
    x={0:gender,
       1:accompany,
       2:consultent,
       3:surgeries,
       4:tinnitus,
       5:exposure,
       6:hlchange,
       7:prevha,
       8:cosi,
       9:otoscopy,
       10:loss,
       11:warrantsent,
       12:middleear,
       13:wds,
       14:quicksin,
       15:results,
       16:nextapptht}

    while count[0] < 17: 
        x[count[0]](count[0])
        count[0]+=1
    outcomht(0)

def htaud(x):
    count[0]=0
    x={0:gender,
       1:accompany,
       2:consultent,
       3:surgeries,
       4:tinnitus,
       5:exposure,
       6:hlchange,
       7:prevha,
       8:cosi,
       9:otoscopy,
       10:loss,
       11:warrantsent,
       12:middleear,
       13:wds,
       14:quicksin,
       15:results,
       16:nextapptht}

    while count[0] < 17: 
        x[count[0]](count[0])
        count[0]+=1
    outcomhtaud(0)

def outcomaud(x):
    print("Otoscopy: "+outcome[1])
    print("Audiometry: "+outcome[2]+outcome[3])
    print(outcome[4])
    print(outcome[5]+outcome[6]+" - "+audiologist[0]+audiologist[1])

def aud(x):
    count[0]=0
    x={0:gender,
       1:otoscopy,
       2:loss,
       3:middleear,
       4:quicksin,
       5:results,
       6:nextapptht
       }

    while count[0] < 7: 
        x[count[0]](count[0])
        count[0]+=1
    outcomaud(0)

def outcomfit(x):
    print("Fitting: "+namea[0]+" was fit with "+outcome[1]+outcome[2]+", "+outcome[3]+"."+outcome[4])
    print("RECD was measured today. NAL-NL2 was used to fit the hearing aids.")
    print("The following adjustments were done to match target; "+outcome[5])
    print("The following programs are in "+namea[0]+"’s hearing aids; "+outcome[6]+".")
    print("The following manual controls are activated: "+outcome[7]+".")
    print("Reviewed insertion – " +namea[0]+" did well. Counseled on operation of manual controls and smart remote app. Checked function during today’s appointment and working well. Practiced changing click domes and batteries.")
    print(outcome[8]+" No batteries were purchased today. - "+audiologist[0]+audiologist[1])

def fit(x):
    count[0]=0
    x={0:gender,
       1:rorl,
       2:fitha,
       3:color,
       4:rece,
       5:gains,
       6:programs,
       7:controls,
       8:nextapptfit,
        }

    while count[0] < 9: 
        x[count[0]](count[0])
        count[0]+=1
    outcomfit(0)


def smiley(x):
    behappy = random.randint(0,10)
    quotes = ["Difficult roads often lead to beautiful destinations.",
              "Be happy. Be bright. Be you!",
              "Happiness is found when you stop comparing yourself to other people.",
              "Be so happy that when others look at you, they become happy.",
              "Everyone wants happiness, no one wants pain. But you can't have a rainbow, without a little rain.",
              "There are so many beautiful reasons to be happy.",
              "You are gold. Solid gold.",
              "You can rock the world with your awesomeness.",
              "Sometimes I feel sad too,"+audiologist[0],
              "You are a kind and generous person "+audiologist[0],
              "Well I hope you start to feel better soon."
              ]
    return quotes[behappy]

def documentation(x):
    print("Upcoming-hearing aid parts customization? accessories?")
    print("      -MORE COWBELL erm I mean booleans... to minimize redundancy")

    print("v1.3  -major naming and pronoun update")
    print("      -running multiple reports on the same criteria (ht + aud)")
    print("      -report sentence order randomization")
    
    print("v1.2  -updated count list to be universal")
    print("      -MASSIVE bug squashed in checkabcde()...solves so many problems")    
    print("      -fitting reports are fully functional, require much fleshing out")     
    print("      -booleans in use")
    print("      -50% done randomization protocol")
    print("      -many MANY spelling mistakes fixed")
    print("      -1000 lines already, so inefficient")


    print("v1.1: -updated check function to allow as many inputs as desired")
    print("      -created main menu and recursive interface")
    print("      -created documentation and other secret feature")
    print("      -enabled custom inputs for majority of functions")
    print("      -25% done creating randomization of sentence outcome")     
    print("      -added audiometry option")
    print("      -5% done fitting reports") 

def stack(x):
    gender(1)
    namentro(2)
    accompany(3)
    outcomht(0)
    
    
def menu(x):
    print("")
    print("")
    print("***************************************")
    print("  Welcome to Audiologists Helper v1.3  ")
    print("         Developed by Matej Goc        ")
    print("***************************************")          
    print("Which report would you like to generate?")
    print("1: HT/HAE Report Only")
    print("2: HT/HAE + AUD Report")
    print("3: AUD Report Only")
    print("4: Fitting Report")    
    print("5: Follow up/ Service (In progress)")
    print("6: Documentation")
    print("7: I'm just feeling sad, Audiologists Helper...")
    ans = input()
    answ=chkabcde(ans,8)
    if answ == "1":
        ht(0)
    if answ == "2":
        htaud(0)
    if answ == "3":
        aud(0)
    if answ == "4":
        fit(0)
    if answ == "5":
        print("What part of not finished yet don't you understand "+audiologist[0]+"?")
    if answ == "6":
        documentation(0)
    if answ == "7":
        custom = smiley(0)
        print(custom)

def start(x):
    makemerunforever = x
    while makemerunforever >0:
        menu(0)
        makemerunforever-=1

start(100)
