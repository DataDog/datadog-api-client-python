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
    from datadog_api_client.v1.model.journey_map_group_by_audience import JourneyMapGroupByAudience


class JourneyMapGroupBy(ModelNormal):
    validations = {
        "facet": {},
        "value_filters": {
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.journey_map_group_by_audience import JourneyMapGroupByAudience

        return {
            "facet": (str,),
            "source": (JourneyMapGroupByAudience,),
            "value_filters": ([str],),
        }

    attribute_map = {
        "facet": "facet",
        "source": "source",
        "value_filters": "value_filters",
    }

    def __init__(
        self_,
        facet: str,
        value_filters: List[str],
        source: Union[JourneyMapGroupByAudience, UnsetType] = unset,
        **kwargs,
    ):
        """
        Group by configuration for the Journey Paths widget.

        :param facet: Facet to group by. Must be a valid tag name.
        :type facet: str

        :param source: Audience the group by facet is read from.
        :type source: JourneyMapGroupByAudience, optional

        :param value_filters: Facet values to keep.
        :type value_filters: [str]
        """
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)

        self_.facet = facet
        self_.value_filters = value_filters
