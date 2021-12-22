from struct import unpack
import NRSEStruct

struct=NRSEStruct.Struct()


def read(file):
    with open(file, 'rb') as f:
        datalen = unpack("@I", f.read(4))

    if datalen[0] != 696:
        return False,struct

    with open(file, 'rb') as f:
        f.seek(6)
        data = unpack('@' + NRSEStruct.fmt, f.read(694))

    i = 0; j = i + 1
    struct.robottype = data[i:j]

    i = j; j = i + 7
    struct.alpha = data[i:j]

    i = j; j = i + 7
    struct.a = data[i:j]

    i = j; j = i + 7
    struct.d = data[i:j]

    i = j; j = i + 9
    struct.axisposlimit = data[i:j]

    i = j; j = i + 9
    struct.axisneglimit = data[i:j]

    i = j; j = i + 9
    struct.coordposlimit = data[i:j]

    i = j; j = i + 9
    struct.coordneglimit = data[i:j]

    i = j; j = i + 9
    struct.reductionratio = data[i:j]

    i = j; j = i + 9
    struct.axislead = data[i:j]

    i = j; j = i + 9
    struct.pulsepercir = data[i:j]

    i = j; j = i + 9
    struct.motortorque = data[i:j]

    i = j; j = i + 9
    struct.motormaxvel = data[i:j]

    i = j; j = i + 9
    struct.jogaxismaxvel = data[i:j]

    i = j; j = i + 9
    struct.jogcordmaxvel = data[i:j]

    i = j + 1; j = i + 1
    struct.jogacc = data[i:j]

    i = j; j = i + 1
    struct.jogdec = data[i:j]

    i = j; j = i + 1
    struct.jogjerk = data[i:j]

    i = j; j = i + 1
    struct.jogstepvel = data[i:j]

    i = j; j = i + 1
    struct.ataxisacc = data[i:j]

    i = j; j = i + 1
    struct.ataxisdec = data[i:j]

    i = j; j = i + 1
    struct.ataxisjerk = data[i:j]

    i = j; j = i + 1
    struct.atlinemaxvel = data[i:j]

    i = j; j = i + 1
    struct.atposemaxvel = data[i:j]

    i = j; j = i + 3
    struct.atextmaxvel = data[i:j]

    i = j; j = i + 1
    struct.atcoordacc = data[i:j]

    i = j; j = i + 1
    struct.atcoorddec = data[i:j]

    i = j; j = j + 1
    struct.atcoordjerk = data[i:j]

    i = j; j = i + 1
    struct.fisrtcycvel = data[i:j]

    i = j; j = i + 1
    struct.emergencysel = data[i:j]

    i = j; j = i + 1
    struct.craftsel = data[i:j]

    i = j; j = i + 1
    struct.enablesel = data[i:j]
    return True,struct


def write(dataunpacked):
    file = r"D:\SysParam1.txt"
    with open(file, 'w') as f:
        for _ in dataunpacked:
            #f.writelines(str.format('%.2f' % _)+'\n')
            f.writelines(str(_) + '\n')


def editorhelp():
    print('help')


def editorabout():
    print('about')


def filenew():
    print('new')


def filesave():
    print('save')


def filesaveas():
    print("saveas")


def fileclose():
    print('close')
