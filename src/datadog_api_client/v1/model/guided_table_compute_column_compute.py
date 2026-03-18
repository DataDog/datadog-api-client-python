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


class GuidedTableComputeColumnCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "filter": (str,),
            "_property": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "filter": "filter",
        "_property": "property",
        "query": "query",
    }

    def __init__(
        self_,
        aggregation: str,
        query: str,
        filter: Union[str, UnsetType] = unset,
        _property: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregation configuration.

        :param aggregation: Aggregation type (e.g. ``avg`` , ``sum`` , ``count`` ).
        :type aggregation: str

        :param filter: Additional filter criteria.
        :type filter: str, optional

        :param _property: Attribute to aggregate on. Depends on the data source (e.g. a log attribute).
        :type _property: str, optional

        :param query: Name of the source query.
        :type query: str
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if _property is not unset:
            kwargs["_property"] = _property
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.query = query
