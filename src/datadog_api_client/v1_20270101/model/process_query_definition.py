# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProcessQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "filter_by": ([str],),
            "is_normalized_cpu": (bool,),
            "limit": (float,),
            "metric": (str,),
            "query_filter": (str,),
            "search_by": (str,),
        }

    attribute_map = {
        "filter_by": "filter_by",
        "is_normalized_cpu": "is_normalized_cpu",
        "limit": "limit",
        "metric": "metric",
        "query_filter": "query_filter",
        "search_by": "search_by",
    }

    def __init__(
        self_,
        limit: float,
        metric: str,
        filter_by: Union[List[str], UnsetType] = unset,
        is_normalized_cpu: Union[bool, UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        search_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param filter_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter_by: [str], optional

        :param is_normalized_cpu: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_normalized_cpu: bool, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float

        :param metric: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric: str

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param search_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type search_by: str, optional
        """
        if filter_by is not unset:
            kwargs["filter_by"] = filter_by
        if is_normalized_cpu is not unset:
            kwargs["is_normalized_cpu"] = is_normalized_cpu
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if search_by is not unset:
            kwargs["search_by"] = search_by
        super().__init__(kwargs)

        self_.limit = limit
        self_.metric = metric
