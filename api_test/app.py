from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # URL for the TryHackMe API
    url = 'https://tryhackme.com/api/hacktivities'
    params = {
        'page': 1,
        'order': 'most-popular',
        'difficulty': 'all',
        'type': 'all',
        'free': 'all',
        'limit': 100
    }
    
    # Fetching data from the API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        hacktivities = response.json()['rooms']
        
        # Categorize hacktivities by type
        categories = {}
        for hacktivity in hacktivities:
            category = hacktivity['type']
            if category not in categories:
                categories[category] = []
            categories[category].append(hacktivity)
        
        return render_template('index.html', categories=categories)
    else:
        return f"Error fetching hacktivities: {response.status_code}", 500

if __name__ == '__main__':
    app.run(debug=True)
