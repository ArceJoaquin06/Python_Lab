class Wizard:
    def spells(self):
        print('Permiso, estoy tirando un hechizo')

class Warrior:
    def defence(self):
        print('Defendiendo estoy')

class Elf:
    def aura(self):
        print('+1000 de aura')

class DarkLord(Warrior, Elf):
    def darkness(self):
        print('no se q poner acá')

dark_lord = DarkLord()

dark_lord.aura()
dark_lord.defence()
print(DarkLord.__mro__)

class DarkLord(Elf, Warrior):
    def darkness(self):
        print('no se q poner acá')

dark_lord = DarkLord()

dark_lord.aura()
dark_lord.defence()
print(DarkLord.__mro__)
