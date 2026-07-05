import pytest

from pages.post_api_page import PostsApi
from utils.logger import logger
import pytest_check as check


api= PostsApi()


def test_get_one_posts():
    logger.info("OBTENIENDO UN POST ")
    
    response= api.get_one_post(1) 

    check.equal(
        response.status_code,
        200,
        "STATUS INCORRECTO"
    )
    
    body = response.json()
    check.equal(
        body["id"],
        1,
        "ID NO COINCIDE"
    )
