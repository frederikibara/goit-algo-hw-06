from collections import UserDict


class AddressBook(UserDict):
    def __init__(self, record=None):
        super().__init__()
        if record:
            self.data[record.name.value] = record
    
        
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record
        return f'Complete : \'{record}\' has been added to book'
        
        
    def delete_record(self, name):
        is_find = False
        for key, record in list(self.data.items()):
              if key == name:
                del self.data[key]
                is_find = True
        
        if not is_find:
            raise ValueError(f'Record \'{name}\' not found')
        else:
            return f'Complete: \'{name}\' has been removed from address book'
       
       
    def find(self, name):
        for record in self.data:
            if record == name:
                return self.data[record]
        raise ValueError(f'Record : \'{name}\' not found in the address book')
    
        
    def __str__(self):
        if not self.data:
            return 'Address book is empty'
        
        items= []
        for key in sorted(self.data.keys()):  
            record = self.data[key]
            items.append(str(record))  
        return "\n".join(items)