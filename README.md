# Translator
Basic Translation Service using Libretranslate and Python

NOTE: For the first time initialization this application reqires atleast 30 mins to download all language packs.

## Usage

This application works by using the locales folder for the source data.
The default is `en` English.

Whatever translation you need you need to set a key value pair and run the application.

Install Docker or Podman


### Docker

Run command
```bash
docker-compose build
docker-compose up
# Stop
docker-compose stop

# Dont use Docker compose down as it will get rid of all the language packs as well.
```


### Podman

Install Podman
```bash
brew install podman
brew install podman-compose

podman machine init
podman machine start
```


Run Command
```bash
podman-compose build
podman-compose up

# Stop
podman-compose stop

# Dont use Podman compose down as it will get rid of all the language packs as well.
```