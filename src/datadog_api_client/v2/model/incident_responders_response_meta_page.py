# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentRespondersResponseMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(self_, total_filtered_count: int, **kwargs):
        """
        Total count for the responder list.

        :param total_filtered_count: Total number of responders matching the query, before pagination.
        :type total_filtered_count: int
        """
        super().__init__(kwargs)

        self_.total_filtered_count = total_filtered_count
