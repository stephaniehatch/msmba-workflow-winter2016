'''
The Airport Check-in Desk Interface for the airport workflow
'''

from frontend.roleApplication import RoleApplication
from frontend.form import Type
from airport.AirportConstants import theflowname


class CheckerApplication(RoleApplication):
    """ The Checker User Interface """

    def __init__(self):
        super(CheckerApplication, self).__init__(theflowname, "Checker");
        self.register_transition_step("checkID", self.does_ID_fit_form_creator, name_fields=["sequence"])


    def does_ID_fit_form_creator(self, stepname, form):
        # form.add_task_label(fields=["Name", "ID"]);
        form.add_field(Type.BOOLEAN, "IDfit");
  
  


if __name__ == '__main__':
    #starts up the CheckerApplication:
    app = CheckerApplication()
    #Start interacting with the user:
    app.MainLoop()