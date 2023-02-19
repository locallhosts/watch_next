# Watch_Next

## About

Watch_Next is a Python application that recommends movies based on their similarity to movies you've already watched.

## Requirements

- Docker
- Git

## Installation

To install Watch_Next, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/locallhosts/watch_next.git


2. Build the Docker image:

   **docker build -t watch_next .**



3. Run the Docker container:

    **docker run -p 80:80 watch_next**


4. Open your web browser and navigate to http://localhost:80.

## Usage

To use Watch_Next, simply enter the name of a movie you've already watched and its description. Watch_Next will then recommend a list of similar movies for you to watch next.


that is for docker, or you can can easily run on your  python favorite editor
