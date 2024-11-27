from pyvis.network import Network
from skillgraph.setup.topics import TopicMap, generate_topic_breakdown, generate_topic_map


def build_graph(root_topic: str, layers: int = 3) -> TopicMap:
    topic_breakdown = generate_topic_breakdown(root_topic)
    topic_description = topic_breakdown.content[0].parsed.description
    
    print(topic_description, "\n")
    topic_map = generate_topic_map(subtopics).content[0].parsed.mapping
    
    map_layers = [{} for _ in range(layers)]
    map_layers[0][root_topic] = topic_map
   
    for layer in range(layers):
        subtopics = topic_breakdown.content[0].parsed.subtopics
        for subtopic in subtopics:
            subtopic_breakdown = generate_topic_breakdown(subtopic.name)
        
            topic_map = generate_topic_map(subtopics).content[0].parsed.mapping

        
        skill_graph = SkillGraph(subject, topic_map)
        skill_graph.show()


class VisualGraph:
    """Creates and manages an interactive skill dependency graph visualization."""
    
    def __init__(self, title: str, topic_map: TopicMap):
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
        self.__title = title
        self._build_graph()
    
    @property
    def title(self):
        return self.__title
    
    def show(self, output_path: str = "skill_graph.html"):
        """
        Save and display the graph visualization.
        
        Args:
            output_path (str): Path where the HTML file should be saved
        """
        self.graph.show(output_path, notebook=False)
    
    def _build_graph(self):
        """Constructs the network graph from the topic map."""
        added_nodes = set()
        for mapping in self.topic_map:
            if mapping.topic not in added_nodes:
                self.graph.add_node(mapping.topic, label=mapping.topic)
                added_nodes.add(mapping.topic)
            
            for dep in mapping.dependencies:
                if dep not in added_nodes:
                    self.graph.add_node(dep, label=dep)
                    added_nodes.add(dep)
                
                self.graph.add_edge(dep, mapping.topic)
    
    
