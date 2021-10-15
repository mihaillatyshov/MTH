import xml.etree.ElementTree as ET

class GraphParser:
	def __init__(self, file_name):
		self.tree = ET.parse(file_name)
		self.__nodes = self.__ParseNodes()
		self.__edges = self.__ParseEdges()

	def __ParseNodes(self):
		NodesLable = []
		Nodes = self.tree.findall("section/section[@name='node']")
		for node in Nodes:
			NodesLable.append(node.find("attribute[@key='label']").text)
		return NodesLable

	def __ParseEdges(self):
		Edges = []
		TEdges = self.tree.findall("section/section[@name='edge']")
		for edge in TEdges:
			Source = int(edge.find("attribute[@key='source']").text)
			Target = int(edge.find("attribute[@key='target']").text)
			Description = edge.find("attribute[@key='label']")
			if Description != None:
				Description = Description.text
			Edges.append({"source" : Source, "target" : Target, "desc" : Description})
		return Edges

	def GetNodes(self):
		return self.__nodes

	def GetEdges(self):
		return self.__edges

	def GetPrevNext(self, id):
		Prev = []
		Next = []
		for edge in self.__edges:
			if edge["source"] == id:
				Next.append({"id" : edge["target"], "desc" : edge["desc"]})
			if edge["target"] == id:
				Prev.append({"id" : edge["source"], "desc" : edge["desc"]})
		return ({"Now" : id, "Prev" : Prev, "Next" : Next})	
	


GP = GraphParser("./res/Polytech_total.xgml")
