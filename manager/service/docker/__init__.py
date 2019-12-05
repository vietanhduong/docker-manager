# coding=utf-8
import logging
import json
import requests_unixsocket

from manager.utilities import const

__author__ = 'anh.dv'

from manager.utilities.exceptions import BadRequestException

_logger = logging.getLogger(__name__)


class DockerManager(object):

    def __init__(self):
        self.__BASE_URL = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
        self.__session = requests_unixsocket.Session()

    def get_containers(self, container_id: str = None):
        response = self.__session.get(f"{self.__BASE_URL}/containers/json")
        ret = []
        if response.status_code == const.HTTP_200:
            res = response.json()
            ret = [self.__received_containers(container) for container in res]

        if container_id is not None:
            ret = [x for x in ret if container_id in x.get("id")]

        return ret

    @staticmethod
    def stream(function, args: tuple or list = None, kwargs: dict = None):
        args = args or ()
        kwargs = kwargs or {}
        while True:
            yield json.dumps(function(*args, **kwargs))

    def container_stop(self, container_id: str):
        return self.__action_with_container("stop", container_id)

    def container_restart(self, container_id: str):
        return self.__action_with_container("restart", container_id)

    def container_kill(self, container_id):
        return self.__action_with_container("kill", container_id)

    def __action_with_container(self, action, container_id):
        self.__check_container_existed(container_id)
        response = self.__session.post(f"{self.__BASE_URL}/containers/{container_id}/{action}?t=3")
        if response.status_code != const.HTTP_204:
            raise Exception(f"{action} container {container_id} failed: HTTP_CODE: {response.status_code}")

        return {
            "code": 200,
            "message": "Success"
        }

    def __check_container_existed(self, container_id):
        container = self.get_containers(container_id)
        if not container:
            raise BadRequestException(f"Container {container_id} does not exist")

    @staticmethod
    def __received_containers(container: dict) -> dict:
        ports = container.get("Ports") or []
        ports = [{
            "public": port.get("PublicPort"),
            "private": port.get("PrivatePort"),
            "type": port.get("Type")
        } for port in ports]
        return {
            "id": container.get("Id") or "",
            "name": (container.get("Names") or ["/"])[0][1:],
            "image": container.get("Image"),
            "ports": ports,
            "state": container.get("State"),
            "status": container.get("Status")
        }
