from ._anvil_designer import ProjectCardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ProjectEditModal import ProjectEditModal
from ... import Globals

class ProjectCard(ProjectCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Set project card info
    self.projectLink.text = self.item['name']
    self.start_label.text = f"Started: {str(self.item['started'])}"

    if self.item['ended'] != None: # if project hasn't ended, either display or not end date
      self.end_label.text = f"Ended: {str(self.item['ended'])}"
    else:
      self.end_label.text = "Ended:"

  def edit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    editModal = ProjectEditModal(self.item)
    res = alert(editModal, large=True, buttons=None)
    if res == None:
      self.parent.parent.refreshProjectList()
      # Globals.setActiveBanner()
  
  def projectLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Set the active project
    Globals.currentProject = self.item
    self.parent.parent.activeProject.text = f"Active Project: {Globals.currentProject['name']}"

  def delete_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = alert(
          content="This will delete the project and all its associated tasks and documentation. It cannot be undone. If you are sure, click DELETE PROJECT.\nIf you prefer not to delete, click Cancel or anywhere else on the screen.",
          title="WARNING",
          large=True,
          buttons=[
            ("DELETE PROJECT", True),
            ("Cancel", False)
          ])

    # Ask again to be sure
    if result:
      res = alert(
          content="Deleting a project also deletes all its tasks and documentation. It cannot be undone. Are you sure?",
          title="ARE YOU SURE?",
          large=True,
          buttons=[
            ("YES, DELETE", True),
            ("Cancel", False)
          ])

      if res:
        self.deleteALL()

  def deleteALL(self):
    pass