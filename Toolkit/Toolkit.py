import numpy as np

def mean(val, na='False'):
    if na == 'False':
        s = sum(val)
        sl = len(val)
        return (s / sl)
    else:
        num = []
        for v in val:
            try:
                float(v)
                num.append(float(v))
            except:
                print('empty cell')
        s = sum(num)
        sl = len(num)
        if sl == 0:
            return('')
        else:
            return(s/sl)

def adjust(dat, val):
    hold = []
    for d in dat:
        hold.append(float(d) + val)
    return(hold)

def which(val, compare): # This will search for an exact matching string in a list
    rw = -1
    fw = "No Match"
    for v in val:
        rw = rw + 1
        if str(v).find(str(compare)) != -1:
            print("Match found")
            fw = rw
            break
    return (fw)


def Decrapify(va): # This removes useless shit from a string
    if type(va) is str:
        va = str(va)
        va = va.replace("'", "")
        va = va.replace('"', "")
        va = va.replace('[', '')
        va = va.replace(']', '')
        va = va.replace('\n', '')
        return (va)
    else:
        hd = []
        for v in va:
            v = str(v)
            v = v.replace("'", "")
            v = v.replace('"', "")
            v = v.replace('[', '')
            v = v.replace(']', '')
            v = v.replace('\n', '')
            hd.append(v)
        return (hd)

def readCSV(dr): # This reads in a csv file
    with open(dr, 'r') as file:
        next(file)
        ct = -1
        for row in file:
            ct = ct + 1
            if ct==0:
                hold = np.empty([10000000, len(str(row).split(","))], dtype=object)
                hold[ct,:] =  str(row).split(',')
            else:
                hold[ct, :] = str(row).split(',')
    file.close()
    hd = hold[0:ct,]
    return(hd)


def converter(data, format): # This dates an array of dats and converts them to a given format
    holder = []
    for d in data:
        holder.append(format(d))
    return holder

# Remove leading zeros from a data

def zeroRM(dat, delim):
    bdlist = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
    gdlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ls = []
    sts = str(dat)
    for b in range(0,len(bdlist)):
        for p in range(0,3): # this messes with the position of the '/'
            if p == 0:
                bd = ''.join([bdlist[b],'/'])
                gd = ''.join([gdlist[b], '/'])
            if p == 1:
                bd = ''.join(['/', bdlist[b]])
                gd = ''.join(['/', gdlist[b]])
            if p == 2:
                bd = ''.join([bdlist[b], ':'])
                gd = ''.join([gdlist[b], ':'])
            sts = str(sts).replace(bd, gd)
    ls.append(str(sts))
    return(ls)

def dirFlip(dr):
    st = str(dr).replace('\\','/')
    return(st)

def listSub(ls1, ls2):
    dif = []
    for l in range(0,len(ls2),1):
        dif.append(float(ls1[l]) - float(ls2[l]))
    return(dif)

def isNum(val):
    try:
        val = abs(val)
        val = str(val).replace(".",'')
        if str(val).isdigit() ==  True:
            return(True)
        else:
            return(False)
    except:
        return(False)

