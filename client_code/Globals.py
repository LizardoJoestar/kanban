import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# Current active project:
projects = app_tables.project.search()
currentProject = projects[0] # default first

# Other globals
kanban_types = ['backlog', 'progress', 'review', 'done']