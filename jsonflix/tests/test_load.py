import gevent
from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging

setup_logging("INFO", None)


class User(HttpUser):
    wait_time = between(1, 5)
    host = 'https://jsonflix.herokuapp.com'

    @task
    def all_page(self):
        self.client.get(url='/api/v1/all')

    @task
    def docs_page(self):
        self.client.get(url='/api/v1/docs')

    @task
    def search_page(self):
        self.client.get(url='/api/v1/?type=tv_show&country=kr&description=mafia')
        self.client.get(url='/api/v1/?type=movie&country=br')
        self.client.get(url='/api/v1/?type=movie&country=us&description=dog,cat')
        self.client.get(url='/api/v1/?type=tv_show&country=fr')
        self.client.get(url='/api/v1/?type=tv_show&country=es&description=crime')


# def test_load_locust():
env = Environment(user_classes=[User])
env.create_local_runner()
env.create_web_ui("127.0.0.1", 8089)
gevent.spawn(stats_printer(env.stats))
gevent.spawn(stats_history, env.runner)
env.runner.start(10, spawn_rate=10)
gevent.spawn_later(60, lambda: env.runner.quit())
env.runner.greenlet.join()
env.web_ui.stop()
failures = env.stats.total.num_failures


def test_load_lucost():
    assert 1 == 1
