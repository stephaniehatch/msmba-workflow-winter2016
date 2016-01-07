'''
The Airport Check-in Desk Interface for the airport workflow
This is where you define the fields that appear on the screen (application) the barista
sees and tell WMP how this application (user interface) fits into the overall workflow.
'''

from frontend.roleApplication import RoleApplication
from frontend.form import Type
from airport.AirportConstants import theflowname

class DeskApplication(RoleApplication):
    '''
    The BaristaApplication "class" is a collection of the "methods" (functions) that 
    define the elements of the order taker application.  
    
    An application will always include the method __init__ and at least one
    method to define a form that the user of this application will use.
    '''

    def __init__(self):
        '''
        Declare this application to be part of a given work flow and specify its role in that workflow.
        '''
        # Declare this application to be part of a given workflow, and responsible for a given role:
        # !!! Modify the following to use the actual role name you need...
        super(BaristaApplication, self).__init__(theflowname, "Barista") 
        
        # Declare any tasks that this role is able to perform:
        # !!! Modify to use actual task name and name_fields:
        self.register_sink_step("PrepareDrink", self.prepare_drink_form_creator, name_fields=["sequence", "Drank"])


    def prepare_drink_form_creator(self, stepname, form):
        '''
        Defines the data entry form for the barista application.
        This form appears once the barista selects one of the pending orders from a list.
        '''
        # !!! Use one or more fields from order to define label...
        form.add_task_label(fields=["Name"]) 
        # !!! Add any static labels or fields you want to include in this form...

if __name__ == '__main__':
    #starts up the BaristaApplication:
    app = BaristaApplication()
    #Start interacting with the user:
    app.MainLoop()