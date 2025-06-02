class Dog:
    def __init__(self, name, breed):
        self.name = name        # instance variable
        self.breed = breed      # instance variable

    def bark(self):
        print(f"{self.name} says: Woof! I'm a {self.breed}.")

# Create two instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "Beagle")

# Call the bark method
dog1.bark()  # Output: Buddy says: Woof! I'm a Golden Retriever.
dog2.bark()  # Output: Luna says: Woof! I'm a Beagle.