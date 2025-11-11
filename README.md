# Job-Scout

## Intro
Job-Scout collates job opportunities from multiple sources in a single query.

Job-Scout is a console tool that can generate and save API queries in properly formatted `json`, that are used to perform `GET` requests on OpenWeb Ninja's JSearch API.

The `GET` request returns a data stream that is formatted and saved to the `search_results` directory, by default, as a `json` file.

Our motivation for building this tool was to aid in finding attractive job opportunities. Beyond this, there is scope to use this tool for deeper analysis, including:
- market trends
    - e.g., the changing availability of junior roles in your particular field
- economic trends
    - e.g., changes in base salaries over time
- sociological trends
    - e.g., expected background expertise, such as a qualifying degree or number of years of experience 

## Pre-requisites
Before running the tool, ensure you meet the following requirements:
```
**Python** V3.13
**Git** for version control
```

## API Token
Job-Scout makes use of [OpenWeb Ninja's JSearch API](https://www.openwebninja.com/api/jsearch). You must first register with OpenWeb Ninja to obtain a token to authenticate with when making a `GET` request.

By default, Job-scout looks for an API token in your environment variables. The token must be labelled as `API_KEY`, and can be stored in a `.env` file in the root of the project.

Here's what a `.env` file might look like:
```env
API_KEY="EXAMPLE_TOKEN"
```

## Deploying in the Console
To deploy, navigate to the root of the project and enter the following into a console:
```
python src/main.py
```

## Requirements
Core packages:
- requests
- python-dotenv
- bandit
- black
- coverage

A full list of packages, and their dependencies, can be found in `requirements.txt` in the root of the project.

## Contributing
To contribute to Job-Scout, please follow these steps:
1. Fork this repository.
2. Create a branch: git checkout -b <branch_name>.
3. Make your changes and commit them: git commit -m '<commit_message>'
4. Push to the original branch: git push origin <project_name>/<location>
5. Create the pull request.

## Contributors
- [@ellweaver](https://github.com/ellweaver) **Ell Weaver**
- [@Seb Allen](https://github.com/Seb-Allen) **Seb Allen**