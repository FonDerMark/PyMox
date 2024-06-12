from pymox import PyMox

pm = PyMox(host='192.168.0.205', username='xm0rph@pam', password='7755685Aa!!!', verify=False)
# print(pm)
# print(pm.nodes.get_nodes(status="online"))
print(pm.nodes.get_node(node='pve'))
# print(pm.nodes.lxc.get_lxc(node='pve'))
# print(pm.nodes.storage.get_storage_status(node='pve'))