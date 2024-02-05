from flask import Flask, jsonify, request

app = Flask(__name__)

airport_data = {
    'UAE': {'Dubai International Airport': 'DXB', 'Abu Dhabi International Airport': 'AUH' ,'Al Maktoum International Airport':'DWC'},
    'Turkey': {'Istanbul Airport': 'IST', 'Trabzon Airport': 'TZX', 'Sabiha Gökçen International Airport': 'SAW'},
    'Oman': {'Muscat International Airport': 'MCT', 'Salalah Airport': 'SLL'},
    'Qatar': {'Hamad International Airport': 'DOH'},
    'Syria': {'Damascus International Airport': 'DAM', 'Aleppo International Airport': 'ALP'},
    'Lebanon': {'Beirut-Rafic Hariri International Airport': 'BEY'},
    'Saudi Arabia': {'King Abdulaziz International Airport': 'JED', 'King Khalid International Airport': 'RUH'},
}

@app.route('/airport', methods=['GET'])
def autocomplete():
    query = request.args.get('query')
    results = []

    for country, airports in airport_data.items():
        for airport_name, airport_code in airports.items():
            if query.lower() in airport_name.lower():
                results.append({'country': country, 'airport_name': airport_name, 'airport_code': airport_code})

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
