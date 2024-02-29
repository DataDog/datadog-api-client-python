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


class MetricDashboardAttributes(ModelNormal):
    validations = {
        "popularity": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "popularity": (float,),
            "title": (str,),
        }

    attribute_map = {
        "popularity": "popularity",
        "title": "title",
    }

    def __init__(self_, popularity: Union[float, UnsetType] = unset, title: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes related to the dashboard, including title and popularity.

        :param popularity: Value from 0 to 5 that ranks popularity of the dashboard.
        :type popularity: float, optional

        :param title: Title of the asset.
        :type title: str, optional
        """
        if popularity is not unset:
            kwargs["popularity"] = popularity
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
