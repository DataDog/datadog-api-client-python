# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TagIndexingRulesResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total": (int,),
        }

    attribute_map = {
        "total": "total",
    }

    def __init__(self_, total: Union[int, UnsetType] = unset, **kwargs):
        """
        Pagination metadata for a list of tag indexing rules.

        :param total: Total number of tag indexing rules in the org.
        :type total: int, optional
        """
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
