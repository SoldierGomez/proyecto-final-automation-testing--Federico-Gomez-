import pytest

from pages.post_api_page import PostsApi
from utils.logger import logger
import pytest_check as check


api= PostsApi()


def test_get_one_posts():
    logger.info("OBTENIENDO UN POST... ")
    
    response= api.get_one_post(1) #to do

    check.equal(
        response.status_code,
        200,
        "STATUS INCORRECTO."
    )
    
    body = response.json()
    check.equal(
        body["id"],
        1,#to do
        "ID NO COINCIDE."
    )

     
def test_posts():
    logger.info("Obteniendo Posts... ")
    response= api.get_posts()

    check.equal(
        response.status_code,
        200,
        "Status incorrecto."
    )
    posts= response.json()
    check.is_true(
        len(posts)>0,
        "No se obtivieron posts."
        )
    check.is_true(
        isinstance(posts,list),
        "La respuesta no es una lista"
    )

def test_create_post(posts_data):
    logger.info("CREANDO UN POST")
    response=api.create_posts(
        posts_data["title"],
        posts_data["body"],
        posts_data["userId"]
    )
    check.equal(
        response.status_code,
        201,
        "NO SE CREO EL POST"
    )

