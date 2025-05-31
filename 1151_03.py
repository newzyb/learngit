# is a; has a 练习

class Computer:
    def __init__(self,brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在使用电脑上网......')

    def __str__(self):
        return self.brand + self.type + self.color

class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + self.author +self.number

class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过此书！')
                break
        else:
            # 将book添加到列表中
            self.books.append(book)
            print('添加成功！')

    def show_book(self):
        for book in self.books:
            print(book.bname)

    def __str__(self):
        return self.name + str(self.computer) + str(self.books)

computer = Computer('mac', 'mac_pro_2020', '深灰色')

book = Book('盗墓笔记', '南派三叔', 100)

stu = Student('yanbin', computer, book)
print(stu)




