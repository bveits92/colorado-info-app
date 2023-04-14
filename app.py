import sqlite3
import wikipedia as wiki
from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
import requests
import zipcodes


# Configure application
app = Flask(__name__)

@app.route('/')
def index():
    # Gathering the summary about the state of Colorado
    title = "State of Colorado"
    summary = wiki.summary(title)
    
    
    return render_template('index.html', summary=summary, title=title)

# Web page that does query to get info about population in specific county
@app.route('/query', methods=["GET", "POST"])
def query():

    # create a connection object
    conn = sqlite3.connect('population.db')

    # create a cursor object to interact with the database
    cursor = conn.cursor()


    if request.method == 'POST':
            
        # Prompts the user for a gender
        gender = request.form.get('gender')

        # Prompts the user for the a year
        year = request.form.get('year')

        # Prompts the user for county
        county = request.form.get('county')

        if gender == 'total':
            # Getting the total population for the selected county and year
            cursor.execute("SELECT total FROM population WHERE county = ? AND year = ? ORDER BY year DESC LIMIT 1", (county, year))
            result = cursor.fetchone()[0]  # extract the first column of the first row
        else:
            # Getting the result for the selected gender, county, and year
            cursor.execute("SELECT {} FROM population WHERE county = ? AND year = ? ORDER BY year DESC LIMIT 1".format(gender), (county, year))
            result = cursor.fetchone()[0]  # extract the first column of the first row


        return render_template('query_result.html', result=result, year=year, gender=gender, county=county)

    
    else:
        counties = cursor.execute("SELECT county FROM population GROUP BY county")

        return render_template('query.html', counties=counties)
    


# Web page that visualize the data from csv population projections by county that the user chose
@app.route('/graphs', methods=["GET", "POST"])
def graphs():
    # create a connection object
    conn = sqlite3.connect('population.db')

    # create a cursor object to interact with the database
    cursor = conn.cursor()

    if request.method == 'POST':
        county = request.form['county']
        gender = request.form['gender']
        if county == 'all':
            df = pd.read_csv('Colorado_population.csv')
        else:
            df = pd.read_csv('Colorado_population.csv').loc[pd.read_csv('Colorado_population.csv')['county'] == county]
        if gender == 'male':
            y = df['malePopulation']
        elif gender == 'female':
            y = df['femalePopulation']
        else:
            y = df['totalPopulation']
        fig = go.Figure(data=[go.Bar(x=df['year'], y=y)])
        plot_div = plot(fig, output_type='div')
        return render_template('graph_result.html', plot_div=plot_div, gender=gender, county=county)

    else:
        counties = cursor.execute("SELECT county FROM population GROUP BY county")
        return render_template('graphs.html', counties=counties)


# Web page which takes a county as an argument and displays a county summary from wikipedia
@app.route('/info', methods=["GET", "POST"])
def info():
    # create a connection object
    conn = sqlite3.connect('population.db')

    # create a cursor object to interact with the database
    cursor = conn.cursor()

    # Getting the counties list from the database
    counties = cursor.execute("SELECT county FROM population GROUP BY county")

    if request.method == 'POST':
        # Prompts the user to pick a county in Colorado
        county = request.form['county']
        title = county + " Colorado county"
        summary = wiki.summary(title)
    
        return render_template('info.html', summary=summary, title=title, counties=counties)
      
    else:
        
        return render_template('info.html', counties=counties)



# Web page that ask from user to pick a Colorado city and type of itinerary that he looking for
@app.route('/itinerary', methods=["GET", "POST"])
def itinerary():
    # Get a list of all zip codes in Colorado
    co_zipcodes = zipcodes.filter_by(state='CO')

    # Extract the list of city names from the zip codes
    cities = [zipcode['city'] for zipcode in co_zipcodes]

    # Remove duplicates and sort the list
    cities = sorted(set(cities))

    # Creating a list of all itinerary types
    itinerary_aliases = {
        "Accommodations": "hotels",
        "Adult": "adult",
        "Amusements": "amusementparks, aquariums, arcades",
        "Architecture": "landmarks, monuments",
        "Cultural": "culturalcenter",
        "Historic": "museums",
        "Industrial facilities": "factories",
        "Natural": "parks",
        "Religion": "religiousorgs",
        "Sport": "active",
        "Banks": "banks",
        "Food": "food",
        "Shops": "shopping",
        "Transport": "transport"
    }
    
    if request.method == 'POST':
        # Get the name of the city from the user input
        city = request.form.get('city')
        city = city + " Colorado"

        # Get the type of itinerary
        category_alias = request.form.get('itinerary_type')


        url = f"https://api.yelp.com/v3/businesses/search?location={city}&term={category_alias}&sort_by=best_match&limit=30"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer pUf2JzXR1iDFAvIGBsmPvQAyVdXBQCodSnID9Z5sT59BcRYkkWvg_VoXZsfeo0Nj8odHJ1lJYcr6h0AwURBOVqRI-SDMTY5iks0_CRpHznpFz-MXz_Xg3PmHpOQ2ZHYx"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        return render_template('itinerary_r.html', data=data, city=city, cities=cities, itinerary_aliases=itinerary_aliases)


    else:
        return render_template('itinerary.html', cities=cities, itinerary_aliases=itinerary_aliases)