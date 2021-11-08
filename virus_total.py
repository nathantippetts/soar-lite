from vault import Vault
import json
import hashlib
# Run pip install virustotal-api
from virus_total_apis import PublicApi as VirusTotalPublicApi
# Not sure if necessary with the PyPi VT API package, but their normal API requires URLs to be base64 encoded
import base64

API_KEY = Vault.get_key_from_db()

# For testing purposes
EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*".encode('utf-8')
EICAR_MD5 = hashlib.md5(EICAR).hexdigest()

vt = VirusTotalPublicApi(API_KEY)
response = vt.get_file_report(EICAR_MD5)
print(json.dumps(response, sort_keys=False, indent=4))



# Unrelated to testing above
# VirusTotal's recommendation for the URL identifier
url_id = base64.urlsafe_b64encode("http://www.reddit.com/r/learnpython".encode()).decode().strip("=")
print(url_id)
