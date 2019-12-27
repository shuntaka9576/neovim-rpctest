import typing

import pynvim as Nvim
from rpctest.rplugin import Rplugin

Args = typing.List[typing.Any]


@Nvim.plugin
class RpcTestHandler(object):

    def __init__(self, nvim: Nvim):
        self._rplugin = Rplugin(nvim)

    @Nvim.function('_rpctest_init', sync=True)
    def init_channel(self, args: Args) -> None:
        self._rplugin.init_channel()

    @Nvim.function('_rpctest_start', sync=True)
    def start(self, args: Args) -> None:
        self._rplugin.start()
