'''
containers = ["nginx", "redis"]
containers.append("postgres" )

print(containers)

containers = ["nginx", "redis"]
containers += ["postgres", "rabbitmq"]
containers += ["postgres", "rabbitmq"]


print(containers)

servers = ["web-1"]
servers.append(["web-2", "web-3"])

print(servers)


environments = [
    ["dev-web-1", "dev-db-1"],
    ["prod-web-1", "prod-db-1"],
    ["web", "web", "web"]
]

print(environments[0])      # Entire dev list
print(environments[0][1])   # dev-db-1
print(environments[1][0])   # prod-web-1
print(environments[1])
print(environments[2])

'''

servers = [['web-1', 'web-2'], ['db-1', 'db-2']]

flat_list = []

for group in servers:
    for server in group:
        flat_list.append(server)

print(flat_list)

flat_list = [server for group in servers for server in group]
print(flat_list)