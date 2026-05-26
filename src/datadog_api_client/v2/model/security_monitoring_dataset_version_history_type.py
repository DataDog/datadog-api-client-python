# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringDatasetVersionHistoryType(ModelSimple):
    """
    The type of resource for a dataset version history response.

    :param value: If omitted defaults to "dataset_version_history". Must be one of ["dataset_version_history"].
    :type value: str
    """

    allowed_values = {
        "dataset_version_history",
    }
    DATASET_VERSION_HISTORY: ClassVar["SecurityMonitoringDatasetVersionHistoryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringDatasetVersionHistoryType.DATASET_VERSION_HISTORY = SecurityMonitoringDatasetVersionHistoryType(
    "dataset_version_history"
)
