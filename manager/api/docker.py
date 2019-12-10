# coding=utf-8
import logging
import flask_restplus as _fr
from flask import Response, stream_with_context

from manager.utilities.namespace import Namespace
from manager.services import docker as DockerService

__author__ = 'anh.dv'
_logger = logging.getLogger(__name__)

ns = Namespace('dockers', description='Docker operations')

dm = DockerService.DockerManager()


@ns.route('/events')
class DockerEventController(_fr.Resource):

    def get(self):
        return Response(stream_with_context(dm.events()), mimetype="text/event-stream", headers={'Cache-Control': 'no-cache'})
