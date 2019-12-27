import pynvim as Nvim


class Rplugin:
    def __init__(self, nvim: Nvim) -> None:
        self._nvim = nvim

    def init_channel(self) -> None:
        self._nvim.vars['rpctest#_channel_id'] = self._nvim.channel_id

    def start(self) -> None:
        self._nvim.command('vsplit')
