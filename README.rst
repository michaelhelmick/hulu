Hulu
====

``hulu`` attempts to make it easy for developers to interact with the `Hulu`_ "hidden" 2.0 API

The Story
---------

A friend of mine, (`@adammagana <https://github.com/adammagana>`_) created a PHP library (`found here <https://github.com/adammagana/hulu-php-library/>`_) to interact with the `Hulu`_ "hidden" 1.0 API. The 1.0 API only returns XML, but someone opened up an issue revealing some 2.0 endpoints that return JSON.

Since JSON is easier to work with in Python than XML is, I took it upon myself to try an open up their API to other developers.

Features
--------

- List companies that have shows/videos on Hulu
- List videos from a specific show
- List trailers available on Hulu
- Find the position of a given video within the shows video list
- (Kind of) Much more!

Installation
------------

::

    $ pip install hulu

Example Usage
-------------
::

    from hulu import Hulu
    h = HuluAPI()
    try:
        h.get_companies()
    except HuluError as e:
        print e

    try:
        h.get_video_info(441295)
    except HuluError as e:
        print e


Contribute
----------

If anyone has additional information (such as; paramters taken to given API methods, extra API methods not yet found, etc.) please feel free to open a Pull Request! :)

TODO
----

- Figure out authentication!

Some API methods require authentication, yet I haven't been able to figure out how to authenticate to make those API calls, these API calls include:
::

    api/2.0/plus_upsell.json
    api/2.0/favorited_show_ids
    api/2.0/queued_video_ids


.. _Hulu: http://hulu.com/
.. _adammagana: https://github.com/adammagana