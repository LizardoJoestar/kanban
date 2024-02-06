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
def deleteTask(taskID):
  if app_tables.task.get_by_id(taskID) is not None:
    app_tables.task.get_by_id(taskID).delete()

@anvil.server.callable(require_user=True)
def updateTask(taskID, name, desc, dueDate, status):
  app_tables.task.get_by_id(taskID)['name'] = name
  app_tables.task.get_by_id(taskID)['description'] = desc
  app_tables.task.get_by_id(taskID)['dueDate'] = dueDate
  app_tables.task.get_by_id(taskID)['status'] = status

@anvil.server.callable(require_user=True)
def getTasks(project):
  # Get all tasks associated with a single project
  return app_tables.task.get(project=project)


# CRUD functions for projects