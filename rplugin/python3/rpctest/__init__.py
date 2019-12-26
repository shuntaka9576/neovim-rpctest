import pynvim as Nvim
from rpctest.rplugin import Rplugin


@Nvim.plugin
class RpcTestHandlers(object):
    def __init__(self, nvim: Nvim) -> None:
        self._rplugin = Rplugin(nvim)

    @Nvim.function('_rpctest_init', sync=True)
    def init_channel(self) -> None:
        self._rplugin.init_channel()
