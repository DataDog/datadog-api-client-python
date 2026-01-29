# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringDatasetDependenciesAttributesRequest(ModelNormal):
    validations = {
        "dataset_ids": {
            "max_items": 100,
            "min_items": 1,
        },
    }

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
        Attributes for dataset dependencies request.

        :param dataset_ids: Array of dataset IDs to check dependencies for (minimum 1, maximum 100).
        :type dataset_ids: [str]
        """
        super().__init__(kwargs)

        self_.dataset_ids = dataset_ids
