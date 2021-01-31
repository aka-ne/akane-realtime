# Akane Track
================================

This a very simple proof of concept of a realtime position tracking system, using modern tecnologies like deta, fastapi, mqtt, mapbox and owntracks


Installation
------------

```bash
git clone https://github.com/aka-ne/realtime-tracking.git
cd realtime-tracking
virtualenv -p python3 env 
. env/bin/activate
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

Navigate to [localhost:8000/map](http://localhost:8000/map) and done with the initial setup.


