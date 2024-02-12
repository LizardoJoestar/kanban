import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Documentation.DocFrame import DocFrame
from .AllProjects.ProjectFrame import ProjectFrame

"""
Globals module is a SINGLETON
Forms should only communicate to each other thru this singleton, that is,
passing data and calling functions between each other. 
Consider further implementing this later!
"""

########################################################################
# Global functions

# Current active project:
# Will be changed only by selecting another project in 'Project list' module

# Active project initialization
currentProject = None 
projects = anvil.server.call('getAllProjects')
if len(projects) != 0:
  currentProject = projects[0] # First project is default

# Global active project variable setter, by 'Project list' module
# def setCurrentProject(value):
#   currentProject = value

# def setCurrentToDefault():
#   currentProject = anvil.server.call('getAllProjects')[0]


########################################################################
# DocFrame functions

def setImgViewer(view):
  # set the image viewer
  # Get the last instance of Documentation module (anvil generates new instances
  # everytime you click away and return)
  # Then modify that instance as you wish
  DocFrame.instanceList[-1].docPreview_panel.clear()
  DocFrame.instanceList[-1].docPreview_panel.add_component(view)

def setNotImageNotice(notice):
  # If doc is not an image, display notice telling user to download instead
  DocFrame.instanceList[-1].docPreview_panel.clear()
  DocFrame.instanceList[-1].docPreview_panel.add_component(notice)

########################################################################
# ProjectCard functions

# def setActiveBanner(value):
#   ProjectFrame.instanceList[-1].activeProject.text = f"Active Project: {value}"