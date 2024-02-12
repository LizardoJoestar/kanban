from ._anvil_designer import IndexTemplate
from anvil import * # this imports all forms
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# if you want to initialize a form as an object, call it like this
# (go to upper directory and import)
from ..Kanban.KanbanBoard import KanbanBoard
from ..Documentation.DocFrame import DocFrame
from ..NoProjectNotice import NoProjectNotice
from .. import Globals

class Index(IndexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Check the active project
    if Globals.currentProject != None:
      # Open kanban by default
      self.content_panel.add_component(KanbanBoard())
    else:
      # When no projects are in the database, display notice
      self.content_panel.add_component(NoProjectNotice())

  def refreshKanban(self, **event_args):
    # Delete current Kanban and add it again
    # KanbanBoard will appear updated per its initialization
    self.content_panel.clear()
    self.content_panel.add_component(KanbanBoard())

  
  # LINKS:

  def link_logout_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Logs out current user, gives option to return to login screen
    anvil.users.logout()
    open_form("LogoutScreen")

  def link_kanban_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Opens project's kanban board
    self.content_panel.clear() # clear main panel
    self.content_panel.add_component(KanbanBoard()) # open current kanban

  def link_users_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Opens user management panel
    self.content_panel.clear() # clear main panel

  def link_docs_click(self, **event_args):
    """This method is called when the link is clicked"""
    # Opens documentation management panel
    self.content_panel.clear()
    self.content_panel.add_component(DocFrame())
