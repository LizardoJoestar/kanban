from ._anvil_designer import NewDocModalTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Globals
import datetime

class NewDocModal(NewDocModalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.file = None # Local file object, placeholder. Only in browser
    self.addDoc_btn.enabled = False # Start with add button disabled

  def file_loader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    # Only uploads to browser. Doesn't send to database yet
    # Check if category isn't empty
    if self.category_box.selected_value != None:
      self.file = file # set local to uploaded file
      self.filename.text = self.file.name # display selected file's name
      alert("Document uploaded. Click Add to confirm and add to project.")
      self.addDoc_btn.enabled = True # enable to upload to server
    else:
      alert("Please select a category. If there aren't any, please create one.")

  def addDoc_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.file != None:
      anvil.server.call('addDocument', self.file.name, self.category_box.selected_value, datetime.date.today(), self.file, Globals.currentProject)
  
      # Reset file name and file placeholder, then notify
      self.clearFields()
      Notification("Document added to project.").show()
      self.addDoc_btn.enabled = False # disable again until another file is loaded
    else:
      Notification("No file selected.").show()

  def cancel_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Reset file placeholder and file name
    self.clearFields()
    self.addDoc_btn.enabled = False
    Notification("Document upload canceled.").show()

  def clearFields(self, **event_args):
    self.file = None
    self.filename.text = "..."
    self.file_loader.clear()
