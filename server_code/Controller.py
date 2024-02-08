import anvil.users
import anvil.tables as tables
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

########################################################################
# CRUD functions for Kanban tasks

@anvil.server.callable(require_user=True)
def addTask(name, desc, dueDate, status, project):
  app_tables.task.add_row(name=name, description=desc, dueDate=dueDate, status=status, project=project)

@anvil.server.callable(require_user=True)
def deleteTask(row):
  if row is not None:
    row.delete()

@anvil.server.callable(require_user=True)
def updateTask(row_id, value):
  row = app_tables.task.get_by_id(row_id)
  row['status'] = value

@anvil.server.callable(require_user=True)
def updateTaskName(row_id, value):
  row = app_tables.task.get_by_id(row_id)
  row['name'] = value

@anvil.server.callable(require_user=True)
def updateTaskDescription(row_id, value):
  row = app_tables.task.get_by_id(row_id)
  row['description'] = value

@anvil.server.callable(require_user=True)
def updateTaskDueDate(row_id, value):
  row = app_tables.task.get_by_id(row_id)
  row['dueDate'] = value

@anvil.server.callable(require_user=True)
def getTasks(project):
  # Get all tasks associated with a single project
  return app_tables.task.get(project=project)

@anvil.server.callable(require_user=True)
def refreshKanban(project, status):
  return app_tables.task.search(project=project, status=status)
  
########################################################################
# CRUD functions for projects

@anvil.server.callable(require_user=True)
def getAllProjects():
  return app_tables.project.search()


########################################################################
# CRUD functions for categories

@anvil.server.callable(require_user=True)
def getAllCategories(project):
  # List comprehension, from iterable 'search()' select only the names column
  return [r['name'] for r in app_tables.category.search(project=project)]

@anvil.server.callable(require_user=True)
def addCategory(name, project):
  pass