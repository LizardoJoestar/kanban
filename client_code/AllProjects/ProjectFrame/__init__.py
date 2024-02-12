from ._anvil_designer import ProjectFrameTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Globals

class ProjectFrame(ProjectFrameTemplate):
  instanceList = []
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.instanceList.append(self)
    self.init_components(**properties)
    
    # Initial refresh
    self.refreshProjectList()
  
  def refreshProjectList(self):
    self.activeProject.text = f"Active project: {Globals.currentProject['name']}"
    
    if Globals.currentProject != None:
      self.projectList_rp.items = anvil.server.call('getAllProjects')
    