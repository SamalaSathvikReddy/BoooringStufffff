class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.depth * self.height * self.width

    def get_cost(self):
        cost = self.armor * self.height
        return cost
    def fortify(self):
        self.armor = self.armor * 2

class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self):
        self.health = self.health - 1
        if(self.health <= 0):
            raise Exception(f"{self.name} is already dead")

    def shoot(self, target):
        if(self.num_arrows <= 0):
            raise Exception(f"{self.name} can't shoot")
        else:
            print(f"{self.name} shoots {target.name}")
            target.take_hit()
            self.num_arrows = self.num_arrows - 1

class Dragon:

    def __init__(self, element):
        self.element = element

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0
    


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        next_books = []
        for b in self.books:
            if(b.title.lower() != book.title.lower() and b.author.lower() != book.author.lower()):
                next_books.append(b)
        self.books = next_books

    def search_books(self, search_string):
        res = []
        for b in self.books:
            if(search_string.lower() in b.title.lower() or search_string.lower() in b.author.lower()):
                res.append(b)
        return res
                

b1 = Brawler("Aragorn", 4, 4)
b2 = Brawler("Gimli", 2, 7)
b3 = Brawler("Legolas", 7, 7)
b4 = Brawler("Frodo", 3, 2)


class BatteringRam:
    damage = 2
    length = 4



