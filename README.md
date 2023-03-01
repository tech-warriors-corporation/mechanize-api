# mechanize-api
Mechanize (API) assist people fix their car and reach their destination.

## Architecture 
- The helpers, services, controllers, repositories, enums and others files should have a **suffix** in name, example: `users_controller.py`;
- Repositories and enums should be named in **singular**, example: `user_repository.py`;
- Files should be in _snake_case_ and class name in _PascalCase_;
- Microservices should be in **plural** name.

## Microservices:
- [Accounts](https://github.com/tech-warriors-corporation/mechanize-accounts-api);
- [Helps](https://github.com/tech-warriors-corporation/mechanize-helps-api).

## Roadmap:
- [ ] Read about [blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints) to apply in routes;
- [ ] Use [Stock Management (API)](https://github.com/tech-warriors-corporation/stock-management-api) as example;
- [X] Block commits in main branch;
- [ ] Add [CORS](https://flask-cors.readthedocs.io/en/latest) to correct origin;
- [ ] Create events to communicate microservices;
- [ ] Verify if controller throw when repository or service throws;
- [ ] Get user tokenized from JWT ([PyJWT](https://pyjwt.readthedocs.io/en/stable));
- [ ] Read about [add_url_rule](https://tedboy.github.io/flask/generated/generated/flask.Flask.add_url_rule.html);
- [ ] See this [Saga architecture pattern](https://github.com/victoramsantos/saga-pattern-example) example;
- [ ] Created base classes for services, repositories, controllers and others;
- [ ] Connect to development and production databases;
- [ ] Set environment variables and remove hardcoded properties;
- [ ] Study about **Decompose by Subdomain**, **API Composition**, **API Gateway** and **Healthcheck**;
- [ ] Remove _FOREIGN KEY_ at databases;
- [ ] Check all repositories and documentations;
- [ ] Do get of user from id in [Accounts](https://github.com/tech-warriors-corporation/mechanize-accounts-api) microservice;
- [ ] Make service create in [Helps](https://github.com/tech-warriors-corporation/mechanize-helps-api) microservice.
