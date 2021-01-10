from resources.user import (
    UserList,
    UserDetail
)


def initialize_routes(api):
    api.add_resource(UserList, '/api/users', endpoint='user_list_view')
    api.add_resource(UserDetail, '/api/users/<id>', endpoint='user_detail_view')
