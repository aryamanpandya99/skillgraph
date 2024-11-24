from pyvis.network import Network

# Create a new network
net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)

# Define the high level subjects
subjects = {
    "Science": [],
    "Mathematics": []
}

# Define math subjects and their relationships as a tree structure
math_subjects = {
    "Mathematics": {
        "Calculus": {
            "Real Analysis": {},
            "Complex Analysis": {},
            "Differential Equations": {}
        },
        "Linear Algebra": {
            "Matrix Theory": {},
            "Vector Spaces": {}
        },
        "Abstract Algebra": {
            "Group Theory": {},
            "Ring Theory": {}
        },
        "Number Theory": {
            "Prime Numbers": {},
            "Cryptography": {}
        }
    }
}

# Add high level nodes first
for subject in subjects.keys():
    if subject == "Mathematics":
        net.add_node("mathematics", title="<a href='file:///Users/ap/skillgraph/src/skillgraph/math_subjects_subtree.html'>Click to see Math subjects</a>")
    else:
        net.add_node(subject, label=subject, title=subject)

# Add edges for high level nodes
for subject, prerequisites in subjects.items():
    for prereq in prerequisites:
        net.add_edge(prereq, subject)

# Create a separate network for math subjects
math_net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)

def add_subjects_recursively(parent, subjects_dict):
    """Recursively add nodes and edges to create a tree structure"""
    for subject, children in subjects_dict.items():
        math_net.add_node(subject, label=subject, title=subject)
        if parent:
            math_net.add_edge(parent, subject)
        add_subjects_recursively(subject, children)

# Build the math subjects tree
add_subjects_recursively(None, math_subjects)

# Configure layout options for tree structure
math_net.set_options("""
const options = {
    "layout": {
        "hierarchical": {
            "direction": "UD",
            "sortMethod": "directed", 
            "levelSeparation": 100,
            "nodeSpacing": 100
        }
    },
    "physics": false
}
""")

# Add physics controls to main network
net.toggle_physics(True)
net.show_buttons(filter_=['physics'])

# Generate and display both graphs
net.show('math_subjects.html', notebook=False)
math_net.show('math_subjects_subtree.html', notebook=False)
