import logging

from ib_sim.client cimport Client
from ib_sim.wrapper cimport Wrapper

cdef class IB:
    def __init__(self):
        self.wrapper = Wrapper(ib=self)
        self.client = Client(self.wrapper)
        self._logger = logging.getLogger('ib_sim.ib')

    cpdef void connect(
        self,
        char *host = '127.0.0.1',
        int port = 7497,
        int clientId = 1,
        float timeout = 4,
        bint readonly = False,
        char *account = '',
    ):
        self.client.connect(
            host, port, clientId, timeout, readonly, account
        )

    cpdef void disconnect(self):
        if not self.client.isConnected():
            return
        self._logger.info(
            f'Disconnecting from {self.client.host}:{self.client.port}'
        )
        self.client.disconnect()

    cpdef bint isConnected(self):
        return self.client.isConnected()
