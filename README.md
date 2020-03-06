# api-project

## How to install

With the following command make a copy of this repo on your local machine

```
git clone git@github.com:paulinocamila/api-project.git
```

To start the project, run the docker-compose command from within the api_project folder
```
docker-compose up -d
```

## How to test

Make a POST request in the endpoint below using the header content-type: application/json

Here's an example:
```
curl -XPOST http://localhost:5000/cars -H "content-type: application/json" -d'{"cor":"preto", "placa":"EDF-1234", "ano":"2010/2011", "modelo":"hb20"}'
```


