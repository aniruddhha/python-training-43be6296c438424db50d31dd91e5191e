

class UserActivationService:

    def activate_user(self, admin_id: str, user_id: str) -> bool:
        '''
            1. check role of admin id
            2. role is not admin throw exception
            3. check given user is available in db, if not throw exception
            4. Check User is already activated, if true throw exception
            5. update the user with user_id and change the status to 1
        '''
        pass
