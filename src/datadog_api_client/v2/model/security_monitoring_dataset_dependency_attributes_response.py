# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringDatasetDependencyAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "ids": ([str],),
            "resource_type": (str,),
        }

    attribute_map = {
        "count": "count",
        "ids": "ids",
        "resource_type": "resource_type",
    }

    def __init__(self_, count: int, ids: List[str], resource_type: str, **kwargs):
        """
        Attributes for dataset dependency.

        :param count: The count of resources that depend on the dataset.
        :type count: int

        :param ids: Array of IDs of resources that depend on the dataset.
        :type ids: [str]

        :param resource_type: The type of resource that depends on the dataset.
        :type resource_type: str
        """
        super().__init__(kwargs)

        self_.count = count
        self_.ids = ids
        self_.resource_type = resource_type
