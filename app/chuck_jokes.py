import requests

class ChuckNorris:

    def __init__(self):
        self.random_joke_url = "https://api.chucknorris.io/jokes/random"
        self.categories_url = "https://api.chucknorris.io/jokes/categories"
        self.category_joke_url = "https://api.chucknorris.io/jokes/random?category=<category>"
        self.query_joke_url = "https://api.chucknorris.io/jokes/search?query=<query>"

    def get_random_joke(self):
        response = requests.get(self.random_joke_url)
        return response.status_code, response.json()

    def get_all_categories(self):
        response = requests.get(self.categories_url)
        return response.status_code, response.json()

    def get_category_joke(self, category):
        category_joke_url = self.category_joke_url.replace("<category>", category)
        response = requests.get(category_joke_url)
        return response.status_code, response.json()

    def query_joke(self, query):
        query_joke_url = self.query_joke_url.replace("<query>", query)
        response = requests.get(query_joke_url)
        return response.status_code, response.json()

