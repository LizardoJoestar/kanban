from ._anvil_designer import LogoutScreenTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Startup

class LogoutScreen(LogoutScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Startup.startup()
    open_form("Index")
