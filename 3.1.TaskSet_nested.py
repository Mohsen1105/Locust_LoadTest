from locust import TaskSet, constant, task, HttpUser
import random

# nested TaskSet
# in a class we have another task class

class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        response = self.client.get("/200")
        print('Get status of 200')
    
    # ****************************************************************************
    # The problem of this definition is when fall in the nested clss never go back
    # for solve this we must use :
    # self.interrupt(reschedule=False)
    # or two classes
    # ****************************************************************************
    @task
    class MyAnotherHTTPCat(TaskSet):

        @task
        def get_500_status(self):
            self.client.get("/500")
            print("Get Status of 500")
            # for get back to parent class
            self.interrupt(reschedule=False)
    


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat]
    wait_time = constant(1)
