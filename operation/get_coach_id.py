

from api.staff.coach_level import CoachLevel

def get_coach_name_id(setting_name):
    resp = CoachLevel.coach_level_list()
    d = {}
    for i in resp["data"]["list"]:
        # for key,value in i.items():
        #     print(key,value)
        d.update({i["setting_name"]: i["id"]})

    try:
        return d[setting_name]
    except KeyError:
        return f"Key '{setting_name}' 不存在."


if __name__ == "__main__":
    print(get_coach_name_id("明星教练1"))