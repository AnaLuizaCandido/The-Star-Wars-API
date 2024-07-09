import requests
import sqlite3

class SwapiDataTest:
    SWAPI_BASE_URL = "https://swapi.dev/api"

    def __init__(self):
        self.conn = sqlite3.connect('swapi_data.db')
        self.cur = self.conn.cursor()

    def query_db(self, query, args=(), one=False):
        conn = self.conn
        cur = conn.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        
        return (rv[0] if rv else None) if one else rv

    def fetch_data(self, endpoint):
        url = f"{self.SWAPI_BASE_URL}/{endpoint}/"
        
        response = requests.get(url)
        data = response.json()
        count = int(data["count"])
        return count
    
    def test_data(self):
        if self.test_planets():
            if self.test_people():
                if self.test_starships():
                    return True
                else: return False
            else: return False
        else:
            print("error")
            return False
        
        self.conn.close()
        

    def test_planets(self):
        planet_count= self.fetch_data('planets')
        query = "SELECT count(name) FROM planets"
        planets = self.query_db(query)
        if planet_count == int(planets[0][0]):
            print("Successful ingestion")
            return True
        else:
            print("Failed ingestion")
            return False

    def test_people(self):
        people_count= self.fetch_data('people')
        query = "SELECT count(name) FROM people"
        people = self.query_db(query)
        if people_count == int(people[0][0]):
            print("Successful ingestion")
            return True
        else:
            print("Failed ingestion")
            return False

    def test_starships(self):
        starships_count= self.fetch_data('starships')
        query = "SELECT count(name) FROM starships"
        starships = self.query_db(query)
        if starships_count == int(starships[0][0]):
            print("Successful ingestion")
            return True
        else:
            print("Failed ingestion")
            return False
        


if __name__ == "__main__":
    test = SwapiDataTest()
    test.test_data()
    
               