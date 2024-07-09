import requests
import sqlite3
from test import SwapiDataTest

class SwapiDataIngestor:
    SWAPI_BASE_URL = "https://swapi.dev/api"

    def __init__(self):
        self.conn = sqlite3.connect('swapi_data.db')
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS planets (
                name TEXT,
                rotation_period INTEGER,
                orbital_period INTEGER,
                diameter INTEGER,
                climate TEXT,
                gravity TEXT,
                terrain TEXT,
                surface_water INTEGER,
                population INTEGER,
                residents TEXT,
                films TEXT,
                created TIMESTAMP,
                edited TIMESTAMP,
                url TEXT
            )
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS people (
                name TEXT,
                height INTEGER,
                mass INTEGER,
                hair_color TEXT,
                skin_color TEXT,
                eye_color TEXT,
                birth_year TEXT,
                gender TEXT,
                homeworld TEXT,
                films TEXT,
                species text,
                vehicles text,
                starships text,
                created TIMESTAMP,
                edited TIMESTAMP,
                url TEXT
            )
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS starships (
                name TEXT,
                model TEXT,
                manufacturer TEXT,
                cost_in_credits text,
                length TEXT,
                max_atmosphering_speed text,
                crew TEXT,
                passengers TEXT,
                cargo_capacity TEXT,
                consumables TEXT,
                hyperdrive_rating TEXT,
                MGLT text,
                starship_class TEXT,
                pilots text,
                films text,
                created TIMESTAMP,
                edited TIMESTAMP,
                url TEXT
            )
        ''')

        self.conn.commit()

    def fetch_data(self, endpoint):
        url = f"{self.SWAPI_BASE_URL}/{endpoint}/"
        list=[]
        while url:
            response = requests.get(url)
            data = response.json()
            list.append(data)
            yield from data['results']
            url = data['next']
        return list

    def insert_data(self):
            self.insert_planets()
            self.insert_people()
            self.insert_starships()
            self.conn.commit()

    def insert_planets(self):
        for planet in self.fetch_data('planets'):
            planet['films'] = ', '.join(planet['films'])
            planet['residents'] = ', '.join(planet['residents'])
            self.cur.execute(
                '''
                INSERT INTO planets (
                    name, rotation_period, orbital_period, diameter, climate, gravity,
                    terrain, surface_water, population, residents,films,created, edited, url
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?)
                ''',
                (
                    planet['name'], 
                    planet['rotation_period'], 
                    planet['orbital_period'], 
                    planet['diameter'],
                    planet['climate'], 
                    planet['gravity'], 
                    planet['terrain'], 
                    planet['surface_water'],
                    planet['population'], 
                    planet['residents'],
                    planet['films'],
                    planet['created'], 
                    planet['edited'], 
                    planet['url']
                )
            )

            

    def insert_people(self):
        for person in self.fetch_data('people'):
            person['films'] = ', '.join(person['films'])
            person['species'] = ', '.join(person['species'])
            person['vehicles'] = ', '.join(person['vehicles'])
            person['starships'] = ', '.join(person['starships'])
            self.cur.execute(
                '''
                INSERT INTO people (
                    name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, 
                    homeworld,films,species,
                    vehicles,starships,
                    created, edited, url
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    person['name'], 
                    person['height'], 
                    person['mass'], 
                    person['hair_color'], 
                    person['skin_color'],
                    person['eye_color'], 
                    person['birth_year'], 
                    person['gender'], 
                    person['homeworld'],
                    person['films'],
                    person['species'],
                    person['vehicles'],
                    person['starships'],
                    person['created'], 
                    person['edited'],
                    person['url']
                )
            )

    def insert_starships(self):
        for starship in self.fetch_data('starships'):

            starship['films'] = ', '.join(starship['films'])
            starship['pilots'] = ', '.join(starship['pilots'])
            
            self.cur.execute(
                '''
                INSERT INTO starships (
                    name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers,
                    cargo_capacity, consumables, hyperdrive_rating, MGLT, starship_class,
                    pilots,films,created, edited, url
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?)
                ''',
                (
                    starship['name'], 
                    starship['model'], 
                    starship['manufacturer'], 
                    starship['cost_in_credits'],
                    starship['length'], 
                    starship['max_atmosphering_speed'], 
                    starship['crew'], 
                    starship['passengers'],
                    starship['cargo_capacity'], 
                    starship['consumables'], 
                    starship['hyperdrive_rating'],
                    starship['MGLT'], 
                    starship['starship_class'], 
                    starship['pilots'],
                    starship['films'],
                    starship['created'], 
                    starship['edited'],
                    starship['url']
                )
            )

    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    ingestor = SwapiDataIngestor()
    ingestor.insert_data()
    ingestor.close()
    print("Successful insert data")
