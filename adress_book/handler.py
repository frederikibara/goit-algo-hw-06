from adress_book_manager import AddressBook
    
    
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        
        if value == '' or value == None:
            raise ValueError('Name is empty')
        for digit in value:
            if digit.isdigit():
                raise TypeError('Name is does not be a number')
        else:
            super().__init__(value.title())
        

class Phone(Field):
    def __init__(self, value):
        self.__max_num_length = 10
        self.operators_code = ('063', '073', '093', '091', '044', 
                               '050', '066', '095', '099', '039',
                               '067', '068', '096', '097', '098')
        
        for char in value:
            if char.isalpha():
                raise ValueError('Invalid phone number')
        
        if len(value) > self.__max_num_length:
            raise ValueError(f'Invalid phone number: maximum length {self.__max_num_length}')
        
        if value[:3] not in self.operators_code:
            raise ValueError('Unknown operator')  # UnknownOperartrError

        self.value = value
                

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        

    def add_phone(self, phone):
        if phone not in self.phones:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
            return f'Complete : \'{phone}\' has been added to the phones list'
        else:
            raise ValueError('This phone already in the phones list') #NotInListError


    def remove_phone(self, current_phone):
        for phone in self.phones:
            if phone.value == current_phone:
                self.phones.remove(phone)
                return f'Complete : \'{phone}\' has been removed from phones list'
        raise ValueError('This phone not in the list') #NotInListError
    
    
    def edit_phone(self, current_phone, new_phone):
        for phone in self.phones:
            if phone.value == current_phone:
                phone.value = new_phone   
                return f'Complete : \'{current_phone}\' has been changed to \'{new_phone}\''      
        raise ValueError('This phone not in the list')
                    
                          
    def find_phone(self, p) -> Phone:
        for phone in self.phones:
            if phone.value == p:
                return f'Complete : \'{phone}\' finded'
                                                                             
                          
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        