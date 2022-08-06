from locust import HttpUser, task, between


class Jsonflix(HttpUser):
    wait_time = between(1, 5)

    @task
    def all_page(self):
        self.client.get(url='/api/v1/all')

    @task
    def docs_page(self):
        self.client.get(url='/api/v1/docs')

    @task
    def search_page(self):
        self.client.get(url='/api/v1/?type=tv_show&country=kr&description=mafia')
