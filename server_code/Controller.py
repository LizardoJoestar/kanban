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
def deleteTaskByProject(project):
  rows = app_tables.task.search(project=project)
  for row in rows:
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

@anvil.server.callable(require_user=True)
def getProjectByName(name):
  return app_tables.project.search(name=name)

@anvil.server.callable(require_user=True)
def getProjectByID(row_id):
  return app_tables.project.get_by_id(row_id)

@anvil.server.callable(require_user=True)
def addNewProject(name, start):
  app_tables.project.add_row(name=name, started=start) # Ended is none at first

@anvil.server.callable(require_user=True)
def updateProject(row_id, name, start, end):
  row = app_tables.project.get_by_id(row_id)
  row['name'] = name
  row['started'] = start
  row['ended'] = end

@anvil.server.callable(require_user=True)
def deleteProject(row):
  if row is not None:
    row.delete()

########################################################################
# CRUD functions for categories

@anvil.server.callable(require_user=True)
def getAllCategories(project):
  # List comprehension, from iterable 'search()' select only the names column
  # Get all categories from a single project
  return [r['name'] for r in app_tables.category.search(project=project)]

@anvil.server.callable(require_user=True)
def getCategories(name, project):
  # Return all categories that match same name
  return app_tables.category.search(name=name, project=project)

@anvil.server.callable(require_user=True)
def addCategory(name, project):
  app_tables.category.add_row(name=name, project=project)

@anvil.server.callable(require_user=True)
def deleteCategory(name, project):
  row = app_tables.category.get(name=name, project=project)
  if row is not None:
    row.delete()

########################################################################
# CRUD functions for documentation

@anvil.server.callable(require_user=True)
def addDocument(name, category, created, doc, project):
  app_tables.document.add_row(name=name, category=category, created=created, document=doc, project=project)

@anvil.server.callable(require_user=True)
def getDocsByCategory(category, project):
  return app_tables.document.search(category=category, project=project)

@anvil.server.callable(require_user=True)
def getDocumentByID(row_id):
  return app_tables.document.get_by_id(row_id)['document']

@anvil.server.callable(require_user=True)
def deleteDocsByCategory(category, project):
  for row in app_tables.document.search(category=category, project=project):
    row.delete()

@anvil.server.callable(require_user=True)
def deleteDocumentByID(row_id):
  row = app_tables.document.get_by_id(row_id)
  if row is not None:
    row.delete()

@anvil.server.callable(require_user=True)
def deleteDocsByProject(project):
  for row in app_tables.document.search(project=project):
    row.delete()