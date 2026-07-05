import requests

class PostsApi:
    URL_BASE= "git "
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
    
    def create_posts(self,title,body,user_id):
        
        data={
            "title":title,
            "body":body,
            "userId":user_id
        }

        return requests.post(
            f"{self.URL_BASE}/posts",
            json=data
        )