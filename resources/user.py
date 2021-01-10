from databases import mysqldb as db
from serializers.user import (
    users_schema,
    user_schema,
    user_id_schema
)
from flask import request, jsonify
from flask_restful import (
    reqparse,
    abort,
    Api,
    Resource,
    fields,
    marshal_with,
    marshal
)
from models.user import User
from .utils import (
    parse_request_args_keys,
    parse_request_json_keys,
    generate_user_id
)
import logging


logger = logging.getLogger('user')


class UserList(Resource):

    def get(self):
        '''
        Get users

        Filter fields:
            id
            username
            name
            email
            phone
            gender


        GET

            /api/users

        Response 200

            [
                {
                    "updated_time": "2020-06-18T22:35:12",
                    "name": null,
                    "id": "0ede8bb172ac4c56beed11c978a53fb3",
                    "created_time": "2020-06-18T22:35:12",
                    "email": null,
                    "phone": null,
                    "gender": null,
                    "username": "ella"
                }
            ]
                    
        '''
        parser = reqparse.RequestParser()
        queries = parse_request_args_keys(request)
        for _ in queries:
            parser.add_argument(_)
        iargs = parser.parse_args()
        # users = User.query.filter_by(**iargs).order_by(-User.created_time).all()
        users = User.query.filter_by(**iargs).all()
        return users_schema.dump(users)

    def post(self):
        '''
        Create a user

        POST

            {
                "username": "test10", # required
                "phone": "xxx",
                "name": "xxx",
                "gender": "F",
                "email": "xxx@xxx.com"
            }

        Response 201

            {
                "created_time": "2020-06-20T10:14:33",
                "phone": "xxx",
                "updated_time": "2020-06-20T10:14:33",
                "name": "xxx",
                "id": "a1c27d194ce44c1f9655cb0036edb101",
                "gender": "F",
                "username": "test10",
                "email": "xxx@xxx.com"
            }

        '''
        # import pdb; pdb.set_trace()
        parser = reqparse.RequestParser()
        post_keys = parse_request_json_keys(request)
        for _ in post_keys:
            parser.add_argument(_)
        iargs = parser.parse_args()
        # generate user_id
        iargs.pop('id', None)
        iargs['id'] = generate_user_id()
        errors = user_schema.validate(iargs)
        if errors:
            abort(400, message=str(errors))
        user = User(**iargs)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            abort(400, message=str(e))
        return user_schema.dump(user), 201


class UserDetail(Resource):

    def get(self, id):
        '''
        Get a user

        GET

            /api/users/0ede8bb172ac4c56beed11c978a53fb3

        Response 200

            {
                "updated_time": "2020-06-18T22:35:12",
                "name": null,
                "id": "0ede8bb172ac4c56beed11c978a53fb3",
                "created_time": "2020-06-18T22:35:12",
                "email": null,
                "phone": null,
                "gender": null,
                "username": "ella"
            }
                    
        '''
        errors = user_id_schema.validate({"id": id})
        if errors:
            abort(400, message=str(errors))

        # users = User.query.filter_by(**iargs).order_by(-User.created_time).all()
        user = User.query.filter_by(id=id).first()
        return user_schema.dump(user)
