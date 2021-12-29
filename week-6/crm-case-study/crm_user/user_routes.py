from pymysql.connections import Connection
from crm_user.user_manipulation_resource import UserManipulationResource
from crm_user.user_activation_resource import UserActivationResource
from crm_user.user_service import UserService
from crm_user.user_activation_service import UserActivationService


def load_user_routes(api, connection: Connection):

    service = UserService(connection)
    activation_service = UserActivationService(connection)

    api.add_resource(
        UserManipulationResource,
        '/user/login',
        resource_class_kwargs={'service': service}
    )

    api.add_resource(
        UserActivationResource,
        '/admin/activation',
        resource_class_kwargs={'activation_service': activation_service}
    )
