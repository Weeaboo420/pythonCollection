class item:
    def __init__(self, name, atkpower, defpower):
        if type(name) is str and len(name) > 3:
            self.name = name
        else:
            raise TypeError("Item name must be a string and be longer than 3 characters!")
        if type(atkpower) is int and atkpower >= 0:
            self.atkpower = atkpower
        else:
            raise TypeError("Atkpower must be an integer and greater than or equal to 0!")
        if type(defpower) is int and defpower >= 0:
            self.defpower = defpower
        else:
            raise TypeError("Defpower must be an integer and greater than or equal to 0!")

db = []
db.append(item("Round Sword", 7, 2))
db.append(item("Justified Spear", 9, 1))
db.append(item("Spaghet Shield", 0, 20))
db.append(item("Ginger\'s Rapier", 6, 4))
db.append(item("Leather Shield", 0, 2))
db.append(item("Dirt Shield", 0, 1))
db.append(item("Broadsword", 8, 3))
db.append(item("Hardened Clay", 3, 1))
db.append(item("Bold Shield", 2, 11))
db.append(item("Dragon Katana", 12, 7))
db.append(item("Fortified Mace", 9, 3))
db.append(item("Dull Sword", 3, 2))
db.append(item("Flat Sword", 15, 1))
db.append(item("Tri-Shield", 0, 15))
db.append(item("Clay Shield", 1, 8))
db.append(item("Small Dagger", 6, 1))
db.append(item("Red Katana", 17, 9))
db.append(item("Black Katana", 20, 3))
db.append(item("Broken Stick", 1, 1))
db.append(item("6 ft. Lance", 12, 2))
