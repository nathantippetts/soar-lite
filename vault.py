from db_base import DBbase

class Vault(DBbase):
    '''
    Gets API keys, encrypts them, then writes them to a local SQLite file
    '''
    def __init__(self):
        super().__init__("vault.sqlite")

    def get_key_from_user(self):
        key = input("Enter your API key: ")
        return key

    def get_key_from_db(self):
        # TODO: SELECT api_key FROM Vault WHERE app = ?

    def encrypt_key(self, key):
        # TODO: Read in key from get_key(), encrypt it with secure 3rd party module, and return encrypted form

    def store_key(self, key):
        # TODO: Write encrypted key to SQLite DB

    def reset_database(self):
        # TODO: DROP then CREATE with necessary columns
