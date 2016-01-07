'''
Back end for the airport workflow, a thing of beauty made by team 8.

This file is where you "wire" together the steps in the process.
'''

# these next few lines import some of the WMP functions we will
# use in this file.
from backend.backend import Backend
from workflow.task import Task
from workflow.result import Result 
from workflow.flowData import Status
from airport.AirportConstants import theflowname

class AirportBackend(Backend):
    '''
    The AirportBackend "class" is a collection of the "methods" (functions) that do the actual
    wiring together of the steps in the process.
    
    A back end will always include the methods __init__ and wire and will also include a method
    to handle each event that occurs in the process.
    '''
   
    def __init__(self): 
        # Specify the workflow name:       
        Backend.__init__(self, theflowname)  

    def wire(self):
        '''
        The wire method is where we tell MWP which tasks to keep track of.
        To register a task, you will need to add a line of code that looks
        like this:
        self.register_result_listener("RoleName", "TaskName", self.method_name)
        Where: RoleName is the person who did the task
               TaskName is the name of the task they did
               self.method_name refers to a method in this class which should respond to
                                the task being completed.
        '''
        self.register_result_listener("desk", "enterID", self.enter_information)
        self.register_result_listener("checker", "checkID", self.checks_information)
        self.register_result_listener("TSA", "frisk", self.frisk_customer_frantically)
        self.register_result_listener("printer", "givetix", self.return_tix)



    def enter_information(self, results):

        for result in results:  # repeat the following actions for each result
            task = Task.construct_from_result(result,"checker", "checkID") 
            self.workflow.add(task) # add the new task to the workflow
            self.workflow.update_status(result, Status.COMPLETE)

    def checks_information(self, results):

        for result in results:  # repeat the following actions for each result
            if result.data['IDfit?'] == 1:
                task = Task.construct_from_result(result, "printer", "givetix")
            else:
                task = Task.construct_from_result(result, "TSA", "frisk")
            self.workflow.add(task)
            self.workflow.update_status(result, Status.COMPLETE) 


    def frisk_customer_frantically(self, results):

        for result in results:  # repeat the following actions for each result
            self.workflow.update_status(result, Status.COMPLETE)
            task = Task.construct_from_result(result,"printer", "givetix") 
            self.workflow.add(task) # add the new task to the workflow
            self.workflow.update_status(result, Status.COMPLETE)
            
    def return_tix(self, results):

        for result in results:  # repeat the following actions for each result
            self.workflow.update_status(result, Status.COMPLETE)

'''
Finally, this last bit of code is fine as it is and you do not need to change it, Stephanie.
'''
if __name__ == '__main__':
    backend = AirportBackend()