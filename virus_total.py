from vault import Vault
import json
from virus_total_apis import PublicApi as VirusTotalPublicApi


class VirusTotal(Vault):
    """
    Allows a user to send IoCs for reputation checks against VirusTotal
    """
    def __init__(self):
        super().__init__()
        self.app = "virus_total"
        # Tries to fetch the API key, if it's not already there then ask the user to supply it
        try:
            self.API_KEY = super().get_apikey_from_db(self.app)
        except:
            self.API_KEY = super().get_apikey_from_user()
            encrypted = super().encrypt_key(self.API_KEY)
            super().store_key(encrypted, self.app)
        finally:
            self.vt = VirusTotalPublicApi(self.API_KEY)

    def vt_hash_reputation(self):
        # Takes a user entered hash (doesn't matter type) and sends it to virus total
        query = input("Enter a hash: ")
        response = self.vt.get_file_report(query)
        print(json.dumps(response, sort_keys=False, indent=4))

    def vt_url_reputation(self):
        # Takes a user entered URL and sends it to virus total
        query = input("Enter a URL: ")
        response = self.vt.get_url_report(query)
        print(json.dumps(response, sort_keys=False, indent=4))

    def vt_parse_info(self):
        # TODO: Parse important info from JSON output for easy viewing
        pass

