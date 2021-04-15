import asyncio
import logging
import time

cdef object CLIENT_IDS = set()


cdef class IB:
    cdef object _logger
    cdef int _clientId

    def __init__(self):
        self._logger = logging.getLogger('ib_sim.ib')

    def connect(
        self,
        str host = '127.0.0.1',
        int port = 7497,
        int clientId = 1,
        float timeout = 4,
        bint readonly = False,
        str account = '',
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
