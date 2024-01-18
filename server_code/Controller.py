import anvil.tables as tables
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

def addTask(name, description, dueDate, status, project):
  app_tables.task.add_row(name=name, description=description, dueDate=dueDate, status=status, project=project)
