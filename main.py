# TASK POINT3D

# class Point3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def info(self):
#         print(f'x = {self.x}, y = {self.y}, z = {self.z}')

#     def distance_calc(self, a, b):
#         return b - a
    
#     def distance_result(self):
#         return (f'Distance x for y: {self.distance_calc(self.x, self.y)}.\nDistance y for z: {self.distance_calc(self.y, self.z)}')


# first = Point3D(5,12,3)
# first.info()

# first = Point3D(21,42,91)
# first.info()

# print(first.distance_result())








# TASK SQUARE

# class Square:
#     def __init__(self, a=0):
#         self.a = a
    
#     def perimetr(self):
#         return self.a * 4

#     def area(self):
#         return self.a * self.a

# my_square = Square(13)
# print(my_square.perimetr())
# print(my_square.area())








# TASK TRIANGLE

# class Triangle:
#     def __init__(self, a=0, b=0, c=0):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def perimetr(self):
#         if (self.c == 0):
#             self.c = (self.a**2 - self.b**2)**0.5
#             return self.a + self.b + self.c 
#         else:
#             return self.a + self.b + self.c 
#     def area(self):
#         self.p = self.perimetr()
#         return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))**0.5

# myTriangle = Triangle(5,2,12)

# print(myTriangle.perimetr())
# print(myTriangle.area())










# TASK DISTANCE

# class GetDistance:
#     def __init__(self, a = (0,0), b = (0,0), c = (0,0)):
#         self.a = a
#         self.b = b
#         self.c = c
#     def ac_distance(self):
#         self.dot_x_position = [self.a[0], self.c[0]]
#         self.dot_y_position = [self.a[1], self.c[1]]
#         self.dot_x_leg = max(self.dot_x_position) - min(self.dot_x_position)
#         self.dot_y_leg = max(self.dot_y_position) - min(self.dot_y_position)
#         return (self.dot_x_leg**2 + self.dot_y_leg**2)**0.5
#     def ab_distance(self):
#         self.dot_x_position = [self.a[0], self.b[0]]
#         self.dot_y_position = [self.a[1], self.b[1]]
#         self.dot_x_leg = max(self.dot_x_position) - min(self.dot_x_position)
#         self.dot_y_leg = max(self.dot_y_position) - min(self.dot_y_position)
#         return (self.dot_x_leg**2 + self.dot_y_leg**2)**0.5
#     def bc_distance(self):
#         self.dot_x_position = [self.b[0], self.c[0]]
#         self.dot_y_position = [self.b[1], self.c[1]]
#         self.dot_x_leg = max(self.dot_x_position) - min(self.dot_x_position)
#         self.dot_y_leg = max(self.dot_y_position) - min(self.dot_y_position)
#         return (self.dot_x_leg**2 + self.dot_y_leg**2)**0.5
#     def perimetr(self):
#         self.a_side = self.ab_distance()
#         self.b_side = self.ac_distance()
#         self.c_side = self.bc_distance()
#         return self.a_side + self.b_side + self.c_side
# myDot = GetDistance((2,4), (6,9), (6,0))
# print(myDot.perimetr())









# TASK CPerson

# class CPerson:
#     def __init__(self, surname, name, patronymic, birth, gender):
#         self.surname = surname
#         self.name = name
#         self.patronymic = patronymic
#         self.birth = birth
#         self.gender = gender
#     def getSurname(self):
#         return(f'Surname: {self.surname}')
#     def getName(self):
#         return(f'Name: {self.name}')
#     def getPatronymic(self):
#         return(f'Patronymic: {self.patronymic}')
#     def getBirth(self):
#         return(f'Birth: {self.birth}')
#     def getGender(self):
#         return(f'Gender: {self.gender}')
#     def getInfo(self):
#         return(f'Surname: {self.surname}\nName: {self.name}\nPatronymic: {self.patronymic}\nBirth: {self.birth}\nGender: {self.gender}')
#     def __del__(self):
#         print("Person deleted")

# myPerson = CPerson("Yurin", "Yuri", "Yurievich", "09.09.2005", "Male")
# print(myPerson.getSurname())
# print(myPerson.getName())
# print(myPerson.getPatronymic())
# print(myPerson.getBirth())
# print(myPerson.getGender())
# print("============================================")
# print(myPerson.getInfo())
# print("============================================")
# myPerson.name = "Eugene"
# print(myPerson.getInfo())
# del myPerson








# TASK Phone

# class Phone:
#     def __init__(self, number, model, weight):
#         self.number = number
#         self.model = model
#         self.weight = weight
#     def getInfo(self):
#         return(f'Number: {self.number}\nModel: {self.model}\nWeight: {self.weight}\n=============')
#     def receiveCall(self, name):
#         return(f'Звонит {name}\n-------------')
#     def getNumber(self):
#         return(self.number)


# myFirstPhone = Phone("88005553535", "X-12", "120")
# mySecondPhone = Phone("89997771212", "Br-4", "110")
# myThirdPhone = Phone("89314448584", "Iq-11", "130")

# print(myFirstPhone.receiveCall("Albert"))
# print(myFirstPhone.getInfo())
# print(myFirstPhone.getNumber())

# print(mySecondPhone.receiveCall("Dmitry"))
# print(mySecondPhone.getInfo())
# print(mySecondPhone.getNumber())

# print(myThirdPhone.receiveCall("Yuri"))
# print(myThirdPhone.getInfo())
# print(myThirdPhone.getNumber())









# TASK Reader

# class Reader:
#     def __init__(self, surname, name, patronymic, libraryCard, faculty, birth, phoneNumber):
#         self.surname = surname
#         self.name = name
#         self.patronymic = patronymic
#         self.libraryCard = libraryCard
#         self.faculty = faculty
#         self.birth = birth
#         self.phoneNumber = phoneNumber
#     def takeBook(self, quantity):
#         self.quantity = quantity
#         print(f'{self.surname} {self.name[0]}. {self.patronymic[0]}. взял {self.quantity} книги.')
#     def returnBook(self, quantity):
#         self.quantity = quantity
#         print(f'{self.surname} {self.name[0]}. {self.patronymic[0]}. вернул {self.quantity} книги.')


# myReader = Reader("Петров", "Владимир", "Викторович", 12, "Факультет", "06.06.1982", "88005553535")

# myReader.takeBook(3)
# myReader.returnBook(3)