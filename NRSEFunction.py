from struct import unpack, pack
import numpy as np


class Struct:
    axisnum: np.uint = 9

    def __init__(self):
        self.robottype: np.uint = 0
        self.alpha = np.array([0] * 6, np.float64)
        self.a = np.array([0] * 6, np.float64)
        self.d = np.array([0] * 6, np.float64)
        self.axisposlimit = np.array([90] * self.axisnum, float)
        self.axisneglimit = np.array([-90] * self.axisnum, float)
        self.coordposlimit = np.array([9999] * self.axisnum, float)
        self.coordneglimit = np.array([-9999] * self.axisnum, float)
        self.reductionratio = np.array([1] * self.axisnum, float)
        self.axislead = np.array([360] * self.axisnum, float)
        self.pulsepercir = np.array([131072] * self.axisnum, np.float64)
        self.motortorque = np.array([0.32] * self.axisnum, np.float64)
        self.motormaxvel = np.array([3000] * self.axisnum, float)
        self.jogaxismaxvel = np.array([60] * 3 + [120] * 3 + [60] * 3, float)
        self.jogcordmaxvel = np.array([100] * self.axisnum, float)
        self.jogacc: np.uint = 5
        self.jogdec: np.uint = 5
        self.jogjerk: np.uint = 8
        self.jogstepvel: np.uint = 30
        self.ataxisacc: np.uint = 5
        self.ataxisdec: np.uint = 5
        self.ataxisjerk: np.uint = 5
        self.atlinemaxvel: float = 2000
        self.atposemaxvel: float = 360
        self.atextmaxvel = np.array([360] * 3, float)
        self.atcoordacc: np.uint = 5
        self.atcoorddec: np.uint = 5
        self.atcoordjerk: np.uint = 5
        self.fisrtcycvel: int = 10
        self.emergencysel: int = 0
        self.craftsel: int = 0
        self.enablesel: int = 0
        return


