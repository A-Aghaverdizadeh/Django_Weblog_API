from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    def on_start(self):
        url = "jwt/create"
        response = self.client.post(url, data={
            "email": "admin@gmail.com",
            "password": "Aa13311331@"
            }).json()
        self.client.headers = {"Authorization": f"Bearer {response.get('access', None)}"}

    @task
    def get_posts(self):
        url = "blog/api/v1/post/"
        self.client.get(url)

    @task
    def get_category(self):
        url = "blog/api/v1/category/"
        self.client.get(url)
