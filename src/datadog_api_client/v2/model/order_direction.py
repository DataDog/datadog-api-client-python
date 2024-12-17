# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrderDirection(ModelSimple):
    """
    The sort direction for results.

    :param value: Must be one of ["asc", "desc"].
    :type value: str
    """

    allowed_values = {
        "asc",
        "desc",
    }
    ASC: ClassVar["OrderDirection"]
    DESC: ClassVar["OrderDirection"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrderDirection.ASC = OrderDirection("asc")
OrderDirection.DESC = OrderDirection("desc")
