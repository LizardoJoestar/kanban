from ._anvil_designer import TaskTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

class Task(TaskTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Set the task fields to the 'item' dictionary fields for each item
    # 'self.item' is inherited from parent form (e.g., KanbanBoard)
    # Each self.item is a task obtained from the database
    self.name_box.text = self.item['name']
    self.description_box.text = self.item['description']
    self.dueDate_box.date = self.item['dueDate']
    self.status_box.selected_value = self.item['status']

  def status_box_change(self, **event_args):
    """This method is called when an item is selected"""
    # If a task's status was changed, update the kanban board
    # to show its new position in the board/progress
    newStatus = self.status_box.selected_value # get new status value
    id = self.item.get_id() # get task id
    anvil.server.call('updateTask', id, newStatus) # update in the database

    # Refresh kanban board
    get_open_form().refreshKanban()
    

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Delete a task from the database, per row
    anvil.server.call('deleteTask', self.item)
    notif = Notification("Task deleted.")
    notif.show() # 2 seconds

    # Refresh kanban board
    get_open_form().refreshKanban()

  def name_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    # Doesn't refresh board, only updates database
    new = self.name_box.text
    id = self.item.get_id()
    anvil.server.call('updateTaskName', id, new)

  def description_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    new = self.description_box.text
    id = self.item.get_id()
    anvil.server.call('updateTaskDescription', id, new)

  def dueDate_box_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    new = self.dueDate_box.date
    id = self.item.get_id()
    anvil.server.call('updateTaskDueDate', id, new)


