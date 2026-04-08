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


class ProductAnalyticsAudienceOccurrenceFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "operator": (str,),
            "value": (str,),
        }

    attribute_map = {
        "operator": "operator",
        "value": "value",
    }

    def __init__(self_, operator: Union[str, UnsetType] = unset, value: Union[str, UnsetType] = unset, **kwargs):
        """
        Filter applied to occurrence counts when building a Product Analytics audience.

        :param operator: The comparison operator used for the occurrence filter (for example: ``gt`` , ``lt`` , ``eq`` ).
        :type operator: str, optional

        :param value: The threshold value to compare occurrence counts against.
        :type value: str, optional
        """
        if operator is not unset:
            kwargs["operator"] = operator
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
