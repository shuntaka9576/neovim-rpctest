import pynvim as Nvim


@Nvim.plugin
class RpcTestHandlers(object):
    def __init__(self, nvim: Nvim) -> None:
        self.nvim = nvim

    @Nvim.function("_rpctest_init", sync=True)
    def init() -> None:
        print("hello")

    # @Nvim.rpc_export()
