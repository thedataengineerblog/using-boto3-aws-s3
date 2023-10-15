# Using Amazon S3 with boto3 SDK

## Setup Environment

First, we have to create a virtual environment with Python. You can run the command below to do this.

```console
thedataengineerblog@desktop$ python3 -m venv venv
```

Second, we have to install the packages found in requirements.txt. Execute the command below:

```console
thedataengineerblog@desktop$ pip install -r requirements.txt
```

Third, we have to activate our environment. You can run the command below to do this too.

```console
thedataengineerblog@desktop$ source venv/bin/activate
```

## File config

On this repo you will find a file called config.cfg. In this file there are 2 keys that you must change.

- ACCESS_KEY
- SECRET_KEY

You just have to put your keys in there.

Example:

```conf
[aws-credentials]
ACCESS_KEY=<<insert your ACCESS_KEY>>
SECRET_KEY=<<insert your SECRET_KEY>>
```

This file will load into a program and we can avoid exposing our credentials.

## Execute the program

Doing this, we can execute the program using the following command:

```console
thedataengineerblog@desktop$ python aws_s3.py
```

You find more information in the original blog post: https://thedataengineer.com.br/