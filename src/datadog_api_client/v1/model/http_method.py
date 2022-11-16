# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HTTPMethod(ModelSimple):
    """
    The HTTP method.

    :param value: Must be one of ["GET", "POST", "PATCH", "PUT", "DELETE", "HEAD", "OPTIONS"].
    :type value: str
    """

    allowed_values = {
        "GET",
        "POST",
        "PATCH",
        "PUT",
        "DELETE",
        "HEAD",
        "OPTIONS",
    }
    GET: ClassVar["HTTPMethod"]
    POST: ClassVar["HTTPMethod"]
    PATCH: ClassVar["HTTPMethod"]
    PUT: ClassVar["HTTPMethod"]
    DELETE: ClassVar["HTTPMethod"]
    HEAD: ClassVar["HTTPMethod"]
    OPTIONS: ClassVar["HTTPMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HTTPMethod.GET = HTTPMethod("GET")
HTTPMethod.POST = HTTPMethod("POST")
HTTPMethod.PATCH = HTTPMethod("PATCH")
HTTPMethod.PUT = HTTPMethod("PUT")
HTTPMethod.DELETE = HTTPMethod("DELETE")
HTTPMethod.HEAD = HTTPMethod("HEAD")
HTTPMethod.OPTIONS = HTTPMethod("OPTIONS")
