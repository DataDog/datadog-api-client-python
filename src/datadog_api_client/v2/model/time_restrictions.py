# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.time_restriction import TimeRestriction


class TimeRestrictions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.time_restriction import TimeRestriction

        return {
            "restrictions": ([TimeRestriction],),
            "time_zone": (str,),
        }

    attribute_map = {
        "restrictions": "restrictions",
        "time_zone": "time_zone",
    }

    def __init__(self_, restrictions: List[TimeRestriction], time_zone: str, **kwargs):
        """
        Holds time zone information and a list of time restrictions for a routing rule.

        :param restrictions: Defines the list of time-based restrictions.
        :type restrictions: [TimeRestriction]

        :param time_zone: Specifies the time zone applicable to the restrictions.
        :type time_zone: str
        """
        super().__init__(kwargs)

        self_.restrictions = restrictions
        self_.time_zone = time_zone
