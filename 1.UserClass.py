from locust import User, task, constant

class FirstTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print('Launching...111')
    
    @task
    def search(self):
        print('Searching...111')



class SecondTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print('Launching...222')
    
    @task
    def search(self):
        print('Searching...222')
    