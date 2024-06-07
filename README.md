# Movie Recommendation System

This project is a movie recommendation system that uses machine learning to suggest movies based on movie description and summary. Follow the steps below to set up and run the application.

Ensure you have the following installed on your system:
- Python 3.x
- Streamlit
  ```bash
    pip install streamlit
    ```

## Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Download Required Files**

    Download the `movies_dict.pkl` and `similarity.pkl` files from [Google Drive](https://drive.google.com/drive/folders/1mA3hC6ifX8z-MySU64uMt_Af-x_Du_YU?usp=sharing).

    Place these files in the project directory.

3. **Run the Application**

    Execute the `app.py` file to start the application:

    ```bash
    streamlit run app.py
    ```

## Project Structure

- `app.py`: The main application script.
- `movies_dict.pkl`: Preprocessed movie data.
- `similarity.pkl`: Similarity matrix for movie recommendations.

## Usage

Once the application is running, you can interact with the movie recommendation system via the web interface. Select the name of a movie from the dropdown list to get recommendations.

