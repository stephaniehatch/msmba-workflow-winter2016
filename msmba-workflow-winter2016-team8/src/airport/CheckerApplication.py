'''
The Airport Check-in Desk Interface for the airport workflow
'''

from frontend.roleApplication import RoleApplication
from frontend.form import Type
from airport.AirportConstants import theflowname

class CheckerApplication(RoleApplication):

    def __init__(self):
        '''
        Declare this application to be part of a given work flow and specify its role in that workflow.
        '''
        # Declare this application to be part of a given workflow, and responsible for a given role:
        # !!! Modify the following to use the actual role name you need...
        super(CheckerApplication, self).__init__(theflowname, "checker") 
        
        # Declare any tasks that this role is able to perform:
        # !!! Modify to use actual task name and name_fields:
        self.register_sink_step("checkID", self.checks_information, name_fields=["sequence", "Name", "ID"])


    def checks_information(self, stepname, form):
        '''
        Defines the data entry form for the checker application.
        Appears after checker selects a pending order.
        '''
        # !!! Use one or more fields from order to define label...
        form.add_task_label(fields=["Name"]) 
        # !!! Add any static labels or fields you want to include in this form...

if __name__ == '__main__':
    #starts up the CheckerApplication:
    app = CheckerApplication()
    #Start interacting with the user:
    app.MainLoop()