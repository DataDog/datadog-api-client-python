# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomConnectionType(ModelSimple):
    """
    The custom connection type.

    :param value: If omitted defaults to "custom_connections". Must be one of ["custom_connections"].
    :type value: str
    """

    allowed_values = {
        "custom_connections",
    }
    CUSTOM_CONNECTIONS: ClassVar["CustomConnectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomConnectionType.CUSTOM_CONNECTIONS = CustomConnectionType("custom_connections")
