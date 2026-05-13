# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.time_restriction import TimeRestriction


class RoutingRuleEscalationPolicyActionSupportHours(ModelNormal):
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

    def __init__(self_, time_zone: str, restrictions: Union[List[TimeRestriction], UnsetType] = unset, **kwargs):
        """
        Support hours during which the escalation policy will be executed. Outside of these hours, the escalation policy will be on hold and triggered once the next support hours window starts.

        :param restrictions: The list of support hours time windows.
        :type restrictions: [TimeRestriction], optional

        :param time_zone: The time zone in which the support hours are expressed.
        :type time_zone: str
        """
        if restrictions is not unset:
            kwargs["restrictions"] = restrictions
        super().__init__(kwargs)

        self_.time_zone = time_zone
