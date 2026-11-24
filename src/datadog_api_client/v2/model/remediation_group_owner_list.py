# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RemediationGroupOwnerList(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "items": ([str],),
            "total": (int,),
        }

    attribute_map = {
        "items": "items",
        "total": "total",
    }

    def __init__(self_, items: List[str], total: int, **kwargs):
        """
        Owners of the group's open findings. ``items`` lists at most 5 owners, the owners of the most findings first,
        then by name. ``total`` counts every distinct owner, so the list is cut when ``total`` is larger than the number
        of items.

        :param items: Owners of the most findings in the group, at most 5.
        :type items: [str]

        :param total: Number of distinct owners across the group's findings.
        :type total: int
        """
        super().__init__(kwargs)

        self_.items = items
        self_.total = total
