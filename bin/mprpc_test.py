from mprpc import RPCClient

c = RPCClient("localhost", 6666)
_, info = c.call("vim_get_api_info")
for f in info["functions"]:
    print(f["name"], f["parameters"], f["return_type"])
