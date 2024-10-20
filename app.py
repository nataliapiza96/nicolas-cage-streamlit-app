import streamlit as st
import pandas as pd

# Load the cleaned dataset from the CSV file
@st.cache_data
def load_data():
    # Replace with the correct file path in your GitHub repository
    df = pd.read_csv('cleaned_nicolas_cage_data.csv')  # Ensure the file name is correct
    return df

# Load the data into df_clean
df_clean = load_data()

# Title of the app
st.title("Nicolas Cage Filmography Insights")

# Display dataset preview
st.write("Here is a preview of Nicolas Cage's cleaned filmography dataset:")
st.dataframe(df_clean.head())

# Display the number of movies Nicolas Cage has acted in
st.subheader("Number of Movies")
num_movies = df_clean.shape[0]
st.write(f"Nicolas Cage has acted in {num_movies} movies.")

# Display the highest and lowest rated movies
st.subheader("Highest and Lowest Rated Movies")
highest_rated_movie = df_clean.loc[df_clean['Rating'].idxmax()]
lowest_rated_movie = df_clean.loc[df_clean['Rating'].idxmin()]
st.write(f"The highest-rated movie is '{highest_rated_movie['Title']}' ({highest_rated_movie['Year']}) with a rating of {highest_rated_movie['Rating']}.")
st.write(f"The lowest-rated movie is '{lowest_rated_movie['Title']}' ({lowest_rated_movie['Year']}) with a rating of {lowest_rated_movie['Rating']}.")

# Display the genre of the highest-rated movie
highest_rated_movie_genre = highest_rated_movie['Genre']
st.write(f"The genre of the highest-rated movie is: {highest_rated_movie_genre}")

# Display the average IMDb rating and Metascore
st.subheader("Average Ratings and Metascore")
average_rating = df_clean['Rating'].mean()
average_metascore = df_clean['Metascore'].mean()
st.write(f"The average IMDb rating of Nicolas Cage's movies is: {average_rating:.2f}")
st.write(f"The average Metascore of Nicolas Cage's movies is: {average_metascore:.2f}")

# Display the most common genre
st.subheader("Most Common Genre")
genre_series = df_clean['Genre'].str.split(',', expand=True).stack().reset_index(drop=True)
most_common_genre = genre_series.value_counts().idxmax()
st.write(f"The genre Nicolas Cage has acted in the most is: {most_common_genre}")

# Distribution of movies by genre
st.subheader("Distribution of Movies by Genre")
genre_counts = genre_series.value_counts()
st.bar_chart(genre_counts)

# IMDb rating trend over the years
st.subheader("IMDb Rating Trend Over the Years")
rating_trend = df_clean.groupby('Year')['Rating'].mean()
st.line_chart(rating_trend)

# Display number of movies per decade
st.subheader("Number of Movies per Decade")
df_clean['Decade'] = (df_clean['Year'] // 10) * 10
movies_per_decade = df_clean['Decade'].value_counts().sort_index()
st.bar_chart(movies_per_decade)

# Display the year with the most movies
st.subheader("Year with the Most Movies")
year_with_most_movies = df_clean['Year'].value_counts().idxmax()
most_movies_count = df_clean['Year'].value_counts().max()
st.write(f"The year with the most movies is {year_with_most_movies} with {most_movies_count} movies.")

# Display the actor Nicolas Cage has acted with the most
st.subheader("Actor Nicolas Cage Has Acted with the Most")
co_actors_series = df_clean['Cast'].str.replace("Nicolas Cage", "", case=False).str.split(',').explode().str.strip()
co_actors_series = co_actors_series[co_actors_series != ""]
most_common_co_actor = co_actors_series.value_counts().idxmax()
most_common_co_actor_count = co_actors_series.value_counts().max()
st.write(f"Nicolas Cage has acted the most with {most_common_co_actor}, in {most_common_co_actor_count} movies.")

