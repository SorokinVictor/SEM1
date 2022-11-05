# Печатаем заголовок программы
print("Добро пожаловать в Телефонную книгу! ")

# Создаём текстовый файл для хранения контактных данных
filename = "myphonebook.txt"
myfile = open(filename, "a+")
myfile.close


# Определение главного меню
def main_menu():
    print("\nГлавное меню\n")
    print("1. Показать все существующие контакты")
    print("2. Добавить новый контакт")
    print("3. Выполнить поиск по существующему контакту")
    print("4. Выход")
    choice = input("Введите свой выбор: ")
    if choice == "1":
        myfile = open(filename, "r+")
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print("В телефонной книге нет контакта.")
        else:
            print(filecontents)
        myfile.close
        enter = input("Нажмите Enter, чтобы продолжить...")
        main_menu()
    elif choice == "2":
        newcontact()
        enter = input("Нажмите Enter, чтобы продолжить...")
        main_menu()
    elif choice == "3":
        searchcontact()
        enter = input("Нажмите Enter, чтобы продолжить...")
        main_menu()
    elif choice == "4":
        print("Благодарим вас за использование телефонной книги!")
    else:
        print("Пожалуйста, предоставьте допустимые входные данные!\n")
        enter = input("Нажмите Enter, чтобы продолжить...")
        main_menu()


# Определение функции поиска
def searchcontact():
    searchname = input("Введите данные для поиска контактной записи:")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("Ваша необходимая контактная информация - это:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("Искомый контакт недоступен в телефонной книге", searchname)


# Имя
def input_firstname():
    first = input("Введите свое имя: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


# Фамилия
def input_lastname():
    last = input("Введите свою фамилию: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


# Сохранение новых контактных данных
def newcontact():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Введите свой номер телефона: ")
    emailID = input("Введите свой адрес электронной почты: ")
    contactDetails = ("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID + "]\n")
    myfile = open(filename, "a")
    myfile.write(contactDetails)
    print("Следующие контактные данные:\n " + contactDetails + "\nбыл успешно сохранен!")


main_menu()