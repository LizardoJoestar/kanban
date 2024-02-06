from ._anvil_designer import KanbanBoardTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..NewTaskModal import NewTaskModal
from ..Globals import *

class KanbanBoard(KanbanBoardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # get active project from Globals module:
    self.project = currentProject

    # Initial refresh
    self.refresh_ui()

  def refresh_ui(self, **event_args):
    self.backlog_rp.items = app_tables.task.search(project=self.project, status="Backlog")
    self.inprogress_rp.items = app_tables.task.search(project=self.project, status="In-Progress")
    self.review_rp.items = app_tables.task.search(project=self.project, status="Review")
    self.done_rp.items = app_tables.task.search(project=self.project, status="Done")

  def addTask_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # This just opens the new task modal
    newTaskModal = NewTaskModal()
    alert(newTaskModal, large=True, buttons=None)
