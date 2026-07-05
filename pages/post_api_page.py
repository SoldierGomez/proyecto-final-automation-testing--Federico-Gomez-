import requests

class PostsApi:
    URL_BASE= "https://jsonplaceholder.typicode.com/"
    API_KEY=""

    def get_one_post(self,post_id):
        return requests.get(
            f"{self.URL_BASE}/posts/{post_id}"
            #, headers={"x-api-key":self.API_KEY} #para APIs privadas
        )
    def get_posts(self):
        return requests.get(
            f"{self.URL_BASE}/posts"
            #, headers={"x-api-key":self.API_KEY} #para APIs privadas
        )
    
    