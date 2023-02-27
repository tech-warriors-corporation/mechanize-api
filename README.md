# mechanize-api
Mechanize (API) helps people fix their car and reach their destination.

## Architecture
- The helpers, services, controllers, repositories, enums and others files should have a **suffix** in name, example: `users_controller.py`;
- Repositories and enums should be named in **singular**, example: `user_repository.py`;
- Files should be in _snake_case_ and class name in _PascalCase_;
- In `projects` folder has microservices and `commons` directory for help development;
- Microservices should be in **plural** name.

## Setup
Create a `.env` file with `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` and `CRYPTOCODE_PASSWORD` variables to work.

## Dependencies
Use `pip install -r requirements.txt` to install dependencies. If return an error, use previous command with `sudo` to have root permissions.

## Start
Run `python -m app` to start project.

## Roadmap:
- [ ] Read about [blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints) to replace `prefixes.py` file;
- [ ] Use [stock management project (api)](https://github.com/tech-warriors-corporation/stock-management-api) as example;
- [X] Block commits in main branch;
- [ ] Add [CORS](https://flask-cors.readthedocs.io/en/latest) to correct origin;
- [ ] Create event bus to communicate microservices with Saga (design pattern);
- [ ] Verify if controller throw when repository or service throws;
- [ ] Get user tokenized from JWT ([PyJWT](https://pyjwt.readthedocs.io/en/stable));
- [ ] Read about [add_url_rule](https://tedboy.github.io/flask/generated/generated/flask.Flask.add_url_rule.html);
- [ ] See this [Saga](https://github.com/victoramsantos/saga-pattern-example) example;
- [ ] Created base classes for services, repositories, controllers and others;
- [ ] Connect to development and production database;
- [ ] Set environment variables and remove hardcoded properties;
- [ ] Study about **Decompose by Subdomain**, **API Composition**, **API Gateway** and **Healthcheck**;
- [ ] Remove FOREIGN KEY at `script.sql`.
