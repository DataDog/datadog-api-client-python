# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumConfigType(ModelSimple):
    """
    The type of the resource. The value should always be `rum_config`.

    :param value: If omitted defaults to "rum_config". Must be one of ["rum_config"].
    :type value: str
    """

    allowed_values = {
        "rum_config",
    }
    RUM_CONFIG: ClassVar["RumConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumConfigType.RUM_CONFIG = RumConfigType("rum_config")
