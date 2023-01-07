import pyang
import pyangbind.lib.pybindJSON as pybindJSON
import netconf
import pyangbind.lib.pybindJSON as pybindJSON

model = pyang.util.yangmodel.YangModel("path/to/yang/model.yang")

bindings = pybindJSON.loads(model.get_schema(), generate_binding=True)

device = netconf.NetconfServiceProvider(
    address="device_ip_address",
    port=830,
    username="username",
    password="password",
)

config = device.get_config(source="running")
config_obj = bindings.parse(config.xml, "config")

for element in config_obj:
    if element not in model:
        print("Element '{}' not found in YANG model".format(element))