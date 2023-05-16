# Colorado info app
#### Video Demo:  <https://drive.google.com/file/d/1fvECnPLUAOIjpQLx7ygtmPuFTulDBG_x/view?usp=sharing>
#### Description:
#### The Colorado Info App is a web application that consolidates information from various online sources to provide valuable insights into the state of Colorado and its counties. By leveraging data from Wikipedia, the Colorado Information Marketplace, and the Yelp Fusion API, this application offers users a comprehensive understanding of Colorado's demographics, county-specific information, and recommended itineraries.

## Project webpages
### Homepage
#### The homepage serves as an introduction to the website, offering general information about the state of Colorado sourced from Wikipedia. This section provides users with an overview of the state's history, geography, and notable attractions. By utilizing the Wikipedia plugin, which incorporates the Wikipedia API, the application dynamically fetches and displays up-to-date information.
### Projection query
#### The projection query page allows users to input parameters such as the year, county, and gender to retrieve population data for a specific demographic. To optimize data manipulation, the population information is stored in a SQLite3 database, which enables faster data retrieval and manipulation. Upon submission of the query, the application fetches the relevant population numbers and displays them to the user.
### Projection graph
#### The projection graph page enables users to visualize the population growth of a selected county over time. Leveraging the power of the pandas module for data manipulation and plotly for interactive graphing, this page provides an intuitive graphical representation of population trends. By selecting a county, users can explore and analyze population growth patterns conveniently.
### Counties info
#### The counties info page allows users to select a specific county of Colorado and retrieve detailed information about it from Wikipedia. By utilizing the Wikipedia module, the application fetches the relevant county's information, including its history, demographics, economy, and notable landmarks. This feature provides users with a comprehensive overview of each county's unique characteristics.
### Itineraries search
#### The itineraries search page offers users the ability to search for itineraries based on county and itinerary type. The application fetches a list of cities associated with the selected county using the zipcodes module. Leveraging the Yelp Fusion API, the application gathers itinerary information, including recommended restaurants, tourist attractions, and points of interest. These itineraries are then displayed on an interactive map powered by the Leaflet library, providing users with an immersive and informative travel planning experience.

#### The Colorado Info App brings together disparate sources of information to create a centralized platform for exploring the state of Colorado. Whether users are interested in demographic trends, county-specific details, or planning their itineraries, this web application offers a user-friendly and comprehensive solution.
