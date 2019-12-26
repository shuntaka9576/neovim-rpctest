import pynvim as Nvim
from rpctest.rplugin import Rplugin


@Nvim.plugin
class RpcTestHandlers(object):
    def __init__(self, nvim: Nvim) -> None:
        self._rplugin = Rplugin(nvim)

    @Nvim.function('_rpctest_init', sync=True)
    def init_channel(self) -> None:
        self._rplugin.init_channel()

    # @Nvim.autocmd("VimEnter")
    # def update(self):
    #     try:
    #         self.wid = self.api.workspaces()[0]["id"]
    #         self.projects = self.get_projects([])
    #     except ConnectionError:
    #         self.echo("No network, toggl.nvim is disabled.")

    # def echo(self, msg):
    #     self.nvim.command("echo '{}'".format(msg))
