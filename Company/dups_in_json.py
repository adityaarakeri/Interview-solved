"""

Given a records
records = [
    {
     "metric": "count",
     "elephants": 8,
    },{
     "name": "Mr Jones",
     "combomeal": 4,
    },{
     "name": "Mr Jones",
     "combomeal": 4,
    },{
     "name": "Mr Smith",
     "combomeal": 54,
    }]

write a function to return the len of the records and no of duplicate objects => (4,1)

Use cmp function for dictonoaries 

"""


def find_duplicate(records):

    count = len(records)

    # duplicate = set([records.count(obj) for obj in records])  // old implementation
    duplicate = [cmp(vx, vy) for ix, vx in enumerate(records)
                 for iy, vy in enumerate(records) if ix != iy and ix < iy]
    # OLD implementation
    # print duplicate.count(0) // 0 if objects are equal

    # dup_count = 0
    # for val in duplicate:
    #     if val == 0:
    #         dup_count += 1

    # return count, dup_count
    return count, duplicate.count(0)


records = [
    {
        "metric": "count",
        "elephants": 8,
    }, {
        "name": "Mr Jones",
        "combomeal": 4,
    }, {
        "name": "Mr Jones",
        "combomeal": 4,
    }, {
        "name": "Mr Smith",
        "combomeal": 54,
    }]

print(find_duplicate(records))
