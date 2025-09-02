# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FastlyAPIKeyType(ModelSimple):
    """
    The definition of the `FastlyAPIKey` object.

    :param value: If omitted defaults to "FastlyAPIKey". Must be one of ["FastlyAPIKey"].
    :type value: str
    """

    allowed_values = {
        "FastlyAPIKey",
    }
    FASTLYAPIKEY: ClassVar["FastlyAPIKeyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FastlyAPIKeyType.FASTLYAPIKEY = FastlyAPIKeyType("FastlyAPIKey")
