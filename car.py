class bird:
    def speak(self):
        return"tweet"
    
class parrot:
    def speak(self):
        return"mithu mithu"
    
class chicken:
    def speak(self):
        return"pak pak pakaaak"
    

def make_bird_speak(bird):
    print(bird.speak())

parrot = parrot()
chicken = chicken()
make_bird_speak(parrot) 
make_bird_speak(chicken)       
