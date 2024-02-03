from ._anvil_designer import NewTaskModalTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class NewTaskModal(NewTaskModalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Collect data from modal
    name = self.name_box.text
    description = self.description_box.text
    dueDate = self.dueDate_box.text
    status = self.status_box.selected_value

    # Send to database as a new row
    anvil.server.call('addTask', name, description, dueDate, status, self.item)

  def cancel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    
