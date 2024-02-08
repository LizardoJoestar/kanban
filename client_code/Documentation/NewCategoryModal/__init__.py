from ._anvil_designer import NewCategoryModalTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Globals

class NewCategoryModal(NewCategoryModalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Add a new category
    if self.addCategory_box.text != "":
      new = self.addCategory_box.text
      duplicates = anvil.server.call('getCategories', new, Globals.currentProject)
      
      if len(duplicates) == 0:
        # Check there aren't any duplicates
        anvil.server.call('addCategory', new, Globals.currentProject)
        Notification("Category added").show()
        self.addCategory_box.text = ""
        
        # Refresh category dropdown list
        self.category_box.items = anvil.server.call('getAllCategories', Globals.currentProject)
      else:
        # Clear field for another input and notify
        self.addCategory_box.text = ""
        alert("Category already exists. Try another name.")
      
    else:
      alert("New category field is empty, please add one.")
      
  def delete_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.category_box.selected_value != None:
      matchingDocs = anvil.server.call('getDocsByCategory', self.category_box.selected_value, Globals.currentProject)
      if len(matchingDocs) == 0:
        name = self.category_box.selected_value
        anvil.server.call('deleteCategory', name, Globals.currentProject)
        
        # Refresh category dropdown list
        self.category_box.items = anvil.server.call('getAllCategories', Globals.currentProject)
        Notification("Category deleted.").show()
      else:
        result = alert(
          content="This category already contains documentation. Please delete any existing documents before deleting this category.\nIf you wish to delete all associated documents, click DELETE. If not, click Cancel.",
          title="WARNING",
          large=True,
          buttons=[
            ("DELETE", True),
            ("Cancel", False)
          ])

        if 
    else:
      alert("Please select a category to delete.")
    
