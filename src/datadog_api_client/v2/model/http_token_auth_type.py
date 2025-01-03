# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HTTPTokenAuthType(ModelSimple):
    """
    The definition of `HTTPTokenAuthType` object.

    :param value: If omitted defaults to "HTTPTokenAuth". Must be one of ["HTTPTokenAuth"].
    :type value: str
    """

    allowed_values = {
        "HTTPTokenAuth",
    }
    HTTPTOKENAUTH: ClassVar["HTTPTokenAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HTTPTokenAuthType.HTTPTOKENAUTH = HTTPTokenAuthType("HTTPTokenAuth")
