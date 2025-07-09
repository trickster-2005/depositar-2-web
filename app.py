# API_URL = "https://demo.depositar.io/api/3/action/package_show?id=2994f" # birds

API_URL = "https://data.depositar.io/api/3/action/package_show?id=diagram"


from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = ""


@app.route('/')
def gallery():
    headers = {"Authorization": API_KEY}
    response = requests.get(API_URL, headers=headers)
    resources = []
    if response.status_code == 200:
        data = response.json()
        resources_data = data.get("result", {}).get("resources", [])
        for res in resources_data:
            url = res.get("url")
            name = res.get("name")
            description = res.get("description")
            if url and name:
                resources.append({"url": url, "name": name, "description":description})
    return render_template('gallery4.html', resources=resources)

if __name__ == '__main__':
    app.run(debug=True)


