import vantage6.client as vtgclient
from config import DEFAULT_IMAGE, DEFAULT_TASK


class TSEClient():

    def __init__(self, host, port, username, password, image=DEFAULT_IMAGE, task=DEFAULT_TASK):
        self.image = image
        self.task = task

        self.client = vtgclient.Client(host, port)
        self.client.authenticate(username, password)

        # TODO: Actually set up encryption
        self.client.setup_encryption(None)
    