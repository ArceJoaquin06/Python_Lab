class Alumno:
    def __init__(self, name, surname, age, course):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.age = age
        self.course = course.capitalize()

    def programar(self):
        print(f'El alumno {self.name} está programando')

alumno1 = Alumno(input('Ingrese su nombre: '), input('Ingrese su apellido: '), int(input('Ingrese su edad: ')), input('Ingrese su curso: '))
alumno1.programar()
