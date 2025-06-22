from graphviz import Digraph

# Use Case Diagram
use_case = Digraph('Use Case Diagram', format='png')
use_case.attr(rankdir='LR')

# Actors
use_case.node('User', shape='actor')
use_case.node('Admin', shape='actor')
use_case.node('System', shape='rectangle', style='filled', fillcolor='lightgray')

# Use Cases
use_case.node('Register/Login', shape='ellipse')
use_case.node('Search Books', shape='ellipse')
use_case.node('View Recommendations', shape='ellipse')
use_case.node('Rate Books', shape='ellipse')
use_case.node('Add to Favorites', shape='ellipse')
use_case.node('Manage Books', shape='ellipse')
use_case.node('Manage Users', shape='ellipse')

# Relationships
use_case.edge('User', 'Register/Login')
use_case.edge('User', 'Search Books')
use_case.edge('User', 'View Recommendations')
use_case.edge('User', 'Rate Books')
use_case.edge('User', 'Add to Favorites')
use_case.edge('Admin', 'Manage Books')
use_case.edge('Admin', 'Manage Users')
use_case.edge('System', 'View Recommendations')

# Render Use Case Diagram
use_case_path = '/mnt/data/use_case_diagram.png'
use_case.render(use_case_path, format='png', cleanup=True)

use_case_path
