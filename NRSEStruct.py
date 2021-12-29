import numpy as np
# from enum import Enum

# class Param(Enum):
#     robottype=0
#     jogacc=1
#     jogdec:2
#     jogjerk=3
#     jogstepvel=4
#     ataxisacc=5
#     ataxisdec=6
#     ataxisjerk=7
#     atlinemaxvel=8
#     atposemaxvel=9
#     atcoordacc=10
#     atcoorddec=11
#     atcoordjerk=12
#     fisrtcycvel=13
#     emergencysel=14
#     craftsel=15
#     enablesel=16
#     alpha=17
#     a=18
#     d=19
#     axisposlimit=20
#     axisneglimit=21
#     coordposlimit=22
#     coordneglimit=23
#     reductionratio=24
#     axislead=25
#     pulsepercir=26
#     motortorque=27
#     motormaxvel=28
#     jogaxismaxvel=29
#     jogcordmaxvel=30
#     atextmaxvel=31

axisnum: np.uint32 = 9
fmt='I' + 'd'*7 + 'd'*7 + 'd'*7 + 'f'*9 + 'f'*9 + 'f'*9 +\
    'f'*9 + 'f'*9 + 'f'*9 + 'd'*9 + 'd'*9 + 'f'*9 + 'f'*9 +\
    'f'*9 + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' +\
    'f' + 'f' + 'f'*3 + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H'

class Struct:
    robottype: np.uint32 = 0
    alpha = np.array([0] * 6, np.float64)
    a = np.array([0] * 6, np.float64)
    d = np.array([0] * 6, np.float64)

    axisposlimit = np.array([90] * axisnum, np.float32)
    axisneglimit = np.array([-90] * axisnum, np.float32)
    coordposlimit = np.array([9999] * axisnum, np.float32)
    coordneglimit = np.array([-9999] * axisnum, np.float32)
    reductionratio = np.array([1] * axisnum, np.float32)
    axislead = np.array([360] * axisnum, np.float32)

    pulsepercir = np.array([131072] * axisnum, np.float64)
    motortorque = np.array([0.32] * axisnum, np.float64)
    motormaxvel = np.array([3000] * axisnum, np.float32)

    jogaxismaxvel = np.array([60] * 3 + [120] * 3 + [60] * 3, np.float32)
    jogcordmaxvel = np.array([100] * axisnum, np.float32)
    jogacc: np.uint32 = 5
    jogdec: np.uint32 = 5
    jogjerk: np.uint32 = 8
    jogstepvel: np.uint32 = 30

    ataxisacc: np.uint32 = 5
    ataxisdec: np.uint32 = 5
    ataxisjerk: np.uint32 = 5
    atlinemaxvel: np.float32 = 2000
    atposemaxvel: np.float32 = 360
    atextmaxvel = np.array([360] * 3, np.float32)
    atcoordacc: np.uint32 = 5
    atcoorddec: np.uint32 = 5
    atcoordjerk: np.uint32 = 5
    fisrtcycvel: np.int32 = 10
    emergencysel: np.int32 = 0
    craftsel: np.int32 = 0
    enablesel: np.int32 = 0

# datastruct=Struct(fmt)
# packed=datastruct.pack(robottype, alpha[:], a[:], d[:],\
#     axisposlimit[:], axisneglimit[:], coordposlimit[:],\
#     coordneglimit[:], reductionratio[:], axislead[:],\
#     pulsepercir[:], motortorque[:], motormaxvel[:],\
#     jogaxismaxvel[:], jogcordmaxvel[:], jogacc, jogdec,\
#     jogjerk, jogstepvel, ataxisacc, ataxisdec,\
#     ataxisjerk, atlinemaxvel, atposemaxvel,\
#     atextmaxvel[:], atcoordacc, atcoorddec, atcoordjerk,\
#     fisrtcycvel, emergencysel, craftsel, enablesel)
# calcsize(packed)
