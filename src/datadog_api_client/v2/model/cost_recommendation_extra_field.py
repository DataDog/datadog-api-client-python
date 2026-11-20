# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class CostRecommendationExtraField(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "path": (str,),
            "value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "path": "path",
        "value": "value",
    }

    def __init__(self_, path: str, value: Any, **kwargs):
        """
        A recommendation field selected by the request's ``extra_fields`` patterns.

        :param path: Dotted path of the matched field in the recommendation event's custom attributes.
        :type path: str

        :param value: Matched JSON value. Paths through arrays return the matched values as an array.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type
        """
        super().__init__(kwargs)

        self_.path = path
        self_.value = value
