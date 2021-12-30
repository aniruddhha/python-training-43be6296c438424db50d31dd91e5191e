from pymysql.connections import Connection
from crm_user.user_manipulation_resource import UserManipulationResource
from crm_user.user_activation_resource import UserActivationResource
from crm_user.user_service import UserService
from crm_user.user_activation_service import UserActivationService
from crm_user.user_list_resource import UserListResource
from crm_user.user_list_service import UserListService


def load_user_routes(api, connection: Connection):

    service = UserService(connection)
    activation_service = UserActivationService(connection)
    user_list_service = UserListService(connection)

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

    api.add_resource(
        UserListResource,
        '/admin/users',
        resource_class_kwargs={'service': user_list_service}
    )
