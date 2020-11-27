#################
drf-imgproxy-demo
#################

Django REST Framework project to demonstrate drf-imgproxy.

This project uses `django-storages
<https://github.com/jschneier/django-storages>`_ as the media storage
backend with `MinIO <https://minio.io>`_ as the object storage server.

*****
Usage
*****

0. Requirements
===============

This project requires Docker and docker-compose setup on your local
system.

1. Quickstart
=============

Simply start the project with docker-compose

.. code:: console
   $ docker-compose up

Now you're able to visit the website at http://localhost:8000.
