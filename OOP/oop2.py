"""
    Encapsulation:
        for public no extra changes
        for private add __ in front of the variables. 
"""

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = 100 * self.__stamina
        self.mana = 10 * self.__intelligence 
    
    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if(fireball_cost > self.mana):
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana = self.mana - fireball_cost
            target.get_fireballed(fireball_damage)

    def is_alive(self):
        if(self.health > 0):
            return True
        return False

    def get_fireballed(self, fireball_damage):
        fireball_damage = fireball_damage - self.__stamina
        self.health = self.health - fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana = potion_mana + self.__intelligence
        self.mana = self.mana + potion_mana

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance 

    def get_account_number(self):
        return self.__account_number 

    def get_balance(self):
        return self.__balance 

    def deposit(self, amount):
        if(amount <= 0):
            raise ValueError("cannot deposit zero or negative funds")
        else:
            self.__balance = self.__balance + amount 

    def withdraw(self, amount):
        if(amount <= 0):
            raise ValueError("cannot withdraw zero or negative funds")
        elif(self.__balance - amount < 0):
            raise ValueError("insufficient funds")
        else:
            self.__balance = self.__balance - amount 
