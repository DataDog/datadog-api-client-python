# Unless explicitly stated otherwise all files in this repository are licensed
# under the 3-clause BSD style license (see LICENSE).
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019 Datadog, Inc.

import os
import re

from setuptools import setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9]+\.[0-9]+\.[0-9]+.*)['"]''')


setup(
    version=VERSION_RE.search(open(os.path.join(ROOT, "src", "datadog_api_client", "version.py")).read()).group(1),
)
