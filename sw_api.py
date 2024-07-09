from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('swapi_data.db')
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/hottest_planet', methods=['GET'])
def hottest_planet():
    query = "SELECT distinct name FROM planets where climate like '%arid%' ORDER BY length(climate) ASC LIMIT 3"
    planets = query_db(query)
    return jsonify([planet[0] for planet in planets])

@app.route('/appears_most', methods=['GET'])
def appears_most():
    query = "SELECT distinct name FROM people ORDER BY length(films) DESC LIMIT 5"
    people = query_db(query)
    return jsonify([person[0] for person in people])

@app.route('/fastest_ships', methods=['GET'])
def fastest_ships():
    query = "SELECT distinct name FROM starships ORDER BY cast(max_atmosphering_speed as int) DESC LIMIT 3"
    ships = query_db(query)
    return jsonify([ship[0] for ship in ships])

@app.route('/powerful_weapon', methods=['GET'])
def powerful_weapon():
    query = "SELECT distinct name FROM starships ORDER BY cast(cost_in_credits as int) DESC LIMIT 3"
    weapons = query_db(query)
    return jsonify([weapon[0] for weapon in weapons])

if __name__ == '__main__':
    app.run(debug=True)
