

from api.staff.coach_level import CoachLevel
from public.get_token import get_token

# coach_level = CoachLevel(get_token("st65271088319", "m562e7Qh"))
def get_coach_name_id(coach_level, setting_name):
    resp = coach_level.coach_level_list()
#     resp = {
#     "code": 0,
#     "msg": "success",
#     "data": {
#         "total": 2,
#         "max": 10,
#         "price_setting": 2,
#         "list": [
#             {
#                 "class_ss_price": 3,
#                 "salary_template": 0,
#                 "used_number": 2,
#                 "id": 273579502010420,
#                 "updated_time": "2019-11-05 17:36:49",
#                 "setting_name": "明星教练",
#                 "operator_name": "汤汤 部俱乐部测试专用",
#                 "auth": {
#                     "brand:setting:coach_level|edit": 1
#                 }
#             },
#             {
#                 "class_price": 0,
#                 "salary_template": 0,
#                 "used_number": 0,
#                 "id": 275094920822807,
#                 "updated_time": "2016 19-11-06 18: 42: 15",
#                 "setting_name": "金牌教练",
#                 "operator_name": "汤汤俱乐部测试专用",
#                 "auth": {
#                     "brand:setting:coach_level|edit": 1,
#                     "brand:setting:coach_level|del": 1
#                 }
#             }
#         ],
#         "page": {
#             "total_counts": 2,
#             "total_pages": 1,
#             "current_page": 0,
#             "size": 20
#         }
#     },
#     "checkAuth": [
#         "brand:setting:coach_level|list"
#     ]
# }
    d = {}
    for i in resp.json()["data"]["list"]:
        d.update({i["setting_name"]:i["id"]})
    try:
        return d[setting_name]
    except KeyError:
        return "Key '{}' 不存在.".format(setting_name)


if __name__ == "__main__":
    pass
    # v = get_coach_name_id("明星教练")
    # print(v)


