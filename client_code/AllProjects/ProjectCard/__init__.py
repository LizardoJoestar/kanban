from ._anvil_designer import ProjectCardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ProjectEditModal import ProjectEditModal

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

  def projectLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
