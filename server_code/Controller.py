import anvil.tables as tables
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def addTask(name, desc, dueDate, status, project):
  app_tables.task.add_row(name=name, description=desc, dueDate=dueDate, status=status, project=project)

@anvil.server.callable
def deleteTask(taskID):
  if app_tables.task.get_by_id(taskID) is not None:
    app_tables.task.get_by_id(taskID).delete()

@anvil.server.callable
def updateTask(taskID, name, desc, dueDate, status):
  app_tables.task.get_by_id(taskID)['name'] = name
  app_tables.task.get_by_id(taskID)['description'] = desc
  app_tables.task.get_by_id(taskID)['dueDate'] = dueDate
  app_tables.task.get_by_id(taskID)['status'] = status