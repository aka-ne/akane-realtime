# Akane Track
=============

This a very simple proof of concept of a realtime position tracking system, using modern tecnologies like deta, fastapi, mqtt, mapbox and owntracks


Installation
------------

```bash
mkdir app && cd app
git clone https://github.com/aka-ne/realtime-tracking.git
virtualenv -p python3 env 
. env/bin/activate
cd realtime-tracking
pip install -r requirements.txt
```

Now in one terminal type (with virtual enviroment activated)
```bash
python sub_client.py
```

In other terminal type (with virtual enviroment activated)
```bash
uvicorn main:app --reload
```

In sub_client.py change `TOPIC = 'test/owntracks'` to a diferent topic like `'realtime/app/track'` or something

Navigate to [localhost:8000/map](http://localhost:8000/map) and done with the initial setup.


Owntracks setup
---------------

Install from the `app store` or `play store`. Make sure MQTT is selected in `preference->connection->mode`

Navigate to `preference->connection->host` and fill with.
```bash
Host : test.mosquitto.org
Port: 1883
Client ID: wherever-id
```

Navigate to p`reference->connection->identification` and fill device id and tracker id only.
```bash
Username: blank
Password: blank
Device ID: GalaxyS5 (or your phone model)
Tracker ID: s5
```

Now go to `preference->configuration managment->editor` and fill it with.
```bash
key:
pubTopicBase
value:
test/owntracks 
```
Note that if you changed the topic in `sub_client.py` it must be match with the value above

At this point, you have the service deployed on a local machine, using a local database called [TinyDB](https://tinydb.readthedocs.io/en/latest/) and can work as that, but we can use cloud base database and host for our service, is here where [deta](https://deta.sh) come to action. Deta provide a cloud base nosql database and a micro cloud hosting service 

Grab a [deta.sh](https://web.deta.sh) account, go to `settings->create key` you'll be prompt with key name, key description and project key, copy the `project key` and paste it in `db.py` `KEY = 'project key'` and `uncomment` the lines in sub_client.py and main.py

Now run `db_conf.py` (with virtual enviroment activated)
```bash
python db_conf.py
```

You will see in the output.
```bash
detaBase is empty
Inserting payload in database
Your id is: 
8vnujsnjq2fl # Yours will be something similar
```

Copy the generated id and paste in `db.py`->`BaseKey = 'generated id'`

Navigate to [web.deta.sh](https://web.deta.sh) in Bases tab, there will be a new data base created, called realtime (database name can be changed in `db.py`->`BASE = 'realtime'`) with a single entry (the payload we inserted with the `db_conf.py`) and there will live our last position received by owntracks

Now let's use deta Micros but first install the deta CLI

```bash
curl -fsSL https://get.deta.dev/cli.sh | sh
```

check if deta cli installed sucesfully

```bash
deta --help
```

If you get error you must add the cli to your path

```bash
export PATH="$PATH:/home/<user>/.deta/bin"
```

Now type.
```bash
deta login # A browser window will prompt to login
deta new
deta deploy
```

Navigate to [web.deta.sh](https://web.deta.sh) in Micros tab, there will be a new micro cloud called realtime-track, inside is a link for your new service. Navigate to it and you will see the `{'hola':'mundo'}` output in the browser

Note that if you use a deta micros or any other provider, the `mbox.html` in template folder must be changed from `var url = 'https://localhost:8000/deta1';` to `var url = 'https://domain-name/deta';`

The `sub_client.py` must be opened all the time on your pc or in a cloud provider to listen on the topic to be able to update the database. You can use aws, gcloud or whatever but i personaly use the cheapest vps/droplet from digitalocean for my `sub_client.py` and my self hosted mqtt broker. 

If you plan to use digitalocean, use my link to get 100$ in credits [Digital Ocean](https://m.do.co/c/9547090d642b)

Cheers
