from enum import Enum

class AtomGroup:
	def __init__(self, string):
		if len(string) > 1:
			if string[1].islower():
				self.symbol = string[0:2]
				self.number = int(string[2:]) if len(string)>2 else 1
			else:
				self.symbol = string[0]
				self.number = int(string[1:])
		else:
			self.symbol = string[0]
			self.number = 1
			
class Molecule:
	def __init__(self, string):
		self.atomGroups = []
		index = 0
		for i, c in enumerate(string):
			if c.isupper():
				if (i-index)>0:
					self.atomGroups.append(AtomGroup(string[index:i]))
				index = i
		self.atomGroups.append(AtomGroup(string[index:]))
		
	def print(self):
		for a in self.atomGroups:
			print(a.symbol + " " + str(a.number))
			
class MoleculeGroup:
	def __init__(self, string):
		string = string.replace(" ", "")
		self.molecules = []
		index = 0
		for i, c in enumerate(string):
			if c == '+':
				self.molecules.append(Molecule(string[index:i]))
				index = i+1
		self.molecules.append(Molecule(string[index:]))
	
	def print(self):
		for m in self.molecules:
			m.print()
			print()
			
class Equation:
	def __init__(self, string):
		string = string.replace(" ", "")
		for i, c in enumerate(string):
			if c == '-' and string[i+1] == '>':
				self.leftSide = MoleculeGroup(string[:i])
				self.rightSide = MoleculeGroup(string[i+2:])
				
	def print(self):
		self.leftSide.print()
		print(" -> ")
		self.rightSide.print()