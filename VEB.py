import math

# Stores a VEB-tree where the values may be between 0 and x (where x is the lowest continuous power of two less than u)

class VEB:

	def high(self, x):
		return int(math.floor(x / math.sqrt(self.u)))

	def low(self, x):
		return int((x % math.ceil(math.sqrt(self.u))))

	def index(self, x, y):
		return int((x * math.floor(math.sqrt(self.u))) + y)

	def __init__(self, u):
		if u < 0:
			raise Exception("u cannot be less than 0 --- u = " + str(u));
		self.u = 2;
		while self.u <= u:
			self.u *= self.u	# get the lowest power of two that is higher than u
		self.min = None
		self.max = None
		if (u > 2):
			self.clusters = [ VEB(self.high(self.u)) for i in range(0, self.high(self.u)) ]
			self.summary = VEB(self.high(self.u))

	def member(self, x):
		if x == self.min or x == self.max:	# found it as the minimum or maximum
			return True
		elif self.u <= 2:					# has not found it in the "leaf"
			return False
		else:
			return self.clusters[self.high(x)].member(self.low(x))	# looks for it in the clusters inside

	def successor(self, x):
		if self.u <= 2:						 
			if x == 0 and self.max == 1:		
				return 1
			else:
				return None
		elif self.min != None and x < self.min: # x is less than everything in the tree, returns the minimum
			return self.min
		else:
			maxlow = self.clusters[self.high(x)].max
			if maxlow != None and self.low(x) < maxlow:
				offset = self.clusters[self.high(x)].successor(self.low(x))
				return self.index(self.high(x), offset)
			else:
				succcluster = self.summary.successor(self.high(x))
				if succcluster == None:
					return None
				else:
					offset = self.clusters[succcluster].min
					return self.index(succcluster, offset)

	def predecessor(self, x):
		if self.u <= 2:
			if x == 1 and self.min == 0:
				return 0
			else:
				return None
		elif self.max != None and x > self.max:
			return self.max
		else:
			minlow = self.clusters[self.high(x)].min
			if minlow != None and self.low(x) > minlow:
				offset = self.clusters[self.high(x)].predecessor(self.low(x))
				return self.index(self.high(x), offset)
			else:
				predcluster = self.summary.predecessor(self.high(x))
				if predcluster == None:
					if self.min != None and x > self.min:
						return self.min
					else:
						return None
				else:
					offset = self.clusters[predcluster].max
					return self.index(predcluster, offset)

	def emptyInsert(self, x):
		self.min = x
		self.max = x

	def insert(self, x):
		if self.min == None:
			self.emptyInsert(x)
		else:
			if x < self.min:
				temp = self.min
				self.min = x
				x = temp
			if self.u > 2:
				if self.clusters[ self.high(x) ].min == None:
					self.summary.insert(self.high(x))
					self.clusters[self.high(x)].emptyInsert(self.low(x))
				else:
					self.clusters[self.high(x)].insert(self.low(x))
			if x > self.max:
				self.max = x
