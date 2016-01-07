'''
The Order Taker User Interface for the coffee bar workflow (Winter Intensives Lab 5)

This is where you define the fields that appear on the screen (application) the order
taker sees and tell WMP how this application (user interface) fits into the overall
workflow.

Note:  the comments here assume you have already read through the comments
in CoffeeBackend.py and made your edits there.
'''

# these next few lines import some of the WMP functions we will
# use in this file.
from frontend.roleApplication import RoleApplication
from frontend.form import Type
from airport.AirportConstants import theflowname

class TSAApplication(RoleApplication):
    '''
    The OrderTakerApplication "class" is a collection of the "methods" (functions) that 
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
        super(TSAApplication, self).__init__(theflowname, "TSA") 
        # Declare any tasks that this role is able to perform:
        # !!! Modify to use actual name for this task...
        self.register_sink_step("frisk", self.frisk_customer_frantically, name_fields=["sequence", "Name"]) 

    def frisk_customer_frantically(self, stepname, form):
        '''
        This method does the actual work of building the user interface.
        '''
        # !!! improve this text...
        form.add_field(Type.SHORTSTRING, "Suspect Name")
        form.add_field(Type.CHOICE, "Type of Inspection Required", choices=['Full Cavity Search','Breathalyzer','Light Petting','Rhino Tranquilizer','Disarming','I just wanted to talk to them, their pretty.'])
        form.add_static_label('Individual presented with:')
        form.add_field(Type.BOOLEAN, "Intoxication") 
        form.add_field(Type.BOOLEAN, "Terroristic Thoughts")
        form.add_field(Type.BOOLEAN, "OLD")
        form.add_field(Type.BOOLEAN, "Weapons")
        form.add_field(Type.BOOLEAN, "Smelliness")
        form.add_field(Type.BOOLEAN, "Wearing fake mustache")
        form.add_field(Type.BOOLEAN, "Wearing night-time glasses during the day")
        form.add_field(Type.BOOLEAN,'Should they be put on the no fly list?')
        form.add_field(Type.SHORTSTRING, "Inspected by:")
        form.add_field(Type.LONGSTRING, "Additional Notes")
        form.add_static_label("Sexual Harassment will not be tolerated by the TSA.")        
        # !!! Add at least two fields here, along with any additional static labels you need...

if __name__ == '__main__':
    #starts up the TSAApplication:
    app = TSAApplication()
    #Start interacting with the user:
    app.MainLoop()