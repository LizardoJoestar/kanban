from ._anvil_designer import DocListTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..DocLink import DocLink
from ... import Globals

class DocList(DocListTemplate):
  def __init__(self, category, project, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.category = category
    self.project = project

    # Initial refresh
    self.refresh_doc_list()

    # set event handler for refresh from a link
    self.docList_rp.set_event_handler('x-deleted', self.refresh_doc_list)
    
  def refresh_doc_list(self, **event_args):
    # Set repeating panel items dictionary to be used by each doc link card
    self.docList_rp.items = anvil.server.call('getDocsByCategory', self.category, self.project)
