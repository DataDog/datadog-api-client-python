# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AgentHealthIssuesResponsePage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_count": (int,),
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "total_count": "total_count",
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(self_, total_count: int, total_filtered_count: int, **kwargs):
        """
        Pagination counts for the Agent Health issues.

        :param total_count: The total number of open issues in the organization, ignoring filters.
        :type total_count: int

        :param total_filtered_count: The total number of open issues matching the filters, across all pages.
        :type total_filtered_count: int
        """
        super().__init__(kwargs)

        self_.total_count = total_count
        self_.total_filtered_count = total_filtered_count
