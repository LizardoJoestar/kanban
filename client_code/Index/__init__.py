from ._anvil_designer import IndexTemplate
from anvil import * # this imports all forms
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..KanbanBoard import KanbanBoard # if you want to initialize a form as an object, call it like this (go to upper directory and import)

class Index(IndexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.content_panel.add_component(KanbanBoard())
    
    # Set current project in view
    projectList = app_tables.project.search()

  def link_logout_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    open_form("LogoutScreen")

  def link_kanban_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Opens project's kanban board
    self.content_panel.clear() # clear main panel
    self.content_panel.add_component(KanbanBoard()) # open current kanban
