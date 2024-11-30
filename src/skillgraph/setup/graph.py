import os
from typing import Dict, Optional, Set, Tuple

from pyvis.network import Network
from skillgraph.setup.topics import (TopicMap, generate_topic_breakdown,
                                     generate_topic_map)


class VisualGraph:
    """Creates and manages an interactive skill dependency graph visualization."""
    
    def __init__(
        self, 
        title: str,
        topic_map: TopicMap, 
        contains_subgraphs: bool = False
    ):
        """
        Initialize the skill graph with a topic dependency map.
        
        Args:
            topic_map (TopicMap): Mapping of topics and their dependencies
            nodes_with_subgraphs (Set[str], optional): Set of node names that have subgraphs
        """
        self.topic_map = topic_map
        self.graph = Network(
            height="750px",
            width="100%",
            bgcolor="#ffffff",
            font_color="#000000"
        )
        self.__title = title
        self.contains_subgraphs = contains_subgraphs
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
                node_attrs = {"label": mapping.topic}
                if self.contains_subgraphs:
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    print(f"Current directory: {current_dir}")
                    html_file = os.path.join(current_dir, f"{mapping.topic.replace(' ', '_')}.html")
                    print(f"HTML file: {html_file}")
                    node_attrs.update({
                        "url": html_file,
                        "title": f"<a href='{html_file}' target='_blank'>Click to view {mapping.topic} breakdown</a>"
                    })
                self.graph.add_node(mapping.topic, **node_attrs)
                added_nodes.add(mapping.topic)
            
            for dep in mapping.dependencies:
                if dep not in added_nodes:
                    node_attrs = {"label": dep}
                    if self.contains_subgraphs:
                        html_file = dep.replace(" ", "_") + ".html"
                        node_attrs.update({
                            "url": html_file,
                            "title": f"<a href='{html_file}' target='_blank'>Click to view {dep} breakdown</a>"
                        })
                    self.graph.add_node(dep, **node_attrs)
                    added_nodes.add(dep)
                
                self.graph.add_edge(dep, mapping.topic)
    
    
def build_graph_layers(root_topic: str) -> Tuple[Dict[str, TopicMap], Dict[str, VisualGraph]]:
    """
    Build a hierarchical graph of skill dependencies for a given root topic.
    
    Args:
        root_topic (str): The root topic to build the graph from
        
    Returns:
        tuple: A tuple containing:
            - dict: Topic breakdowns mapping topic names to their breakdowns
            - dict: Topic graphs mapping topic names to their visualizations
    """
    topic_breakdown, topic_graph = build_graph(root_topic)
    subtopics = topic_breakdown.content[0].parsed.subtopics
    
    topic_breakdowns = {}
    topic_graphs = {}
    
    # Create the root graph with knowledge of which nodes will have subgraphs
    topic_breakdown, topic_graph = build_graph(root_topic, show=True, contains_subgraphs=True)
    topic_breakdowns[root_topic] = topic_breakdown
    topic_graphs[root_topic] = topic_graph
   
    for subtopic in subtopics:
        print(f" - {subtopic.name}")
        subtopic_breakdown, topic_graph = build_graph(subtopic.name)
        topic_breakdowns[subtopic.name] = subtopic_breakdown.content[0].parsed
        topic_graphs[subtopic.name] = topic_graph
    
    return topic_breakdowns, topic_graphs


def build_graph(
    topic_name: str, 
    show: bool = True, 
    contains_subgraphs: bool = False
) -> Tuple[TopicMap, VisualGraph]:
    """
    Build a graph for a given topic.
    
    Args:
        topic_name (str): Name of the topic to build graph for
        show (bool): Whether to display the graph
        contains_subgraphs (bool): Whether the graph contains subgraphs
    """
    topic_breakdown = generate_topic_breakdown(topic_name)
    topics = topic_breakdown.content[0].parsed.subtopics
    topic_map = generate_topic_map(topics).content[0].parsed.mapping
    skill_graph = VisualGraph(topic_name, topic_map, contains_subgraphs)

    if show:
        output_name = topic_name.replace(" ", "_") + ".html"
        skill_graph.show(output_path=output_name)
    
    return topic_breakdown, skill_graph