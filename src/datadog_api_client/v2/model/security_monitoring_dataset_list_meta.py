# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringDatasetListMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_count": (int,),
        }

    attribute_map = {
        "total_count": "totalCount",
    }

    def __init__(self_, total_count: int, **kwargs):
        """
        Metadata for dataset list responses.

        :param total_count: The total count of datasets.
        :type total_count: int
        """
        super().__init__(kwargs)

        self_.total_count = total_count
