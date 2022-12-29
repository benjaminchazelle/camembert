docker run -ti -v $PWD:/host -v $PWD/cache:/.cache -v $PWD/site-packages:/opt/bitnami/python/lib/python3.8/site-packages -p 3000:3000 -u root bitnami/pytorch:latest python /host/server.py
