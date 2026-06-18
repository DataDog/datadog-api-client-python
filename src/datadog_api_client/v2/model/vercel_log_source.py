# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class VercelLogSource(ModelSimple):
    """
    Source of logs that Vercel forwards to Datadog.

    :param value: Must be one of ["static", "lambda", "edge", "build", "external", "firewall"].
    :type value: str
    """

    allowed_values = {
        "static",
        "lambda",
        "edge",
        "build",
        "external",
        "firewall",
    }
    STATIC: ClassVar["VercelLogSource"]
    LAMBDA: ClassVar["VercelLogSource"]
    EDGE: ClassVar["VercelLogSource"]
    BUILD: ClassVar["VercelLogSource"]
    EXTERNAL: ClassVar["VercelLogSource"]
    FIREWALL: ClassVar["VercelLogSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


VercelLogSource.STATIC = VercelLogSource("static")
VercelLogSource.LAMBDA = VercelLogSource("lambda")
VercelLogSource.EDGE = VercelLogSource("edge")
VercelLogSource.BUILD = VercelLogSource("build")
VercelLogSource.EXTERNAL = VercelLogSource("external")
VercelLogSource.FIREWALL = VercelLogSource("firewall")
