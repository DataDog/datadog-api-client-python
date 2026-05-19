# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseAggregateGroupBy(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "groups": ([str],),
            "limit": (int,),
        }

    attribute_map = {
        "groups": "groups",
        "limit": "limit",
    }

    def __init__(self_, groups: List[str], limit: int, **kwargs):
        """
        Configuration for grouping aggregated results by one or more case fields.

        :param groups: Fields to group by.
        :type groups: [str]

        :param limit: Maximum number of groups to return.
        :type limit: int
        """
        super().__init__(kwargs)

        self_.groups = groups
        self_.limit = limit
