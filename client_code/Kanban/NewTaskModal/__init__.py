from ._anvil_designer import NewTaskModalTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Globals
import datetime

class NewTaskModal(NewTaskModalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Collect data from modal
    name = self.name_box.text
    description = self.description_box.text
    dueDate = self.dueDate_box.date
    status = self.status_box.selected_value

    # Send to database as a new row
    # 'currentProject' is from Globals module
    anvil.server.call('addTask', name, description, dueDate, status, Globals.currentProject)
    self.clearModalFields()

    # Every time a task is added, kanban board refreshes in the background
    # Task modal remains in case user wants to add more tasks, until clicked away
    get_open_form().refreshKanban() # Gets last opened form (Index) (check open_form details for more info)
  
  def clearModalFields(self):
    self.name_box.text = ""
    self.description_box.text = ""
    self.dueDate_box.date = datetime.date.today()
    self.status_box.selected_value = "Backlog"
    