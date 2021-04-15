import asyncio

import pytest

from ib_sim import IB


def test_connect():
    ib = IB()
    ib.connect()


# def test_second_connect_fail():
#     ib = IB()
#     ib.connect()
#
#     with pytest.raises(asyncio.TimeoutError):
#         ib.connect()
