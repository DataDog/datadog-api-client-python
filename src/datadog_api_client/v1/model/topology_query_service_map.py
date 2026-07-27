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
    from datadog_api_client.v1.model.topology_query_service_map_data_source import TopologyQueryServiceMapDataSource


class TopologyQueryServiceMap(ModelNormal):
    validations = {
        "filters": {
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_query_service_map_data_source import TopologyQueryServiceMapDataSource

        return {
            "data_source": (TopologyQueryServiceMapDataSource,),
            "filters": ([str],),
            "query_string": (str,),
            "service": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "filters": "filters",
        "query_string": "query_string",
        "service": "service",
    }

    def __init__(
        self_,
        data_source: TopologyQueryServiceMapDataSource,
        filters: List[str],
        service: str,
        query_string: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query to the service map topology data source.

        :param data_source: Name of the data source.
        :type data_source: TopologyQueryServiceMapDataSource

        :param filters: Your environment and primary tag (or * if enabled for your account).
        :type filters: [str]

        :param query_string: A search string for filtering services. When set, this replaces the ``service`` field.
        :type query_string: str, optional

        :param service: (deprecated) Name of the service. Leave this empty and use query_string instead.
        :type service: str
        """
        if query_string is not unset:
            kwargs["query_string"] = query_string
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.filters = filters
        self_.service = service
