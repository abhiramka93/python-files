class Bank:
    head_office = "Ernakulam"
    year_of_foundation = 1987

    def __init__(self, branch_manager, location, ifsc_code):
        self.branch_manager = branch_manager
        self.location = location
        self.ifsc_code = ifsc_code

    def change_bank_manager(self, new_manager):
        self.branch_manager = new_manager

    @classmethod
    def change_head_office(cls, new_head_office_name):
        cls.head_office = new_head_office_name


s1 = Bank('Jins', 'Kaloor', 123456789)

print(s1.branch_manager)
s1.change_bank_manager('robert')
print(s1.branch_manager)
Bank.change_head_office('Kottayam')
print('Headquarters has been changed to', Bank.head_office)
