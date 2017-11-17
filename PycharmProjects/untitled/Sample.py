class Enemy:
    life = 3

    def attack(self):
        print("gone")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print ("dead")
        else:
            print(str(self.life) + "life left")


enemy1 = Enemy()    # assign object to function
enemy2 = Enemy()

enemy1.attack()       # calling the object to function
enemy2.attack()

enemy1.checkLife()      # calling another function with object function
enemy2.checkLife()