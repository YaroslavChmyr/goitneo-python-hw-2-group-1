from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        try:
            self.validate_phone(value)
            self.value = value
        except ValueError as error:
            print(error)

    def validate_phone(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone must be 10 digits")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def edit_phone(self, old_phone, new_phone):
        new_phone = Phone(new_phone)
        for item in range(len(self.phones)):
            if self.phones[item].value == old_phone:
                self.phones[item] = new_phone

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return phone
        return "No such phone"

    def remove_phone(self, phone):
        removed = False
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)
                removed = True
        if not removed:
            print("No such phone for this contact.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for item in self.data:
            if item == name:
                return self.data[item]

    def delete(self, name):
        try:
            self.data.pop(name)
        except KeyError:
            print("No such contact in AddressBook")


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(john)
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
