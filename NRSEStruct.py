from numpy import array, uint

axisnum: uint = 6 + 3
fmt='I' + 'd'*7 + 'd'*7 + 'd'*7 + 'f'*9 + 'f'*9 + 'f'*9 +\
    'f'*9 + 'f'*9 + 'f'*9 + 'd'*9 + 'd'*9 + 'f'*9 + 'f'*9 +\
    'f'*9 + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' +\
    'f' + 'f' + 'f'*3 + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H'

class Struct:
    def __init__(self):
        self.robottype: uint = 0
        self.alpha = array([0] * 6, 'd')
        self.a = array([0] * 6, 'd')
        self.d = array([0] * 6, 'd')

        self.axisposlimit = array([90] * axisnum, 'f')
        self.axisneglimit = array([-90] * axisnum, 'f')
        self.coordposlimit = array([9999] * axisnum, 'f')
        self.coordneglimit = array([-9999] * axisnum, 'f')
        self.reductionratio = array([1] * axisnum, 'f')
        self.axislead = array([360] * axisnum, 'f')

        self.pulsepercir = array([131072] * axisnum, 'f')
        self.motortorque = array([0.32] * axisnum, 'f')
        self.motormaxvel = array([3000] * axisnum, 'f')

        self.jogaxismaxvel = array([60] * 3 + [120] * 3 + [60] * 3, 'f')
        self.jogcordmaxvel = array([100] * axisnum, 'f')
        self.jogacc: uint = 5
        self.jogdec: uint = 5
        self.jogjerk: uint = 8
        self.jogstepvel: uint = 30

        self.ataxisacc: uint = 5
        self.ataxisdec: uint = 5
        self.ataxisjerk: uint = 5
        self.atlinemaxvel: float = 2000
        self.atposemaxvel: float = 360
        self.atextmaxvel = array([360] * 3, 'f')
        self.atcoordacc: uint = 5
        self.atcoorddec: uint = 5
        self.atcoordjerk: uint = 5
        self.fisrtcycvel: int = 10
        self.emergencysel: int = 0
        self.craftsel: int = 0
        self.enablesel: int = 0

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
