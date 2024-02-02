from ._anvil_designer import IndexTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..KanbanBoard import KanbanBoard

class Index(IndexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(KanbanBoard())
    # Any code you write here will run before the form opens.
    # Minotaur hotel