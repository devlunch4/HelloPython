class Dog:

    def __init__(self):
        self.bark = True

    def mute(self):
        self.bark = False


class Bird:

    def __init__(self):
        self.flypower = 100

    def flypowerup(self, powerup):
        self.flypower += powerup


class GS(Dog, Bird):

    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)

if __name__ == "__main__":
    a = GS(); 
    print("bark", ":", a.bark)
    print("flypower", ":", a.flypower)
    a.mute()
    a.flypowerup(10)
    print("bark", ":", a.bark)
    print("flypower", ":", a.flypower)
