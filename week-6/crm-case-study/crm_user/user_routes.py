from pymysql.connections import Connection
from crm_user.user_manipulation_resource import UserManipulationResource
from crm_user.user_service import UserService


def load_user_routes(api, connection: Connection):

    service = UserService(connection)

    api.add_resource(
        UserManipulationResource,
        '/user/login',
        resource_class_kwargs={'service': service}
    )
