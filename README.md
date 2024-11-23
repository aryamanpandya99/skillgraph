# Knowledge Graph

Knowledge Graph is a comprehensive application designed to assist users building knowledge trees for skills that they want to gain. It breaks down the skill into smaller sub-skills and then tracks user progress based on descriptions of actions performed by the user or inferred from user behavior (git logs, pdfs, pictures of notes, etc.).

## Features

- **Knowledge Tree Visualization**
  - Interactive tree-based UI for visualizing skill hierarchies
  - Background displays the full knowledge graph
  - Foreground shows current learning path and progress
  - Click on nodes to see skill subtrees

- **Multi-Modal Learning Tracking**
  - Save and organize learning resources (websites, notes, documents)
  - Integration with Git logs to track coding progress
  - Support for PDF documents and handwritten notes
  - GPT-powered search across all saved materials
  - NotebookLM notebook integration for interactive learning

- **Smart Progress Tracking**
  - Commit-style summaries for learning milestones
  - Automated progress inference from user activities
  - Memory system for tracking historical progress

- **Learning Views**
  - Challenge View: Practice exercises and assessments
  - Map View: Overall skill progression visualization
  - Instruction View: Detailed learning materials and guides


## Directory Structure

- `src/skillgraph/`: Contains all skillgraph related code


## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) for fast and easy package management

### Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:aryamanpandya99/skillgraph.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd skillgraph
   ```

4. **Install Dependencies**

   ```bash
   uv venv
   uv pip install .
   ```
