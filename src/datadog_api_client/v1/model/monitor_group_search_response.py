# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorGroupSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_group_search_response_counts import MonitorGroupSearchResponseCounts
        from datadog_api_client.v1.model.monitor_group_search_result import MonitorGroupSearchResult
        from datadog_api_client.v1.model.monitor_search_response_metadata import MonitorSearchResponseMetadata

        return {
            "counts": (MonitorGroupSearchResponseCounts,),
            "groups": ([MonitorGroupSearchResult],),
            "metadata": (MonitorSearchResponseMetadata,),
        }

    attribute_map = {
        "counts": "counts",
        "groups": "groups",
        "metadata": "metadata",
    }
    read_only_vars = {
        "counts",
        "groups",
    }

    def __init__(self, *args, **kwargs):
        """
        The response of a monitor group search.

        :param counts: The counts of monitor groups per different criteria.
        :type counts: MonitorGroupSearchResponseCounts, optional

        :param groups: The list of found monitor groups.
        :type groups: [MonitorGroupSearchResult], optional

        :param metadata: Metadata about the response.
        :type metadata: MonitorSearchResponseMetadata, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorGroupSearchResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
