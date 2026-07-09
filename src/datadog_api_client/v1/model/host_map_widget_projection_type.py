# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostMapWidgetProjectionType(ModelSimple):
    """
    Type of the host map projection.

    :param value: If omitted defaults to "hostmap". Must be one of ["hostmap"].
    :type value: str
    """

    allowed_values = {
        "hostmap",
    }
    HOSTMAP: ClassVar["HostMapWidgetProjectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostMapWidgetProjectionType.HOSTMAP = HostMapWidgetProjectionType("hostmap")
