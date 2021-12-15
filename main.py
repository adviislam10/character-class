class Character:
    # Initialize
    def __init__(self, name, phrase1, phrase2, level):
        
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = level

    # Methods
    def speak(self, phraseNum):

        if phraseNum == 1:
            print(self.phrase1)
        else: 
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print(self.name + " is level " + str(self.level) + "!")

# Create Objects
Po = Character("Po", "Skadoosh", "You have been blinded by pure awesomeness", 0)
Spiderman = Character("Peter", "My Spider-Sense is tingling", "Happy?", 0)

# Test Class and methods
Spiderman.speak(1)
Po.setLevel(2)
Po.speak(2)