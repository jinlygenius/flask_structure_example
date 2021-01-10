from marshmallow import fields, Schema, validates, validates_schema, ValidationError
from models.user import User
from . import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    email = fields.Email()
    class Meta:
        model = User
        fields = ("id", "username", "name", \
            "email", "phone", "gender",\
            "created_time", "updated_time")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserIDSchema(ma.Schema):
    '''
    Validate user id
    '''
    id = fields.Str(required=True)

    @validates("id")
    def validate_id(self, value):
        user = User.query.filter_by(id=value).first()
        if not user:
            raise ValidationError(f"User id {value} does not exist.")

user_id_schema = UserIDSchema()




# class UserSchema(ma.SQLAlchemySchema):
    # id = ma.auto_field()
    # username = ma.auto_field()
    # phone = ma.auto_field()
    # created_time = ma.auto_field()
    # updated_time = ma.auto_field()


# class UserSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ("id", "username", "phone", "created_time", "updated_time")

#     # # Smart hyperlinking
#     # _links = ma.Hyperlinks(
#     #     {"self": ma.URLFor("user_detail", id="<id>"), "collection": ma.URLFor("users")}
#     # )
