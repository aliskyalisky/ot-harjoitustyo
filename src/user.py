class User:
    """Luokka yksittäiselle käyttäjälle
    """
    def __init__(self, username:str, password:str):
        """Käyttäjän luonti

        Args:
            username (str): käyttäjänimi
            password (str): salasana
        """
        self.username = username
        self.password = password

    def edit_password(self, new_password):
        """Salasanan muokkaus

        Args:
            new_password (_type_): Uusi salasana
        """
        self.password = new_password
        