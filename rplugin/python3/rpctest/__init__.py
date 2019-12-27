import pynvim as Nvim


@Nvim.plugin
class RpcTestHandlers(object):
    def __init__(self, nvim: Nvim) -> None:
        self.nvim = nvim

    @Nvim.function("_rpctest_init", sync=True)
    def init(self, args) -> None:
        self.nvim.current.line = ('Command with args: {}, range: {}'
                                  .format(args, range))
        self.nvim.command('vsplit')
        return "unti"

    # @neovim.function("TestFunction", sync=True)
    # def testfunction(self, args):
    #     return 3

    # @Nvim.rpc_export()
