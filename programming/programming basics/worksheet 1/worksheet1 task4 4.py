numberOfStudents = int(input("enter number of students: "))
numberOfBooks = int(input("enter number of books available: "))

booksPerPerson = numberOfBooks//numberOfStudents
booksLeft = numberOfBooks%numberOfStudents
print(booksPerPerson)
print(booksLeft)