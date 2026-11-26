# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TreeDataProjectionSunburstDimensionsItemsDimension(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["group", "value"].
    :type value: str
    """

    allowed_values = {
        "group",
        "value",
    }
    GROUP: ClassVar["TreeDataProjectionSunburstDimensionsItemsDimension"]
    VALUE: ClassVar["TreeDataProjectionSunburstDimensionsItemsDimension"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TreeDataProjectionSunburstDimensionsItemsDimension.GROUP = TreeDataProjectionSunburstDimensionsItemsDimension("group")
TreeDataProjectionSunburstDimensionsItemsDimension.VALUE = TreeDataProjectionSunburstDimensionsItemsDimension("value")
