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
    from datadog_api_client.v1.model.topology_query_data_streams_or_service_map_data_source import (
        TopologyQueryDataStreamsOrServiceMapDataSource,
    )


class TopologyQueryDataStreamsOrServiceMap(ModelNormal):
    validations = {
        "filters": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.topology_query_data_streams_or_service_map_data_source import (
            TopologyQueryDataStreamsOrServiceMapDataSource,
        )

        return {
            "data_source": (TopologyQueryDataStreamsOrServiceMapDataSource,),
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
        data_source: TopologyQueryDataStreamsOrServiceMapDataSource,
        filters: List[str],
        query_string: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query to service-based topology data sources like the service map or data streams.

        :param data_source: Name of the data source
        :type data_source: TopologyQueryDataStreamsOrServiceMapDataSource

        :param filters: Your environment and primary tag (or * if enabled for your account).
        :type filters: [str]

        :param query_string: A search string for filtering services, used in ``data_streams`` queries only. When set, this replaces the ``service`` field
        :type query_string: str, optional

        :param service: Name of the service
        :type service: str, optional
        """
        if query_string is not unset:
            kwargs["query_string"] = query_string
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.filters = filters
