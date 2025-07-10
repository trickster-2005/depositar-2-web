DATASET_IDS = ['diagram', 'ceramic-artifacts','jade-artifacts','stone-artifacts','field']
API_URL = "https://data.depositar.io/api/3/action/package_show?id={}"
API_KEY = ""


from flask import Flask, render_template
import requests



app = Flask(__name__)
@app.route('/')
def gallery():
    headers = {"Authorization": API_KEY}
    resources = []
    dataset_titles = {}  # for select menu

    for dataset_id in DATASET_IDS:
        url = API_URL.format(dataset_id)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            dataset_title = data["result"].get("title", dataset_id)
            dataset_titles[dataset_id] = dataset_title
            resources_data = data.get("result", {}).get("resources", [])
            for res in resources_data:
                resource_url = res.get("url")
                name = res.get("name")
                description = res.get("description")
                if resource_url and name:
                    resources.append({
                        "url": resource_url,
                        "name": name,
                        "description": description,
                        "dataset_id": dataset_id,
                        "dataset_title": dataset_title
                    })
    return render_template('gallery.html', resources=resources, dataset_titles=dataset_titles)

if __name__ == '__main__':
    app.run(debug=True)


