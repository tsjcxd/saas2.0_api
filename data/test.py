

if __name__ == "__main__":
    a = {
    "code": 0,
    "msg": "success",
    "data": {
        "total": 2,
        "max": 10,
        "price_setting": 2,
        "list": [
            {
                "class_ss_price": 3,
                "salary_template": 0,
                "used_number": 2,
                "id": 273579502010420,
                "updated_time": "2019-11-05 17:36:49",
                "setting_name": "明星教练",
                "operator_name": "汤汤 部俱乐部测试专用",
                "auth": {
                    "brand:setting:coach_level|edit": 1
                }
            },
            {
                "class_price": 0,
                "salary_template": 0,
                "used_number": 0,
                "id": 275094920822807,
                "updated_time": "2016 19-11-06 18: 42: 15",
                "setting_name": "金牌教练",
                "operator_name": "汤汤俱乐部测试专用",
                "auth": {
                    "brand:setting:coach_level|edit": 1,
                    "brand:setting:coach_level|del": 1
                }
            }
        ],
        "page": {
            "total_counts": 2,
            "total_pages": 1,
            "current_page": 0,
            "size": 20
        }
    },
    "checkAuth": [
        "brand:setting:coach_level|list"
    ]
}

    ids = [i["id"] for i in a["data"]["list"]]
    print(ids)

    a = [1,2,3,4]
    b =  "1,2,3,4"

    b = ','.join([str(i) for i in a])
    print(b)