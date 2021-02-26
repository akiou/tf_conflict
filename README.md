# tf_conflict

## Reproduce a conflict exception in local environment

```sh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ pip install -e .
(venv) $ mvn clean install -f tf_conflict-java/pom.xml
(venv) $ python test/conflict.py # raise exception
```

### Reproduce a conflict exception with docker container

```sh
$ docker build -t tf_conflict .
$ docker run -it -v $(pwd):/src tf_conflict bash
root@170297a71e0a:/src# mvn clean install -f tf_conflict-java/pom.xml
root@170297a71e0a:/src# python test/conflict.py # raise exception
```
