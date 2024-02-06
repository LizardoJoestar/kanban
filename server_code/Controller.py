import anvil.users
import anvil.tables as tables
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# CRUD functions for Kanban tasks

@anvil.server.callable(require_user=True)
def addTask(name, desc, dueDate, status, project):
  app_tables.task.add_row(name=name, description=desc, dueDate=dueDate, status=status, project=project)

@anvil.server.callable(require_user=True)
def deleteTask(row):
  if row is not None:
    row.delete()

@anvil.server.callable(require_user=True)
def updateTask(row):
  if row is not None:
    app_tables.task.

@anvil.server.callable(require_user=True)
def getTasks(project):
  # Get all tasks associated with a single project
  return app_tables.task.get(project=project)

@anvil.server.callable(require_user=True)
def refreshKanban(project, status):
  return app_tables.task.search(project=project, status=status)
  
# CRUD functions for projects