class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.vol = 1
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
            self.canal -= 1
            self.vol -= 1

    def aumenta_canal(self):
        if self.ligada:
           self.canal += 1
    def diminui_canal(self):
        if self.ligada:
           self.canal -= 1

    def aumenta_vol(self):
        if self.ligada:
           self.vol += 1

    def diminui_vol(self):
        if self.ligada:
           self.vol -= 1

televisao = televisao()

print('televisa esta ligada?: {}'.format(televisao.ligada))
televisao.power()
print('televisa esta ligada?: {}'.format(televisao.ligada))
televisao.power()
print('televisa esta ligada?: {}'.format(televisao.ligada))
televisao.power()
print('televisa esta ligada?: {}'.format(televisao.ligada))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal:{}'. format(televisao.canal))
televisao.aumenta_canal()
print('Canal:{}'. format(televisao.canal))
televisao.diminui_canal()
televisao.aumenta_canal()
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal:{}'. format(televisao.canal))
televisao.aumenta_vol()
televisao.aumenta_vol()
print('volume:{}'.format(televisao.vol))
televisao.aumenta_vol()
print('volume:{}'.format(televisao.vol))
televisao.diminui_vol()
televisao.aumenta_vol()
print('volume:{}'.format(televisao.vol))
televisao.aumenta_vol()
print('volume:{}'.format(televisao.vol))
