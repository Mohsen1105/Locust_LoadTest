from locust import TaskSet, constant, task, HttpUser
import random

# Two Class TaskSet
# we have two task class

class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        response = self.client.get("/200")
        print('Get status of 200')

        self.interrupt(reschedule=False)
    


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get Status of 500")
        # for get back to parent class
        self.interrupt(reschedule=False)
    


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat, MyAnotherHTTPCat]
    wait_time = constant(1)
