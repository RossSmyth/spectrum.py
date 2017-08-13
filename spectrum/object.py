# -*- coding: utf-8 -*-

class Object:
	"""Represents a generic Spectrum object
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two objects are equal.     |
	+-----------+--------------------------------------+
	| x != y    | Checks if two objects are not equal. |
	+-----------+--------------------------------------+
	
	This is the class that will be the base class of most objects, since most 
	have an ID number. 
	
	Attributes
	----------
	id : int
		The ID of the object
	"""
	
	def __init__(self, id):
		self.id = id
		
	def __eq__(self, other):
		return isinstance(other, self.__class__) and other.id == self.id
		
	def __ne__(self, other):
		if isinstance(other, self.__class__):
			return other.id != self.id
		return True
