import typing

import pynvim as Nvim
import logging

from rpctest.rplugin import Rplugin

Args = typing.List[typing.Any]

logger = logging.getLogger("rpctest")
logger.setLevel(logging.DEBUG)

handler1 = logging.FileHandler(filename="/tmp/rpctest.log")
handler1.setLevel(logging.DEBUG)
handler1.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

logger.addHandler(handler1)


@Nvim.plugin
class RpcTestHandler(object):

    def __init__(self, nvim: Nvim):
        self._rplugin = Rplugin(nvim)

    @Nvim.function('_rpctest_init', sync=True)
    def init_channel(self, args: Args) -> None:
        self._rplugin.init_channel()

    @Nvim.function('_rpctest_start', sync=True)
    def start(self, args: Args) -> None:
        logger.debug("rpctest debug messagge")
        self._rplugin.start()
