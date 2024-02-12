from ._anvil_designer import ProjectEditModalTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ProjectEditModal(ProjectEditModalTemplate):
  def __init__(self, project, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.project = project # get project row for that card, NOT global
    self.resetFields() # Set initial fields with existing project info

  def edit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    newName = self.name_box.text
    newStart = self.startDate_box.date
    newEnd = self.endDate_box.date

    if newName != "" and newStart != None:
      # check duplicates
      matches = self.checkDuplicates(newName)
      if len(matches) == 0:
        id = self.project.get_id()
        anvil.server.call('updateProject', id, newName, newStart, newEnd)
        alert("Project information updated.")
        self.resetFields()
      else:
        alert("A project with that name already exists, or the start date is empty. Please use another name or enter a start date.")
        self.resetFields()
    else:
      alert("Name and start date fields cannot be empty.")

  def resetFields(self):
    id = self.project.get_id()
    row = anvil.server.call('getProjectByID', id)

    # Set fields with existing project info
    self.name_box.text = row['name']
    self.startDate_box.date = row['started']
    self.endDate_box.date = row['ended']

  def checkDuplicates(self, name):
    # Will not return duplicates for its own, only checks in other projects
    # that aren't the selected one
    list = anvil.server.call('getProjectByName', name)
    id = self.project.get_id()
    results = []
    for item in list:
      if item.get_id() != id:
        results.append(item)
    return results