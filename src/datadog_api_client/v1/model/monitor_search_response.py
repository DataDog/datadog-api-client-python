# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_search_response_counts import MonitorSearchResponseCounts
        from datadog_api_client.v1.model.monitor_search_response_metadata import MonitorSearchResponseMetadata
        from datadog_api_client.v1.model.monitor_search_result import MonitorSearchResult

        return {
            "counts": (MonitorSearchResponseCounts,),
            "metadata": (MonitorSearchResponseMetadata,),
            "monitors": ([MonitorSearchResult],),
        }

    attribute_map = {
        "counts": "counts",
        "metadata": "metadata",
        "monitors": "monitors",
    }
    read_only_vars = {
        "counts",
        "monitors",
    }

    def __init__(self, *args, **kwargs):
        """
        The response form a monitor search.

        :param counts: The counts of monitors per different criteria.
        :type counts: MonitorSearchResponseCounts, optional

        :param metadata: Metadata about the response.
        :type metadata: MonitorSearchResponseMetadata, optional

        :param monitors: The list of found monitors.
        :type monitors: [MonitorSearchResult], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorSearchResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
