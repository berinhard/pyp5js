from pyp5js import *

def setup():
    pass

def draw():
    pass

deviceMoved = None
deviceTurned = None
deviceShaken = None
keyPressed = None
keyReleased = None
keyTyped = None
mouseMoved = None
mouseDragged = None
mousePressed = None
mouseReleased = None
mouseClicked = None
doubleClicked = None
mouseWheel = None
touchStarted = None
touchMoved = None
touchEnded = None
windowResized = None


# From Prof. Claudio Esperança examples for BrythonIDE
# https://github.com/esperanc/brythonide/blob/master/demoSketches/boids.py

boids = [];

def setup() :
  createCanvas(720, 400);

  # Add an initial set of boids into the system
  for i in range(40):
    boids.append (Boid(random(720), random(400)))

def draw() :
  background(51);
  # Run all the boids
  for boid in boids: boid.run(boids)


# Boid class
# Methods for Separation, Cohesion, Alignment added
class Boid (object):

    def __init__(self, x, y) :
        self.acceleration = createVector(0, 0);
        self.velocity = p5.Vector.random2D();
        self.position = createVector(x, y);
        self.r = 3.0;
        self.maxspeed = 3;    # Maximum speed
        self.maxforce = 0.05; # Maximum steering force

    def run (self, boids):
        self.flock(boids);
        self.update();
        self.borders();
        self.render();

    # Forces go into acceleration
    def applyForce (self,force):
        self.acceleration.add(force);

    # We accumulate a new acceleration each time based on three rules
    def flock (self, boids) :
        sep = self.separate(boids); # Separation
        ali = self.align(boids);    # Alignment
        coh = self.cohesion(boids); # Cohesion
        # Arbitrarily weight these forces
        sep.mult(2.5);
        ali.mult(1.0);
        coh.mult(1.0);
        # Add the force vectors to acceleration
        self.applyForce(sep);
        self.applyForce(ali);
        self.applyForce(coh);

    # Method to update location
    def update (self) :
        # Update velocity
        self.velocity.add(self.acceleration);
        # Limit speed
        self.velocity.limit(self.maxspeed);
        self.position.add(self.velocity);
        # Reset acceleration to 0 each cycle
        self.acceleration.mult(0);

    # A method that calculates and applies a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek (self,target):
        desired = p5.Vector.sub(target, self.position); # A vector pointing from the location to the target
        # Normalize desired and scale to maximum speed
        desired.normalize();
        desired.mult(self.maxspeed);
        # Steering = Desired minus Velocity
        steer = p5.Vector.sub(desired, self.velocity);
        steer.limit(self.maxforce); # Limit to maximum steering force
        return steer;

    # Draw boid as a circle
    def render (self) :
        fill(127, 127);
        stroke(200);
        ellipse(self.position.x, self.position.y, 16, 16);

    # Wraparound
    def borders (self) :
        if (self.position.x < -self.r): self.position.x = width + self.r;
        if (self.position.y < -self.r): self.position.y = height + self.r;
        if (self.position.x > width + self.r): self.position.x = -self.r;
        if (self.position.y > height + self.r): self.position.y = -self.r;


    # Separation
    # Method checks for nearby boids and steers away
    def separate (self, boids) :
        desiredseparation = 25.0;
        steer = createVector(0, 0);
        count = 0;
        # For every boid in the system, check if it's too close
        for i in range(len(boids)):
            d = p5.Vector.dist(self.position, boids[i].position);
            # If the distance is greater than 0 and less than an arbitrary amount (0 when you are yourself)
            if ((d > 0) and (d < desiredseparation)) :
              # Calculate vector pointing away from neighbor
              diff = p5.Vector.sub(self.position, boids[i].position);
              diff.normalize();
              diff.div(d); # Weight by distance
              steer.add(diff);
              count+=1; # Keep track of how many
        # Average -- divide by how many
        if (count > 0) :
            steer.div(count);


        # As long as the vector is greater than 0
        if (steer.mag() > 0) :
            # Implement Reynolds: Steering = Desired - Velocity
            steer.normalize();
            steer.mult(self.maxspeed);
            steer.sub(self.velocity);
            steer.limit(self.maxforce);

        return steer;


    # Alignment
    # For every nearby boid in the system, calculate the average velocity
    def align (self, boids) :
      neighbordist = 50;
      sum = createVector(0, 0);
      count = 0;
      for i in range(len(boids)):
        d = p5.Vector.dist(self.position, boids[i].position);
        if ((d > 0) and (d < neighbordist)) :
          sum.add(boids[i].velocity);
          count+=1;

      if (count > 0) :
        sum.div(count);
        sum.normalize();
        sum.mult(self.maxspeed);
        steer = p5.Vector.sub(sum, self.velocity);
        steer.limit(self.maxforce);
        return steer;
      else:
        return createVector(0, 0);

    # Cohesion
    # For the average location (i.e. center) of all nearby boids, calculate steering vector towards that location
    def cohesion  (self, boids) :
      neighbordist = 50;
      sum = createVector(0, 0); # Start with empty vector to accumulate all locations
      count = 0;
      for i in range(len(boids)):
        d = p5.Vector.dist(self.position, boids[i].position);
        if ((d > 0) and (d < neighbordist)) :
          sum.add(boids[i].position); # Add location
          count+=1;

      if (count > 0) :
        sum.div(count);
        return self.seek(sum); # Steer towards the location
      else:
        return createVector(0, 0);



event_functions = {
    "deviceMoved": deviceMoved,
    "deviceTurned": deviceTurned,
    "deviceShaken": deviceShaken,
    "keyPressed": keyPressed,
    "keyReleased": keyReleased,
    "keyTyped": keyTyped,
    "mouseMoved": mouseMoved,
    "mouseDragged": mouseDragged,
    "mousePressed": mousePressed,
    "mouseReleased": mouseReleased,
    "mouseClicked": mouseClicked,
    "doubleClicked": doubleClicked,
    "mouseWheel": mouseWheel,
    "touchStarted": touchStarted,
    "touchMoved": touchMoved,
    "touchEnded": touchEnded,
    "windowResized": windowResized,
}

start_p5(setup, draw, event_functions)