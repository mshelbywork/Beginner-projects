class Alien:
    health = 3
    total_aliens_created = 0
    alien_list = []
    def __init__(self, location):
        self.location_x = location[0]
        self.location_y = location[1]
        print (location)


        Alien.total_aliens_created += 1
    
    def hit (self):
        Alien.health -= 1
    
    
    def is_alive(self):
        alive = Alien.health
        if alive == 0:
            return 'alien died'
        else:
            return f'alien hit!, alien health: {self.health}'


    def teleport (self,location):
        self.location_x = location [0]
        self.location_y = location [1]


    def collision_detection(self):
        pass
    
    
    #def
    #location = alien_start_positions 

    

    


alien = Alien((2,0))

print (alien.health)
print (alien.location_x)
alien.hit()

alien.hit()
print (alien.is_alive())
alien.teleport((3,1))
print (alien.location_x)
