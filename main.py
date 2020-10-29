def ruleKhusus(data):
    dictRule = {'ruleA':['b'],
                'ruleE':['y','f','m','p','s'],
                'ruleI':['b','r'],
                'ruleO':['b','c','y'],
                'ruleQ':['y'],
                'ruleR':['n'],
                'ruleS':['l','n'],
                'ruleT':['r']
                }
    if(data[0] in dictRule['ruleA'] or data[4] in dictRule['ruleE']
    or data[8] in dictRule['ruleI'] or data[14] in dictRule['ruleO']
    or data[16] in dictRule['ruleQ'] or data[17] in dictRule['ruleR']
    or data[18] in dictRule['ruleS'] or data[19] in dictRule['ruleT']):
        return True
    else:
        return False

def numeric(dataInput):
    dictNumeric = {1:{'b':0.11,'c':1,'x':0.47,'f':0.49,'k':0.72,'s':0},
                2:{'f':0.33,'g':1,'y':0.54,'s':0.55},
                3:{'n':0.45,'b':0.71,'c':0.27,'g':0.44,'r':0,'p':0.61,'u':0,'e':0.58,'w':0.31,'y':0.63},
                4:{'t':0.18,'f':0.69},
                5:{'a':0,'l':0,'c':1,'y':1,'f':1,'m':1,'n':0.03,'p':1,'s':1},
                6:{'a':0.09,'d':0,'f':0.49,'n':0},
                7:{'c':0.56,'w':0.09,'d':0},
                8:{'b':0.3,'n':0.89},
                9:{'k':0.16,'n':0.11,'b':1,'h':0.72,'g':0.67,'r':1,'o':0,'p':0.43,'u':0.1,'e':0,'w':0.2,'y':0.26},
                10:{'e':0.54,'t':0.44},
                11:{'b':0.49,'c':0.08,'u':0,'e':0.23,'z':0,'r':0,'?':0.71},
                12:{'f':0.26,'y':0.33,'k':0.94,'s':0.3},
                13:{'f':0.24,'y':0.27,'k':0.94,'s':0.31},
                14:{'n':0.96,'b':1,'c':1,'g':0,'o':0,'p':0.69,'e':0,'w':0.38,'y':1},
                15:{'n':0.88,'b':1,'c':1,'g':0,'o':0,'p':0.69,'e':0,'w':0.38,'y':1},
                16:{'p':0.48,'u':0},
                17:{'n':0,'o':0,'w':0.49,'y':1},
                18:{'n':1,'o':0.51,'t':0.12},
                19:{'c':0,'e':0.64,'f':0,'l':1,'n':1,'p':0.21,'s':0,'z':0},
                20:{'k':0.12,'n':0.11,'b':0,'h':0.97,'r':1,'o':0,'u':0,'w':0.76,'y':0},
                21:{'a':0,'c':0.15,'n':0,'s':0.29,'v':0.7,'y':0.38},
                22:{'g':0.34,'l':0.71,'m':0.12,'p':0.88,'u':0.74,'w':0,'d':0.4}
                }
    # print(len(dataInput))
    dataBaru = []
    for i in range(len(dataInput)):
        dataBaru.append(dictNumeric[i+1][dataInput[i]])

    # print(dictNumeric['A']['k'])
    return dataBaru

def RUN():
    # data = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
    data = ['x','f','n','f','n','f','w','b','n','t','e','s','f','w','w','p','w','o','e','k','a','g']
    hasil = ""
    if(ruleKhusus(data)==True):
        hasil ="Beracun"
    else:
        dataBaru = numeric(data)
        print(dataBaru)



if __name__ == '__main__':
    RUN()