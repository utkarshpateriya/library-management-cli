class CLI:
    """
    For better readability, separated CLI methods from core.
    """
    @staticmethod
    def get_user_input(message):
        return input(message)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def wait_to_continue():
        input("Press Enter to continue...")