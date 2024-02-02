import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# You can define variables and functions here, and use them from any form. 

def startup():
  user = anvil.users.login_with_form()
  open_form("Index")
