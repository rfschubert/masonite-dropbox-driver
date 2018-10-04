""" A Dropbox Service Provider """

from config import storage
from ..drivers import UploadDropboxDriver
# from .DropboxUploadManager import DropboxUploadManager
from masonite.provider import ServiceProvider

class DropboxProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UploadDropboxDriver', UploadDropboxDriver)

    def boot(self):
        pass
