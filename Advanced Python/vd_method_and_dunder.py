class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"{self.name} makes a {sound} sound."

    def __str__(self):
        return f"{self.name} is a {self.species}"

# Tạo đối tượng Animal
cat = Animal("Viet", "cat")
dog = Animal("Huy", "dog")

# In ra thông tin về các đối tượng Animal
print(cat)  # Kết quả: Viet is a cat
print(dog)  # Kết quả: Huy is a dog

# Khiến các đối tượng Animal kêu
cat_sound = cat.make_sound("meow")
dog_sound = dog.make_sound("gauu")
print(cat_sound)  # Kết quả: Viet makes a meow sound.
print(dog_sound)  # Kết quả: Huy makes a gauu sound.


