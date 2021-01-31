# Akane Track
================================

This a very simple proof of concept of a realtime position tracking system, using modern tecnologies like deta, fastapi, mqtt, mapbox and owntracks

* Installation_
* `Known limitations`_
* `Usage and API`_
    * `Client`_
        * `Constructor / reinitialise`_
        * `Option functions`_
        * `Connect / reconnect / disconnect`_
        * `Network loop`_
        * `Publishing`_
        * `Subscribe / Unsubscribe`_
        * `Callbacks`_
        * `External event loop support`_
        * `Global helper functions`_
    * `Publish`_
        * `Single`_
        * `Multiple`_
    * `Subscribe`_
        * `Simple`_
        * `Using Callback`_
* `Reporting bugs`_
* `More information`_





Installation
------------

```bash
git clone https://github.com/aka-ne/realtime-tracking.git
cd realtime-tracking
virtualenv -p python3 env 
. env/bin/activate

