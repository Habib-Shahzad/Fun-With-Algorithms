
from dp import get_best_block as dp_get_best_block
from bf import get_best_block as bf_get_best_block
blocks = [
    {"hospital": False, "gym": False, "office": False, "lake": False},
    {"hospital": False, "gym": True, "office": True, "lake": True},
    {"hospital": False, "gym": False, "office": True, "lake": False},
    {"hospital": False, "gym": False, "office": True, "lake": True},
    {"hospital": False, "gym": False, "office": False, "lake": True},
    {"hospital": True, "gym": False, "office": True, "lake": False},
    {"hospital": True, "gym": True, "office": True, "lake": False},
    {"hospital": False, "gym": False, "office": False, "lake": True},
    {"hospital": False, "gym": False, "office": True, "lake": False},
    {"hospital": False, "gym": False, "office": False, "lake": True},
]

reqs = ['hospital', 'gym', 'office', 'lake']


blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

reqs = ["gym", "school", "store"]


print(bf_get_best_block(blocks, reqs, True))
print(dp_get_best_block(blocks, reqs, True))
