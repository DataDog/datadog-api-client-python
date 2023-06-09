# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DowntimeResourceType(ModelSimple):
    """
    Downtime resource type.

    :param value: If omitted defaults to "downtime". Must be one of ["downtime"].
    :type value: str
    """

    allowed_values = {
        "downtime",
    }
    DOWNTIME: ClassVar["DowntimeResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DowntimeResourceType.DOWNTIME = DowntimeResourceType("downtime")
