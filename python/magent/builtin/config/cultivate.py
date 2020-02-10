"""
A resource management game.
"""

import magent


def get_config(map_size):
    gw = magent.gridworld
    cfg = gw.Config()

    cfg.set({"map_width": map_size, "map_height": map_size})
    cfg.set({"embedding_size": 10})

    deer = cfg.register_agent_type(
        "deer",
        {'width': 1, 'length': 1, 'hp': 5, 'speed': 0,
         'view_range': gw.CircleRange(0), 'attack_range': gw.CircleRange(0),
         'step_recover': 0.2,
         'kill_supply': 8,
         })

    tiger = cfg.register_agent_type(
        "tiger",
        {'width': 1, 'length': 1, 'hp': 10, 'speed': 1,
         'view_range': gw.CircleRange(4), 'attack_range': gw.CircleRange(1),
         'cultivate_range': gw.CircleRange(1),
         'damage': 1, 'cultivate': -2, 'step_recover': -0.2,
         })

    deer_group  = cfg.add_group(deer)
    tiger_group = cfg.add_group(tiger)

    a = gw.AgentSymbol(tiger_group, index='any')
    b = gw.AgentSymbol(deer_group,  index='any')

    # tigers get reward when they attack a deer
    e = gw.Event(a, 'attack', b)
    cfg.add_reward_rule(e, receiver=[a], value=[1])

    #cultivate reward
    f = gw.Event(a, 'cultivate', b)
    cfg.add_reward_rule(f, receiver=[a], value=[1])

    return cfg
