#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="Tanner",
    version="0.6.0",
    description="He who flays the hide",
    author="MushMush Foundation",
    author_email="glastopf@public.honeynet.org",
    url="https://github.com/mushorg/tanner",
    packages=find_packages(exclude=["*.pyc"]),
    scripts=["bin/tanner", "bin/tannerweb", "bin/tannerapi"],
    data_files=[
        ("/opt/tanner/db/", ["/opt/tanner/data/db_config.json", "/opt/tanner/data/GeoLite2-City.mmdb"]),
        (
            "/opt/tanner/data/",
            [
                "/opt/tanner/data/dorks.pickle",
                "/opt/tanner/data/crawler_user_agents.txt",
                "/opt/tanner/files/engines/mako.py",
                "/opt/tanner/files/engines/tornado.py",
                "/opt/tanner/data/config.yaml",
            ],
        ),
    ],
)
