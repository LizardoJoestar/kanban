import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

kanban_types = ['backlog', 'progress', 'review', 'done']
projectList = app_tables.project.search()