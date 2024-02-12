from ._anvil_designer import ProjectFrameTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ProjectFrame(ProjectFrameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Initial refresh
    self.refreshProjectList()
  
  def refreshProjectList(self):
    self.projectList_rp.items = anvil.server.call('getAllProjects')
    