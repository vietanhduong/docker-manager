# coding=utf-8
import logging
import json
import requests_unixsocket

from manager.utilities import const

__author__ = 'anh.dv'

from manager.utilities.common import convert_camel_to_snake

from manager.utilities.exceptions import BadRequestException

_logger = logging.getLogger(__name__)


class DockerManager(object):

    def __init__(self):
        self.__BASE_URL = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
        self.__session = requests_unixsocket.Session()

    def get_containers(self, container_id: str = None):
        response = self.__session.get(f"{self.__BASE_URL}/containers/json?all=1")
        ret = []
        if response.status_code == const.HTTP_200:
            res = response.json()
            ret = [self.__received_containers(container) for container in res]

        if container_id is not None:
            ret = [x for x in ret if container_id in x.get("id")]

        return ret

    def container_inspect(self, container_id: str):
        resp = self.__session.get(f'{self.__BASE_URL}/containers/{container_id}/json')
        if resp.status_code != const.HTTP_200:
            raise Exception(f'Inspect container {container_id} failed with code: {resp.status_code}')

        ret = convert_camel_to_snake(resp.json())

        return ret

    def container_stop(self, container_id: str):
        return self.__action_with_container("stop", container_id)

    def container_restart(self, container_id: str):
        return self.__action_with_container("restart", container_id)

    def container_kill(self, container_id: str):
        return self.__action_with_container("kill", container_id)

    def container_logs(self, container_id: str):
        """
        This method return a stream
        """
        self.__check_container_existed(container_id)

        response = self.__session.get(f"{self.__BASE_URL}/containers/{container_id}/logs?stderr=1&stdout=1&tail=all&follow=1",
                                      stream=True)
        is_tty_ = self.is_tty(container_id)
        if is_tty_:
            for line in response.iter_lines():
                yield line + b"\n"
        else:
            for line in response.iter_lines():
                yield line[8:] + b"\n"

    def events(self):
        """
        This method return a stream
        """
        response = self.__session.get(f"{self.__BASE_URL}/events", stream=True)
        for line in response.iter_lines():
            yield line + b"\n"

    def is_tty(self, container_id):
        container = self.container_inspect(container_id)
        config = container.get("config") or {}
        tty = config.get("tty")
        return tty if tty is not None else False

    def __action_with_container(self, action, container_id):
        self.__check_container_existed(container_id)
        response = self.__session.post(f"{self.__BASE_URL}/containers/{container_id}/{action}?t=1")
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
            "id": container.get("Id")[:12] or "",
            "name": (container.get("Names") or ["/"])[0][1:],
            "image": container.get("Image"),
            "ports": ports,
            "state": container.get("State"),
            "status": container.get("Status")
        }
