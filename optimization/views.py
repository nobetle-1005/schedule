from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request,"index.html")

# Create your views here.
from pulp import *
def result(request):
    prob = LpProblem("BAVU_AR",LpMinimize)
    DrAd  =  ["Emine", "Harun", "Selcuk", "Ismail",
            "Hakki", "Zehra", "Betul", "Zeynep", "Rabia",
            "Shainaz", "Celal", "Pervin", "Hazan", "Ayse",
            "Tural", "Zeynepnur"]
    NofDr = len(DrAd)
    DrID  = range(0,len(DrAd))
    DrDict2 ={}
    j=0
    for i in DrAd:
        DrDict2[i] = DrID[j]
        j=j+1
    T      = 28
    SP     = 0
    Dr     = DrAd #Dr'lari simdilik numara ile tutuyorum. 
    Days   = range(SP,T+SP)
    WEDays = [1,7,8,14,15,21,22,28] #haftasonu gunleri
    Fridays= [6,13,20,27] #haftasonu gunleri
    SwF    = [8,15,22]
    for i in range(0,len(WEDays)):
        WEDays[i] = WEDays[i]-1
    for i in range(0,len(Fridays)):
        Fridays[i] = Fridays[i]-1
    for i in range(0,len(SwF)):
        SwF[i] = SwF[i]-1
    deltaT       = 0
    deltaTminus1 = 0
    Loc  = ["ICU1", "ICU2", "SR"]
    T1   = range(SP,T-1+SP)
    T2   = range(SP,T-2+SP)
    SwFChoose={}
    SwFChooseTemp   = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(0,NofDr):

        SwFChoose[Dr[i]] = SwFChooseTemp[i]
    FridayShiftsTemp  = [0 for a in Dr]
    WEShiftsTemp      = [0 for a in Dr]
    TotalShiftsTemp   = [0 for a in Dr]
    SatShiftsTemp     = [0 for a in Dr]
    SanShiftsTemp     = [0 for a in Dr]
    FridayShifts ={}
    WEShifts ={}
    TotalShifts ={}
    FridayShifts["Emine"] = 1
    FridayShifts["Harun"] = 0
    FridayShifts["Selcuk"] = 1
    FridayShifts["Ismail"] = 1
    FridayShifts["Hakki"] = 1
    FridayShifts["Zehra"] = 0
    FridayShifts["Betul"] = 1
    FridayShifts["Zeynep"] = 0
    FridayShifts["Rabia"] = 1
    FridayShifts["Shainaz"] = 1
    FridayShifts["Celal"] = 1
    FridayShifts["Pervin"] = 0
    FridayShifts["Hazan"] = 1
    FridayShifts["Ayse"] = 1
    FridayShifts["Tural"] = 1
    FridayShifts["Zeynepnur"] = 1
    TotalShifts["Emine"] = 4
    TotalShifts["Harun"] = 4
    TotalShifts["Selcuk"] = 4
    TotalShifts["Ismail"] = 4
    TotalShifts["Hakki"] = 4
    TotalShifts["Zehra"] = 0
    TotalShifts["Betul"] = 4
    TotalShifts["Zeynep"] = 2
    TotalShifts["Rabia"] = 7
    TotalShifts["Shainaz"] = 8
    TotalShifts["Celal"] = 8
    TotalShifts["Pervin"] = 0
    TotalShifts["Hazan"] = 8
    TotalShifts["Ayse"] =9
    TotalShifts["Tural"] = 9
    TotalShifts["Zeynepnur"] = 9
    WEShifts["Emine"] = 1
    WEShifts["Harun"] = 1
    WEShifts["Selcuk"] = 1
    WEShifts["Ismail"] = 1
    WEShifts["Hakki"] = 1
    WEShifts["Zehra"] = 0
    WEShifts["Betul"] = 1
    WEShifts["Zeynep"] = 1
    WEShifts["Rabia"] = 2
    WEShifts["Shainaz"] = 2
    WEShifts["Celal"] = 2
    WEShifts["Pervin"] = 0
    WEShifts["Hazan"] = 2
    WEShifts["Ayse"] = 3
    WEShifts["Tural"] = 3
    WEShifts["Zeynepnur"] = 3
    InfLoc ={}
    InfLoc["Emine"]     = ['SR']
    InfLoc["Harun"]     = ['SR']
    InfLoc["Selcuk"]    = ['SR']
    InfLoc["Ismail"]    = ['SR']
    InfLoc["Hakki"]     = ['SR']
    InfLoc["Zehra"]     = ['SR', 'ICU1']
    InfLoc["Betul"]     = ['SR']
    InfLoc["Zeynep"]    = []
    InfLoc["Rabia"]     = ['SR']
    InfLoc["Shainaz"]   = []
    InfLoc["Celal"]     = []
    InfLoc["Pervin"]    = ['SR', 'ICU1']
    InfLoc["Hazan"]     = []
    InfLoc["Ayse"]      = []
    InfLoc["Tural"]     = ['ICU1',"ICU2"]
    InfLoc["Zeynepnur"] = ['ICU1',"ICU2"]
    ONDays   = {}
    for i in ONDays:
        for j in range(0,len(ONDays[i])):
            ONDays[i][j] =  ONDays[i][j]-1
    MustDays     = {'Zeynep': [19,28],
                    'Ayse':[28],
                    'Emine':[10, 13,15 ]}
    for i in MustDays:
        for j in range(0,len(MustDays[i])):
            MustDays[i][j] =  MustDays[i][j]-1
    VacationDays = {'Selcuk':[1,13,14,15,16,17,18,19,20,21,22,23],
                    'Rabia':[1,2,3,4,5,6,7,8,9],
                    'Emine': [18,19,20,21,22],
                    'Harun': [7,14,21,28],
                    'Ismail':[11,12,13,14,15,27,28],
                    'Hakki': [20,21,22],
                    'Betul': [1,20,21,22,23],
                    'Celal': [9,10,11,12,13,14,15],
                    'Ayse': [7,8,15],
                    'Zeynepnur': [1,20,21,22]}
    for i in VacationDays:
        for j in range(0,len(VacationDays[i])):
            VacationDays[i][j] =  VacationDays[i][j]-1
    OFFDays      ={ }
    for i in OFFDays:
        for j in range(0,len(OFFDays[i])):
            OFFDays[i][j] =  OFFDays[i][j]-1
    SGN = ['Ayse', 'Betul','Tural']
    EGN = []
    CofWEPos = {}
    CofWENeg = {}
    CofFriPos = {}
    CofFriNeg = {}
    CofSatPos = {}
    CofSatNeg = {}
    CofSunPos = {}
    CofSunNeg = {}

    CofSwFPos = {}
    CofSwFNeg = {}
    CofTanPos = {}
    CofOFFPos = {}
    CofOFFNeg = {}
    CofONPos  = {}
    CofONNeg  = {}


    CofLocPos = {}
    CofLocNeg = {}
    for i in Dr:
        CofFriPos[i] = 5.4
        CofFriNeg[i] = 5.4
        CofSatPos[i] = 1
        CofSatNeg[i] = 1
        CofSunPos[i] = 1
        CofSunNeg[i] = 1
        for t in Days:
            CofSwFPos[i,t] = 5.2
            CofSwFNeg[i,t] = 5.2
            CofTanPos[i,t] = 1.9
            CofOFFPos[i,t] = 14.4
            CofOFFNeg[i,t] = 14.4
            CofONPos[i,t]  = 4
            CofONNeg[i,t]  = 4
    ShiftVar = LpVariable.dicts("X",(Dr,Days,Loc),
                            lowBound=0,
                            upBound=1,
                            cat=pulp.LpInteger)
    DevLocPos = LpVariable.dicts("DevLocPos",(Dr,Loc),
                            lowBound=0,
                            cat=pulp.LpContinuous)
    DevLocNeg = LpVariable.dicts("DevLocNeg",(Dr,Loc),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevWEPos  = LpVariable.dicts("DevWEPos",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevWENeg  = LpVariable.dicts("DevWENeg",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevFriPos = LpVariable.dicts("DevFriPos",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevFriNeg = LpVariable.dicts("DevFriNeg",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevSatPos = LpVariable.dicts("DevSatPos",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevSatNeg = LpVariable.dicts("DevSatNeg",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevSunPos = LpVariable.dicts("DevSunPos",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevSunNeg = LpVariable.dicts("DevSunNeg",(Dr),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevSwFPos = LpVariable.dicts("DevSwFPos",(Dr,Days),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevSwFNeg = LpVariable.dicts("DevSwFNeg",(Dr,Days),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevTanPos = LpVariable.dicts("DevTanPos",(Dr,Days),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevOFFPos = LpVariable.dicts("DevOFFPos",(Dr,Days),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    DevONNeg = LpVariable.dicts("DevONNeg",(Dr,Days),
                           lowBound=0,
                           cat=pulp.LpContinuous)
    prob += lpSum([CofFriPos[i]*DevFriPos[i] for i in Dr ]
                + [CofFriNeg[i]*DevFriNeg[i] for i in Dr ]
    + [CofOFFPos[i,t]*DevOFFPos[i][t] for i in Dr for t in Days]
    + [CofONNeg[i,t]*DevONNeg[i][t] for i in Dr for t in Days]
    + [CofSwFPos[i,t]*DevSwFPos[i][t] for i in Dr for t in Days]
    + [CofSwFNeg[i,t]*DevSwFNeg[i][t] for i in Dr for t in Days]
    + [CofTanPos[i,t]*DevTanPos[i][t] for i in Dr for t in Days]), ""
    for i in InfLoc:
        for l in InfLoc[i]:
            prob += lpSum([ShiftVar[i][t][l] for t in Days ]) == 0, ""
    for i in Dr:
        for t in Days:
            prob += lpSum([ShiftVar[i][t][l] for l in Loc])   <= 1, ""
    for t in Days:
        prob += lpSum([ShiftVar[i][t]["ICU1"] for i in Dr]) == 1, ""
    for t in Days:
        prob += lpSum([ShiftVar[i][t]["ICU2"] for i in Dr]) == 1, ""
    for t in Days:
        prob += lpSum([ShiftVar[i][t]["SR"] for i in Dr]) >= 0, ""
    for t in Days:
        prob += lpSum([ShiftVar[i][t]["SR"] for i in Dr]) <= 1, ""
    for i in Dr:
        prob += lpSum([ShiftVar[i][t][l] for t in Days for l in Loc])  == TotalShifts[i], ""
    for i in Dr:
        prob += lpSum([ShiftVar[i][t][l] for t in WEDays for l in Loc])   == WEShifts[i], ""
    for i in Dr:
        prob += lpSum([ShiftVar[i][t][l]  for t in Fridays for l in Loc])-DevFriPos[i] + DevFriNeg[i]  == FridayShifts[i], ""



    for i in Dr:
        for t in T1:
            prob += lpSum([ShiftVar[i][t][l] + ShiftVar[i][t+1][l] for l in Loc])  <= 1, ""
    for i in SGN:
        prob += lpSum([ShiftVar[i][Days[0+SP]][l]  for l in Loc])  == 0, ""
    for i in Dr:
        for t in T2:
            if t not in SwF:
                prob += lpSum([ShiftVar[i][t][l] + ShiftVar[i][t+1][l]+
                        ShiftVar[i][t+2][l] for l in Loc]) -DevTanPos[i][t]  <= 1, ""
    for i in SGN:
        if t not in SwF:
            prob += lpSum([ShiftVar[i][Days[0+SP]][l]+
                    ShiftVar[i][Days[1+SP]][l] for l in Loc])-DevTanPos[i][t]   == 0, ""
    for i in EGN:
        if t not in SwF:
            prob += lpSum([ShiftVar[i][Days[0+SP]][l] for l in Loc])-DevTanPos[i][t] == 0, ""
    for i in Dr:
        for t in SwF:
            prob += lpSum([ShiftVar[i][t-2][l]*SwFChoose[i]  - ShiftVar[i][t][l]*SwFChoose[i]
                        for l in Loc]) -DevSwFPos[i][t]   <= 0, ""
    if deltaT ==1:
        for i in SGN:
            prob += lpSum([ShiftVar[i][Days[1+SP]][l] for l in Loc]) + DevSwFNeg[i][t]  == 1, ""
    if deltaTminus1 ==1:
        for i in SGN:
            prob += lpSum([ShiftVar[i][Days[0+SP]][l] for l in Loc]) + DevSwFNeg[i][t]  == 1, ""
    for i in VacationDays:
        for t in VacationDays[i]:
            prob += lpSum([ShiftVar[i][t][l] for l in Loc ]) == 0, ""


    for i in MustDays:
        for t in MustDays[i]:
            prob += lpSum([ShiftVar[i][t][l] for l in Loc ])  == 1, ""
    for i in OFFDays:
        for t in OFFDays[i]:
            prob += lpSum([ShiftVar[i][t][l] for l in Loc ]) - DevOFFPos[i][t] == 0, ""
    for i in ONDays:
        for t in ONDays[i]:
            prob += lpSum([ShiftVar[i][t][l] for l in Loc ])  + DevONNeg[i][t] == 1, ""
    prob.writeLP("BAVU.lp")
    prob.solve()
    f = open('Guray.txt', 'w')
    f.write('Bezmialem Anestezi ve Yogun Bakim Nobet Cizelgesi\n')
    if LpStatus[prob.status]=='Infeasible':
        f.write('Maalesef uygun bir cozum bulamadim, nobet sayilarini degistirip tekrar deneyin\n\n')
    elif LpStatus[prob.status]=='Optimal':
        f.write('OPTIMAL cozumu buldum! \n\n')
    liste=[]
    for t in Days:
        Temp = Days[t]+1
        f.write("%s\t" % Temp )
        for l in Loc:
            for i in Dr:
                if ShiftVar[i][t][l].value() == 1:
                    f.write("%s\t" % i )
                    liste.append([i])
        f.write("\n")
        
    subat=range(0,29)
    f.close()
    def group(lst, n):
        for i in range(0, len(lst), n):
            val = lst[i:i+n]
            if len(val) == n:
                yield tuple(val)
    liste=list(group(liste, 3))

    context={
        "liste":liste
    }
    messages.success(request,"Çizelge Oluşturuldu")

    return render(request,"result.html",context)
