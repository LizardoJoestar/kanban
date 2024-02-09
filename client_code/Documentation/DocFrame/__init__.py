from ._anvil_designer import DocFrameTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..NewCategoryModal import NewCategoryModal
from ..NewDocModal import NewDocModal
from ..DocList import DocList
from ... import Globals

class DocFrame(DocFrameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Get active project from Globals module
    self.project = Globals.currentProject

    # Initial refresh. Will execute everytime module es added/created
    self.refresh_docs()

  def refresh_docs(self, **event_args):
    # Set title in accordance with active project
    self.title.text = self.project['name'] + " - Documentation"

    # Fill category dropdown with categories associated with active project
    self.category_box.items = anvil.server.call('getAllCategories', self.project)

  def refresh_list(self, **event_args):
    # This needs to be refreshed separately, by this form and others independently
    self.docList_panel.add_component(DocList(self.category_box.selected_value, self.project))
  
  def categoryModal_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    modal = NewCategoryModal()     
    modal.category_box.items = anvil.server.call('getAllCategories', self.project)
    alert(modal, large=True, buttons=None)

  def newDocModal_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    modal = NewDocModal()
    modal.category_box.items = anvil.server.call('getAllCategories', self.project)
    alert(modal, large=True, buttons=None)

  def category_box_change(self, **event_args):
    """This method is called when an item is selected"""
    self.refresh_list()
