from math import inf

class HashMap:
    def __init__(self, size=0):
        self.size = size
        self.hash_table = {}
        self.search_history = []

    def set_value(self, **payload):
        self.hash_table.update(payload)

    def get_value(self, key):
        for searched_item in self.search_history:
            if searched_item.get(key) != None:
                return 'Already searched for this item'
        return self.hash_table.get(key)

    def delete_value(self, key):
        deleted_element = self.hash_table.pop(key, 'Key not found')
        self.search_history.append(deleted_element)


def dijkstras(graph, start):
  distances = {}
  
  for vertex in graph:
    distances[vertex] = inf
    
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
        
  return distances