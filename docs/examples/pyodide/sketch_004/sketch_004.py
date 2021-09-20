# From Prof. Claudio Esperança examples for BrythonIDE
# https://github.com/esperanc/brythonide/blob/master/demoSketches/boids.py

boids = []

def setup():
    createCanvas(720, 400)
    # Add an initial set of boids into the system
    for i in range(30):
        boids.append (Boid(random(720), random(400)))
    # frameRate(60)
    
def draw():
    background(51)
    # Run all the boids
    for boid in boids: 
        boid.run(boids)
        fill(255)

    # Display score
    textSize(16)
    textAlign(LEFT)
    text("Frames: %.1f" %frameRate(), 150, 390) 

# Boid class
# Methods for Separation, Cohesion, Alignment added
class Boid(object):

    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector.random2D()
        self.position = PVector(x, y)
        self.r = 3.0
        self.maxspeed = 3    # Maximum speed
        self.maxforce = 0.05 # Maximum steering force

    def run(self, boids):
        self.flock(boids)
        self.update()
        self.borders()
        self.render()

    # Forces go into acceleration
    def applyForce(self,force):
        self.acceleration = self.acceleration + force

    # We accumulate a new acceleration each time based on three rules
    def flock(self, boids):
        sep = self.separate(boids) # Separation
        ali = self.align(boids)    # Alignment
        coh = self.cohesion(boids) # Cohesion
        # Arbitrarily weight these forces
        sep = 2.5 * sep
        ali = 1.0 * ali
        coh = 1.0 * coh
        # Add the force vectors to acceleration
        self.applyForce(sep)
        self.applyForce(ali)
        self.applyForce(coh)

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity = self.velocity + self.acceleration
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position = self.position + self.velocity
        # Reset acceleration to 0 each cycle
        self.acceleration = 0 * self.acceleration

    # A method that calculates and applies a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self,target):
        desired = target - self.position # A vector pointing from the location to the target
        # Normalize desired and scale to maximum speed
        desired.normalize()
        desired = desired * self.maxspeed
        # Steering = Desired minus Velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce) # Limit to maximum steering force
        return steer

    # Draw boid as a circle
    def render(self):
        fill(127, 127)
        stroke(200)
        ellipse(self.position.x, self.position.y, 16, 16)

    # Wraparound
    def borders(self):
        if (self.position.x < -self.r): 
            self.position.x = width + self.r
        if (self.position.y < -self.r): 
            self.position.y = height + self.r
        if (self.position.x > width + self.r): 
            self.position.x = -self.r
        if (self.position.y > height + self.r): 
            self.position.y = -self.r


    # Separation
    # Method checks for nearby boids and steers away
    def separate(self, boids):
        desiredseparation = 25.0
        steer = PVector(0, 0)
        count = 0
        # For every boid in the system, check if it's too close
        for i in range(len(boids)):
            d = PVector.dist(self.position, boids[i].position)
            # If the distance is greater than 0 and less than an arbitrary amount (0 when you are yourself)
            if (0 < d < desiredseparation) :
                # Calculate vector pointing away from neighbor
                diff = self.position - boids[i].position
                diff.normalize()
                diff = diff / d
                steer = steer + diff
                count += 1 # Keep track of how many
        # Average -- divide by how many
        if (count > 0):
            steer = steer/count

        # As long as the vector is greater than 0
        if (steer.mag() > 0):
            # Implement Reynolds: Steering = Desired - Velocity
            steer.normalize()
            steer = steer * self.maxspeed
            steer = steer - self.velocity  
            steer.limit(self.maxforce)

        return steer


    # Alignment
    # For every nearby boid in the system, calculate the average velocity
    def align(self, boids):
        neighbordist = 50
        summ = PVector(0, 0)
        count = 0
        for i in range(len(boids)):
            d = PVector.dist(self.position, boids[i].position)
            if (0 < d < neighbordist):
                summ = summ + boids[i].velocity
                count += 1

        if (count > 0) :
            summ = summ/count
            summ.normalize()
            summ = summ * self.maxspeed
            steer = summ - self.velocity
            steer.limit(self.maxforce)
            return steer
        else:
            return PVector(0, 0)

    # Cohesion
    # For the average location (i.e. center) of all nearby boids, calculate steering vector towards that location
    def cohesion(self, boids) :
        neighbordist = 50
        summ = PVector(0, 0) # Start with empty vector to accumulate all locations
        count = 0
        for i in range(len(boids)):
            d = PVector.dist(self.position, boids[i].position)
            if (0 < d < neighbordist) :
                summ = summ + boids[i].position   # Add location
                count += 1

        if (count > 0) :
            summ = summ / count
            return self.seek(summ) # Steer towards the location
        else:
            return PVector(0, 0)
