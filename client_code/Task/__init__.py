from ._anvil_designer import TaskTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Task(TaskTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def status_box_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
