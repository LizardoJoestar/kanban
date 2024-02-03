from ._anvil_designer import KanbanBoardTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..NewTaskModal import NewTaskModal

class KanbanBoard(KanbanBoardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def addTask_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # This just opens the new task modal
    newTaskModal = NewTaskModal()
    alert(newTaskModal, large=True, buttons=None)
