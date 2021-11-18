from flask import Flask, render_template
from virus_total import VirusTotal
app = Flask(__name__)

# Placeholder content. Will be more dynamic in the future
posts = [
    {
        "author": "KrebsOnSecurity",
        "title": "Hoax Email Blast Abused Poor Coding in FBI Website",
        "content": "The Federal Bureau of Investigation (FBI) confirmed today that its fbi.gov domain name and Internet"
                   " address were used to blast out thousands of fake emails about a cybercrime investigation. "
                   "According to an interview with the person who claimed responsibility for the hoax, the spam messages"
                   " were sent by abusing insecure code in an FBI online portal designed to share information with state"
                   " and local law enforcement authorities.",
        "date_posted": "November 13, 2021"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "November 13, 2021"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home")


@app.route("/integrations")
def integrations():
    return render_template("integrations.html", title="Integrations")


@app.route("/reputations")
def reputations():
    return render_template("reputation.html", title="Reputation Lookup")


@app.route("/reputations/hash")
def hash_reputation():
    vt = VirusTotal()
    vt_hash_dict = vt.vt_hash_reputation()
    vt_results = vt.vt_parse_scan_results(vt_hash_dict)
    vt_totals = vt.vt_parse_scan_totals(vt_hash_dict)
    vt_query = vt.query
    return render_template("reputation_results.html", title="Reputation Results", vt_totals=vt_totals, vt_hashes=vt_results, vt_query=vt_query)


if __name__ == "__main__":
    app.run(debug=True)
