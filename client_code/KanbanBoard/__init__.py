from ._anvil_designer import KanbanBoardTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..NewTaskModal import NewTaskModal
from ..Task import Task
from ..Globals import *
import datetime

class KanbanBoard(KanbanBoardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # get active project from Globals module:
    self.project = currentProject

    # Initial refresh
    self.refresh_kanban()

  def refresh_kanban(self, **event_args):
    self.backlog_rp.items = anvil.server.call('refreshKanban', self.project, "Backlog")
    self.inprogress_rp.items = anvil.server.call('refreshKanban', self.project, "In-Progress")
    self.review_rp.items = anvil.server.call('refreshKanban', self.project, "Review")
    self.done_rp.items = anvil.server.call('refreshKanban', self.project, "Done")

  
  def addTask_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # This just opens the new task modal
    newTaskModal = NewTaskModal()

    # Set due date default to today
    newTaskModal.dueDate_box.date = datetime.date.today()
    alert(newTaskModal, large=True, buttons=None)
