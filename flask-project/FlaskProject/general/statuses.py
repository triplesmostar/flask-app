class Status:
    def __init__(self, error_code=None, description=None):
        self.errorCode = error_code
        self.description = description

    @classmethod
    def something_went_wrong(cls):
        """
        :return: cls(-1, 'Something went wrong')
        """
        return cls(-1, 'Something went wrong',)

    @classmethod
    def status_successfully_access_to_route(cls):
        """
        :return: cls(200, 'You have successfully accessed the route)
        """
        return cls(200, 'You have successfully accessed the route')

    @classmethod
    def status_successfully_processed(cls):
        """
        :return: cls(200, 'Successfully processed')
        """
        return cls(200, 'Successfully processed')

    @classmethod
    def status_connection_refuse(cls):
        """
        :return: cls(-1, 'Connection refuse')
        """
        return cls(-1, 'Connection refuse')

    @classmethod
    def status_token_required(cls):
        """
        :return: cls(-1, 'Token required')
        """
        return cls(-1, 'Token required')

    def repr_print(self):
        return {
            "errorCode": self.errorCode,
            "description": self.description,
        }
