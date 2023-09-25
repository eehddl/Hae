# 31번
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 출력(self):
        print("car.바퀴\n {0}".format(self.바퀴))
        print("car. 가격\n {0}".format(self.가격))

car = 차(2,1000)
car.출력()

# 32번
class 자전차(차):
    def __init__(self, 바퀴, 가격):
        차.__init__(self, 바퀴, 가격)

# 33번
    def 출력(self):
        print("bicycle.가격\n {0}".format(self.가격))

bicycle = 자전차(2, 100)
bicycle.출력()

# 34번
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        차.__init__(self, 바퀴, 가격)
        self.구동계 = 구동계

    def 출력(self):
        print("bicycle.구동계\n {0}".format(self.구동계))

bicycle = 자전차(2, 100, "시마노")
bicycle.출력()

# 35번
class 자동차(차):
    def __init__(self, 바퀴, 가격):
        차.__init__(self, 바퀴, 가격)

    def 정보(self):
        print("바퀴수 {0}".format(self.바퀴))
        print("가격 {0}".format(self.가격))

car = 자동차(4, 1000)
car.정보()

#36번
class 자전차(차):
    def __init__(self, 바퀴, 가격):
        차.__init__(self, 바퀴, 가격)

    def 정보(self):
        print("바퀴수 {0}".format(self.바퀴))
        print("가격 {0}".format(self.가격))

bicycle = 자전차(2, 100)
bicycle.정보()

#37번
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        차.__init__(self, 바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        print("바퀴수 {0}".format(self.바퀴))
        print("가격 {0}".format(self.가격))
        print("구동계 {0}".format(self.구동계))

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()