import asyncio
import logging
import time

from ib_sim.wrapper cimport Wrapper

cdef object CLIENT_IDS = set()

cdef int DISCONNECTED = 0
cdef int CONNECTING = 1
cdef int CONNECTED = 2

cdef class Client:
    def __init__(self, wrapper: Wrapper):
        self.wrapper = wrapper
        self._logger = logging.getLogger('ib_sim.client')

        self.host = ''
        self.port = -1
        self.clientId = -1

        self.reset()

    cpdef void reset(self):
        print(f'{DISCONNECTED}, {CONNECTING}, {CONNECTED}')
        self.conState = DISCONNECTED

    cpdef void connect(
        self,
        char *host = '127.0.0.1',
        int port = 7497,
        int clientId = 1,
        float timeout = 4,
        bint readonly = False,
        char *account = '',
    ):
        self._logger.info(
            f'Connecting to {host}:{port} with clientId {clientId}...'
        )
        if clientId in CLIENT_IDS:
            self._logger.warning(
                f'Peer closed connection. clientId {clientId} already in use?'
            )
            time.sleep(timeout)
            raise asyncio.TimeoutError()
        CLIENT_IDS.add(clientId)
        self.host = host
        self.port = port
        self.clientId = clientId
        self.conState = CONNECTED
        self._logger.info('Connected')

    cpdef void disconnect(self):
        self._logger.info('Disconnecting')
        CLIENT_IDS.remove(self.clientId)
        self.reset()

    cpdef bint isConnected(self):
        return self.conState == CONNECTED