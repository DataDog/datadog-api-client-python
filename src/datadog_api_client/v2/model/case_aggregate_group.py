# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseAggregateGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "group": (str,),
            "value": ([float],),
        }

    attribute_map = {
        "group": "group",
        "value": "value",
    }

    def __init__(self_, group: str, value: List[float], **kwargs):
        """
        A single group within the aggregation results, containing the group key and its associated count values.

        :param group: The value of the field being grouped on (for example, ``OPEN`` when grouping by status).
        :type group: str

        :param value: The count of cases in this group.
        :type value: [float]
        """
        super().__init__(kwargs)

        self_.group = group
        self_.value = value
