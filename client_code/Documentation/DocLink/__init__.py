from ._anvil_designer import DocLinkTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ImgPreview import ImgPreview
from ..Notice import Notice
import anvil.media
from ... import Globals
import re

class DocLink(DocLinkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.title_link.text = self.item['name']

  def download_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    id = self.item.get_id()
    doc = anvil.server.call('getDocumentByID', id)
    anvil.media.download(doc) # Will download file to user's browser

  def delete_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    id = self.item.get_id()
    anvil.server.call('deleteDocumentByID', id)
    Notification("Document deleted.").show()

    # Refresh doc list
    self.parent.raise_event('x-deleted')

  def title_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    id = self.item.get_id()
    doc = anvil.server.call('getDocumentByID', id)

    # Check that doc is an image, to avoid unnecessarily instancing the viewer
    if re.search("image\/", doc.content_type) != None:
      view = ImgPreview()
      view.img_panel.source = doc
      Globals.setImgViewer(view)
    else:
      Globals.setNotImageNotice(Notice())

    
