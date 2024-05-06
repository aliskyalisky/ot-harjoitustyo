class UserService:
    """Luokka joka huolehtii kaikista käyttäjistä
    """
    def __init__(self):
        """Alustus tyhjällä listalla
        """
        self.users = []

    def add_user(self, user):
        """Uuden käyttäjän lisäys
        Args:
            user: Käyttäjäolio
        """
        self.users.append(user)

    def list_users(self):
        """Käyttäjien nimimerkkien listaaminen

        Returns:
            list: Lista käyttäjien nimimerkeistä
        """
        list = [] # pylint: disable=redefined-builtin
        for user in self.users:
            list.append(user.username)
        return list

    def check_login(self, username:str, password:str):
        """Tarkistaa käyttäjän nimen ja salasanan

        Args:
            username (str): käyttäjänimi
            password (str): salasana

        Returns:
            Boolean: True jos check onnistunut, muuten False
        """
        for user in self.users:
            return bool(user.username == username and user.password == password)
            