# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringDatasetDependentsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "dataset_id": (str,),
            "ids": ([str],),
            "resource_type": (str,),
        }

    attribute_map = {
        "count": "count",
        "dataset_id": "datasetId",
        "ids": "ids",
        "resource_type": "resource_type",
    }

    def __init__(self_, count: int, dataset_id: str, ids: List[str], resource_type: str, **kwargs):
        """
        The attributes of a dataset dependents entry.

        :param count: The number of resources that depend on the dataset.
        :type count: int

        :param dataset_id: The UUID of the dataset whose dependencies are being reported.
        :type dataset_id: str

        :param ids: The list of resource IDs that depend on the dataset.
        :type ids: [str]

        :param resource_type: The type of resource that depends on the dataset.
        :type resource_type: str
        """
        super().__init__(kwargs)

        self_.count = count
        self_.dataset_id = dataset_id
        self_.ids = ids
        self_.resource_type = resource_type
