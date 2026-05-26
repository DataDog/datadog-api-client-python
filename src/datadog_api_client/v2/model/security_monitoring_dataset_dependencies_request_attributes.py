# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringDatasetDependenciesRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dataset_ids": ([str],),
        }

    attribute_map = {
        "dataset_ids": "datasetIds",
    }

    def __init__(self_, dataset_ids: List[str], **kwargs):
        """
        The attributes of a dataset dependencies request.

        :param dataset_ids: The list of dataset UUIDs to query dependencies for. Must contain between 1 and 100 items.
        :type dataset_ids: [str]
        """
        super().__init__(kwargs)

        self_.dataset_ids = dataset_ids
