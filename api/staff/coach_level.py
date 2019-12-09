from base.rest_client import RestClient
from public.get_token import get_token


class CoachLevel(RestClient):
    """教练等级所有API的封装"""

    def coach_level_list(self,data=None,**kwargs):
        """教练等级列表（分页）"""
        resp = self.get('/v1/setting/coach',data=data,**kwargs)
        return resp

    def coach_level_create(self,data=None, json=None, **kwargs):
        """新增教练等级"""
        resp = self.post('/v1/setting/coach', data=data, json=None, **kwargs)
        return resp
    
    def coach_level_delete(self, coach_id,**kwargs):
        resp = self.delete('/v1/setting/coach/{}'.format(coach_id), **kwargs)
        return resp
    
    def coach_level_edit(self,coach_id,data=None,**kwargs):
        resp = self.put('/v1/setting/coach/{}'.format(coach_id), data=data,**kwargs)
        return resp
        

if __name__ == "__main__":
    from public.get_token import get_token
    token = get_token("st6527031128", "CUEw6057")
    print(token)
    c = CoachLevel(token)
    r = c.coach_level_list()
    print(r)