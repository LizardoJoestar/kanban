from ._anvil_designer import TaskTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Task(TaskTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Set the task fields to the 'item' dictionary fields for each item
    # 'self.item' is inherited from parent form (e.g., KanbanBoard)
    self.name_box.text = self.item['name']
    self.description_box.text = self.item['description']
    self.dueDate_box.text = self.item['dueDate']
    self.status_box.selected_value = self.item['status']

  def status_box_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