class NRSEFunction:

    file = ''
    data = Struct()
    fmt = 'I' + 'd' * 7 + 'd' * 7 + 'd' * 7 + 'f' * 9 + \
        'f' * 9 + 'f' * 9 + 'f' * 9 + 'f' * 9 + 'f' * 9 + \
        'd' * 9 + 'd' * 9 + 'f' * 9 + 'f' * 9 + 'f' * 9 + \
        'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'f' + \
        'f' + 'f' * 3 + 'H' + 'H' + 'H' + 'H' + 'H' + 'H' + 'H'

    def read(self, file):
        self.file = file

        with open(self.file, 'rb') as f:
            datalen = unpack("@I", f.read(4))

        if datalen[0] != 696:
            return False

        with open(self.file, 'rb') as f:
            f.seek(6)
            data = unpack('@' + self.fmt, f.read(694))

        i = 0
        j = i + 1
        self.data.robottype = data[i:j]

        i = j
        j = i + 7
        self.data.alpha = data[i:j]

        i = j
        j = i + 7
        self.data.a = data[i:j]

        i = j
        j = i + 7
        self.data.d = data[i:j]

        i = j
        j = i + 9
        self.data.axisposlimit = data[i:j]

        i = j
        j = i + 9
        self.data.axisneglimit = data[i:j]

        i = j
        j = i + 9
        self.data.coordposlimit = data[i:j]

        i = j
        j = i + 9
        self.data.coordneglimit = data[i:j]

        i = j
        j = i + 9
        self.data.reductionratio = data[i:j]

        i = j
        j = i + 9
        self.data.axislead = data[i:j]

        i = j
        j = i + 9
        self.data.pulsepercir = data[i:j]

        i = j
        j = i + 9
        self.data.motortorque = data[i:j]

        i = j
        j = i + 9
        self.data.motormaxvel = data[i:j]

        i = j
        j = i + 9
        self.data.jogaxismaxvel = data[i:j]

        i = j
        j = i + 9
        self.data.jogcordmaxvel = data[i:j]

        i = j
        j = i + 1
        self.data.jogacc = data[i:j]

        i = j
        j = i + 1
        self.data.jogdec = data[i:j]

        i = j
        j = i + 1
        self.data.jogjerk = data[i:j]

        i = j
        j = i + 1
        self.data.jogstepvel = data[i:j]

        i = j
        j = i + 1
        self.data.ataxisacc = data[i:j]

        i = j
        j = i + 1
        self.data.ataxisdec = data[i:j]

        i = j
        j = i + 1
        self.data.ataxisjerk = data[i:j]

        i = j + 1
        j = i + 1
        self.data.atlinemaxvel = data[i:j]

        i = j
        j = i + 1
        self.data.atposemaxvel = data[i:j]

        i = j
        j = i + 3
        self.data.atextmaxvel = data[i:j]

        i = j
        j = i + 1
        self.data.atcoordacc = data[i:j]

        i = j
        j = i + 1
        self.data.atcoorddec = data[i:j]

        i = j
        j = j + 1
        self.data.atcoordjerk = data[i:j]

        i = j
        j = i + 1
        self.data.fisrtcycvel = data[i:j]

        i = j
        j = i + 1
        self.data.emergencysel = data[i:j]

        i = j
        j = i + 1
        self.data.craftsel = data[i:j]

        i = j
        j = i + 1
        self.data.enablesel = data[i:j]
        return True

    def write(self, file=''):
        if file != '':
            self.file = file
        else:
            file = self.file

        data = []
        i = 0
        j = i + 1
        data[i:j] = list([self.data.robottype])

        i = j
        j = i + 7
        data[i:j] = list(self.data.alpha)

        i = j
        j = i + 7
        data[i:j] = list(self.data.a)

        i = j
        j = i + 7
        data[i:j] = list(self.data.d)

        i = j
        j = i + 9
        data[i:j] = list(self.data.axisposlimit)

        i = j
        j = i + 9
        data[i:j] = list(self.data.axisneglimit)

        i = j
        j = i + 9
        data[i:j] = list(self.data.coordposlimit)

        i = j
        j = i + 9
        data[i:j] = list(self.data.coordneglimit)

        i = j
        j = i + 9
        data[i:j] = list(self.data.reductionratio)

        i = j
        j = i + 9
        data[i:j] = list(self.data.axislead)

        i = j
        j = i + 9
        data[i:j] = list(self.data.pulsepercir)

        i = j
        j = i + 9
        data[i:j] = list(self.data.motortorque)

        i = j
        j = i + 9
        data[i:j] = list(self.data.motormaxvel)

        i = j
        j = i + 9
        data[i:j] = list(self.data.jogaxismaxvel)

        i = j
        j = i + 9
        data[i:j] = list(self.data.jogcordmaxvel)

        i = j
        j = i + 1
        data[i:j] = list([self.data.jogacc])

        i = j
        j = i + 1
        data[i:j] = list([self.data.jogdec])

        i = j
        j = i + 1
        data[i:j] = list([self.data.jogjerk])

        i = j
        j = i + 1
        data[i:j] = list([self.data.jogstepvel])

        i = j
        j = i + 1
        data[i:j] = list([self.data.ataxisacc])

        i = j
        j = i + 1
        data[i:j] = list([self.data.ataxisdec])

        i = j
        j = i + 1
        data[i:j] = list([self.data.ataxisjerk])

        i = j
        j = i + 1
        data[i:j] = list([0])

        i = j
        j = i + 1
        data[i:j] = list([self.data.atlinemaxvel])

        i = j
        j = i + 1
        data[i:j] = list([self.data.atposemaxvel])

        i = j
        j = i + 3
        data[i:j] = list(self.data.atextmaxvel)

        i = j
        j = i + 1
        data[i:j] = list([self.data.atcoordacc])

        i = j
        j = i + 1
        data[i:j] = list([self.data.atcoorddec])

        i = j
        j = j + 1
        data[i:j] = list([self.data.atcoordjerk])

        i = j
        j = i + 1
        data[i:j] = list([self.data.fisrtcycvel])

        i = j
        j = i + 1
        data[i:j] = list([self.data.emergencysel])

        i = j
        j = i + 1
        data[i:j] = list([self.data.craftsel])

        i = j
        j = i + 1
        data[i:j] = list([self.data.enablesel])

        with open(file, 'wb') as f:
            f.write(pack('@I', 696))
            f.write(pack('@2s', '\r\n'.encode('utf-8')))
            f.seek(6)
            for i in range(len(data)):
                f.write(pack('>' + self.fmt[i], data[i]))
            f.write(pack('@6s', 'TEND\r\n'.encode('utf-8')))
        return True

    def close(self):
        if self.file == '':
            return

        try:
            open(self.file)
        except Exception:
            if ('[Errno 13] Permission denied' in str(Exception)):
                self.file.close()
        else:
            self.file.close()
        finally:
            return
