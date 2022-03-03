import pygame as pg
import pygame.gfxdraw
import math
import sys


# math
NORTH = math.pi / 2

# rendu
SIZE = (600, 600)
CENTER = (SIZE[0]//2, SIZE[1]//2)

def draw_text(surface:pg.Surface, text:str, pos:iter, color):
	if not isinstance(text, str):
		text = str(text)
	font = pg.font.SysFont("Arial", 20)
	rendered = font.render(text, True, color)
	w, h = rendered.get_size()

	surface.blit(rendered, (pos[0] - w//2, pos[1]-h//2)) # center le text

class GraphRenderer:
	"""
	:graph: Le graph sous forme d'un dictionnaire
	:node_radius: La taille du rayon d'un cercle
	"""
	def __init__(self, graph:dict, node_radius:int=20, base_length:int=100, length_offset:int=40):
		pg.init()
		self.graph = graph
		self.node_radius = node_radius

		self.screen = pg.display.set_mode(SIZE)
		self.running = True
		self.nodelist = tuple(self.graph.keys())

		self.nodes_pos = {} # la positon du centre des nodes

		self.calculate_nodes_center(base_length, length_offset)

	def events(self):
		for e in pg.event.get():
			if e.type == pg.QUIT:
				self.running = False

	def draw(self):
		while self.running:
			self.events()
			self.screen.fill((12, 12, 12))

			self.draw_nodes_links()
			self.draw_nodes()

			# pg.gfxdraw.aacircle(self.screen, *CENTER, self.node_radius, (255, 255, 255))
			# draw_text(self.screen, 'A', CENTER)

			pg.display.update()
		pg.quit()


	# si la longueur * l'angle est inférieur à 2 * le rayon d'un noeud, alors il faut agrandir la longueur
	# la distance centre - point car ils risquent de se chevaucher
	def calculate_nodes_center(self, longueur, long_offset):
		delta_angle = 2*math.pi / len(self.nodelist) # l'angle entre chaque noeud -> 360° / nb-de-noeuds
		angle = NORTH
		
		while longueur*delta_angle < 2*self.node_radius:
			longueur += long_offset

		for node in self.nodelist:
			self.nodes_pos[node] = [CENTER[0] + math.cos(angle)*longueur, CENTER[1] - math.sin(angle)*longueur]
			angle += delta_angle

	def draw_nodes(self):
		for node in self.nodelist:
			pg.gfxdraw.filled_circle(self.screen, int(self.nodes_pos[node][0]), int(self.nodes_pos[node][1]), self.node_radius, (12, 12, 12))
			pg.gfxdraw.aacircle(self.screen, int(self.nodes_pos[node][0]), int(self.nodes_pos[node][1]), self.node_radius, (255, 255, 255))
			draw_text(self.screen, node, self.nodes_pos[node], (255, 255, 255))

	def draw_nodes_links(self):
		for start_node in self.nodelist:
			start_pos = self.nodes_pos[start_node]
			for end_node in self.graph[start_node]:
				end_pos = self.nodes_pos[end_node]
				pg.draw.line(self.screen, (255, 255, 255), start_pos, end_pos)

# huge_graph = {chr(num): num for num in range(ord('A'), ord('A')+26)}
# graph = {0:[1, 6, 7], 1:[2, 4, 0, 6, 5], 2:[1], 3:[5, 6, 8], 4:[1], 5:[6, 3, 1], 6:[1, 5, 3, 7, 0], 7:[0, 6, 8], 8:[7, 3]}

# renderer = GraphRenderer(graph)
# renderer.draw()
