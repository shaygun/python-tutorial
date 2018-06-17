ldp_messages_table_items = [(('33.33.33.33',), [('ldp_instance_targeted_hello_interval', 15), ('ldp_instance_link_hello_hold_time', 15), ('ldp_instance_link_hello_interval', 5), ('ldp_i
nstance_targeted_hello_hold_time', 45), ('ldp_instance_keepalive_timeout', 30)])]

ldp_messages_table = {}
ldp_messages_table['mpls'] = {}
ldp_messages_table['mpls']['signaling-protocols'] = {}
ldp_messages_table['mpls']['signaling-protocols']['ldp'] = {}
ldp_messages_table['mpls']['signaling-protocols']['ldp']['global'] = {}
ldp_messages_table['mpls']['signaling-protocols']['ldp']['global']['hellos'] = []

for ldp_messages_table_entry in ldp_messages_table_items:
    ldp_messages_entry = {
        elem[0]: elem[1] for elem in ldp_messages_table_entry[1]
    }
    ldp_router_id = ldp_messages_entry['ldp_router_id']
    keepalive_interval = ldp_messages_entry['ldp_instance_keepalive_interval']
    keepalive_timeout = ldp_messages_entry['ldp_instance_keepalive_timeout']
    link_hello_interval = ldp_messages_entry['ldp_instance_link_hello_interval']
    link_hello_hold_time = ldp_messages_entry['ldp_instance_link_hello_hold_time']
    targeted_hello_interval = ldp_messages_entry['ldp_instance_targeted_hello_interval']
    targeted_hello_hold_time = ldp_messages_entry['ldp_instance_targeted_hello_hold_time']

    if ldp_router_id not in ldp_messages_table:
        ldp_messages_table['mpls']['signaling-protocols']['ldp']['global']['hellos'].append([
                        {state:
                                    {'keepalive_interval': keepalive_interval,
                                    'keepalive_timeout': keepalive_timeout,
                                    'link_hello_interval': link_hello_interval,
                                    'link_hello_hold_time': link_hello_hold_time,
                                    'targeted_hello_interval': targeted_hello_interval,
                                    'targeted_hello_hold_time': targeted_hello_hold_time
                                     }
                        }
                    ])

print (ldp_messages_table)
