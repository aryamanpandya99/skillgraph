from pyvis.network import Network
from skillgraph.setup.topics import TopicMap, generate_topic_breakdown, generate_topic_map


def build_graph_layers(root_topic: str) -> TopicMap:
    topic_breakdown, topic_map = build_graph(root_topic)

    subtopics = topic_breakdown.content[0].parsed.subtopics
    topic_map = generate_topic_map(subtopics).content[0].parsed.mapping
    
    map_layers = [{}, {}]
    map_layers[0][root_topic] = (topic_breakdown, topic_map)
   
    for subtopic in subtopics:
        print(f" - {subtopic.name}: {subtopic.description} \n Required: {subtopic.required} \n")
        subtopic_breakdown, subtopic_map = build_graph(subtopic.name)
        map_layers[1][subtopic.name] = (subtopic_breakdown, subtopic_map)

def build_graph(topic_name, show: bool = True):
    topic_breakdown = generate_topic_breakdown(topic_name)
    topic_description = topic_breakdown.content[0].parsed.description
    print(topic_description, "\n")
    
    topics = topic_breakdown.content[0].parsed.subtopics
    topic_map = generate_topic_map(topics).content[0].parsed.mapping
    
    if show:
        skill_graph = VisualGraph(topic_name, topic_map)
        output_name = topic_name.replace(" ", "_") + ".html"
        skill_graph.show(output_path=output_name)
    
    return topic_breakdown, topic_map


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
    
    
