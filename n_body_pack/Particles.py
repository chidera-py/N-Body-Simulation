import numpy as np

class Particle:
	def __init__(self, position, velocity, acceleration):
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration
	
	def update_positions(self, dt):
		"""Update particle position based on velocity"""
		self.position += self.velocity * dt

	
	def update_velocity(self, dt):
		"""Update particle velocity with acceleration"""
		self.velocity += (dt/2) * self.acceleration

	def update_acceleration(self, net_force, mass):
		"""Update particle acceleration based on net force"""
		self.acceleration = (1/mass) * net_force 
