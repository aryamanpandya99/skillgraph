from pyvis.network import Network
from .subjects import TopicMap


class SkillGraph:
    """Creates and manages an interactive skill dependency graph visualization."""
    
    def __init__(self, topic_map: TopicMap):
        """
        Initialize the skill graph with a topic dependency map.
        
        Args:
            topic_map (TopicMap): Mapping of topics and their dependencies
        """
        self.topic_map = topic_map
        self.graph = Network(
            height="750px",
            width="100%",
            bgcolor="#ffffff",
            font_color="#000000"
        )
        self._build_graph()
    
    def show(self, output_path: str = "skill_graph.html"):
        """
        Save and display the graph visualization.
        
        Args:
            output_path (str): Path where the HTML file should be saved
        """
        self.graph.show(output_path)
    
    def _build_graph(self):
        """Constructs the network graph from the topic map."""
        added_nodes = set()
        for mapping in self.topic_map:
            if mapping not in added_nodes:
                print(f"Adding node: {mapping}")
                self.graph.add_node(mapping, label=mapping)
                added_nodes.add(mapping)
            
            for dep in mapping.dependencies:
                if dep not in added_nodes:
                    self.graph.add_node(dep, label=dep)
                    added_nodes.add(dep)
                
                self.graph.add_edge(dep, mapping)
    
    
