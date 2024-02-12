from ._anvil_designer import NewProjectFrameTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime
from ... import Globals

class NewProjectFrame(NewProjectFrameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.startDate_box.date = datetime.date.today() # start date default is current date

  def add_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    start = self.startDate_box.date

    if name != "":
        # Check duplicate projects first
        if len(anvil.server.call('getProjectByName', name)) == 0:
          anvil.server.call('addNewProject', name, start)
    
          # Notify and reset fields
          alert(f"Project {name} has been added. You can now manage its kanban board and documentation.")
          self.resetFields()

          # If there weren't any projects in database (and now it's one), set current to this
          if len(anvil.server.call('getAllProjects')) == 1:
            Globals.currentProject = anvil.server.call('getAllProjects')[0] # VERY IMPORTANT, BEST TO SET CURRENT DIRECTLY
            # print("Current: " + str(Globals.currentProject))
            # print("Projects table: " + str([r['name'] for r in anvil.server.call('getAllProjects')]))
        else:
          alert("A project with that name already exists. Please use another name.")
          self.resetFields()
    else:
      alert("Project name cannot be empty, please enter one.")

  def resetFields(self):
    self.name_box.text = ""
    self.startDate_box.date = datetime.date.today()