class Emosi(object):
    def __init__(self, emosi):
        self.emosi = emosi

    def santai(self):
        if self.emosi <= 20:
            return 1
        elif 20 < self.emosi < 35:
            return -(self.emosi - 35) / (35 - 20)
        else:
            return 0

    def biasa(self):
        if self.emosi <= 20 or self.emosi >= 70:
            return 0
        elif 20 < self.emosi < 35:
            return (self.emosi - 20) / (35 - 20)
        elif 35 <= self.emosi <= 60:
            return 1
        else:
            return -(self.emosi - 70) / (70 - 60)

    def marah(self):
        if self.emosi <= 60:
            return 0
        elif 60 < self.emosi < 70:
            return (self.emosi - 60) / (70 - 60)
        else:
            return 1


class Provokasi(object):
    def __init__(self, provokasi):
        self.provokasi = provokasi

    def sedikit(self):
        if self.provokasi <= 15:
            return 1
        elif 15 < self.provokasi < 30:
            return -(self.provokasi - 30) / (30 - 15)
        else:
            return 0

    def sedang(self):
        if self.provokasi <= 15 or self.provokasi >= 75:
            return 0
        elif 15 < self.provokasi < 30:
            return (self.provokasi - 15) / (30 - 15)
        elif 30 <= self.provokasi <= 65:
            return 1
        else:
            return -(self.provokasi - 75) / (75 - 65)

    def banyak(self):
        if self.provokasi <= 65:
            return 0
        elif 65 < self.provokasi < 75:
            return (self.provokasi - 65) / (75 - 65)
        else:
            return 1


def defuzzification(tidakHoax, hampirHoax, hoaxBanget):
    return ((tidakHoax * 20) + (hampirHoax * 50) + (hoaxBanget * 70))


def statusHoax():
    if defuzzification(tidakHoax, hampirHoax, hoaxBanget) > 50:
        return 'HOAX'
    else:
        return 'Tidak'


emo = Emosi(100)
pro = Provokasi(99)

th1 = min(emo.santai(), pro.sedikit())
th2 = min(emo.santai(), pro.sedang())
th3 = min(emo.biasa(), pro.sedikit())
tidakHoax = max(th1, th2, th3)

hh1 = min(emo.marah(), pro.sedikit())
hh2 = min(emo.biasa(), pro.sedang())
hampirHoax = max(hh1, hh2)

hb1 = min(emo.santai(), pro.banyak())
hb2 = min(emo.biasa(), pro.banyak())
hb3 = min(emo.marah(), pro.sedang())
hb4 = min(emo.marah(), pro.banyak())
hoaxBanget = max(hb1, hb2, hb3, hb4)


print(th1, th2, th3, hh1, hh2, hb1, hb2, hb3, hb4)

print('Emosi        :', emo.emosi)
print('Provokasi    :', pro.provokasi)
print('Tidak Hoax   :', tidakHoax)
print('Hampir Hoax   :', hampirHoax)
print('Hoax Banget  :', hoaxBanget)
print('Index hoax   :', defuzzification(tidakHoax, hampirHoax, hoaxBanget))
print('Status hoax  :', statusHoax())
