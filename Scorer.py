import math

class Scorer:

	def testtest():
		print("test")

	def getDistance(node1, node2):
		distX = abs(node1.getX() - node2.getX())
		distY = abs(node1.getY() - node2.getY())
		distance = (math.sqrt( distX ** 2 + distY ** 2) * 10) // 1 
		return int(distance)

	@staticmethod
	def score(parent, node, dest):
		if parent == None:
			node.setG(0)
		else:
			gScore = Scorer.getDistance(node, parent) + parent.getG()
			node.setG(gScore)

		hScore = Scorer.getDistance(node, dest)
		node.setH(hScore)

		fScore = int(node.getG() + node.getH())

		if fScore < node.getF():
			node.setF(fScore)
			node.setParent(parent)

		return node



