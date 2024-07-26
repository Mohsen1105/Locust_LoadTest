from locust import SequentialTaskSet, constant, task, HttpUser


class MySeqTask(SequentialTaskSet):

    @task
    def get_status(self):
        response = self.client.get("/200")
        print('Get status of 200')


    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get Status of 500")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySeqTask]
    wait_time = constant(1)
