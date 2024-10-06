# FastAPI Docker Project

This project is a simple FastAPI application that demonstrates how to build and deploy a web API using Docker. The application includes a scraper that fetches the IP address from a specified URL.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Complexities](#complexities)
- [Solutions](#solutions)
- [Challenges](#challenges)
- [License](#license)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/faisal-fida/fastapi_docker_project.git
cd fastapi_docker_project
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file with the following content:

```
URL=<your_url_here>
```

4. Run the application:

```sh
uvicorn app:app --reload
```

## Usage

The application provides two endpoints:

1. `GET /` - Returns a message indicating the server is running.
2. `GET /ip` - Returns the IP address fetched by the scraper.

- **Environment Variables**: The project uses `python-dotenv` to manage environment variables, which allows for secure and flexible configuration.
- **Dependency Management**: Dependencies are managed using a `requirements.txt` file, ensuring that the correct versions of packages are used.
- **External API Dependency**: The scraper relies on an external URL to fetch the IP address. Network issues or changes in the external API could affect the application's functionality.
- **Configuration Management**: Managing environment variables securely and ensuring they are correctly set up can be challenging, especially in different environments (development, staging, production).

## License

This project is licensed under the MIT License. See the LICENSE file for details.
