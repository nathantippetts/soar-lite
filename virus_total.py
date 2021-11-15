from vault import Vault
from virus_total_apis import PublicApi as VirusTotalPublicApi


class VirusTotal:
    """
    Allows a user to send IoCs for reputation checks against VirusTotal
    """
    def __init__(self):
        vault = Vault()
        self.query = ""
        self.app = "virus_total"
        # Tries to fetch the API key, if it's not already there then ask the user to supply it
        try:
            self.API_KEY = vault.get_apikey_from_db(self.app)
        except:
            self.API_KEY = vault.get_apikey_from_user()
            encrypted = vault.encrypt_key(self.API_KEY)
            vault.store_key(encrypted, self.app)
        finally:
            self.vt = VirusTotalPublicApi(self.API_KEY)

    def vt_hash_reputation(self):
        # Takes a user entered hash (doesn't matter type) and sends it to virus total
        # TODO: Figure out how to read in from the web interface
        self.query = input("Enter a hash: ")
        response = self.vt.get_file_report(self.query)
        return response

    def vt_url_reputation(self):
        # Takes a user entered URL and sends it to virus total
        # TODO: Figure out how to read in from the web interface
        self.query = input("Enter a URL: ")
        response = self.vt.get_url_report(self.query)
        return response

    def vt_parse_info(self, response):
        # Parses out the scan results into a dictionary
        hashes = []
        engines = []
        for v in response.values():
            if type(v) is dict:
                for j,x in list(v["scans"].items()):
                    engines.append(j)
                    hashes.append(x)
        results = zip(engines, hashes)
        return results
