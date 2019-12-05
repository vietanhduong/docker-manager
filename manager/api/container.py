# coding=utf-8
import logging
import flask_restplus as _fr
from flask import Response

from manager.utilities.namespace import Namespace
from manager.service import docker as DockerService

__author__ = 'anh.dv'
_logger = logging.getLogger(__name__)

ns = Namespace('containers', description='Container operations')

dm = DockerService.DockerManager()


@ns.route('')
class ContainerController(_fr.Resource):

    def get(self):
        return dm.get_containers()


@ns.route("/<container_id>")
class ContainerDetailController(_fr.Resource):

    def get(self, container_id: str):
        return dm.get_containers(container_id)


@ns.route("/<container_id>/restart")
class ContainerRestart(_fr.Resource):
    def post(self, container_id: str):
        return dm.container_restart(container_id)


@ns.route("/<container_id>/stop")
class ContainerStop(_fr.Resource):
    def post(self, container_id: str):
        return dm.container_stop(container_id)


@ns.route("/<container_id>/kill")
class ContainerKill(_fr.Resource):
    def post(self, container_id: str):
        return dm.container_kill(container_id)
