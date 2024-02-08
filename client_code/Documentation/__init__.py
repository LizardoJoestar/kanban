from ._anvil_designer import DocumentationTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Globals import *

class Documentation(DocumentationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Get active project from Globals module
    self.project = currentProject

    # Initial refresh. Will execute everytime module es added/created
    self.refresh_docs()

  def refresh_docs(self, **event_args):
    # Set title in accordance with active project
    self.title.text = self.project['name'] + " - Documentation"