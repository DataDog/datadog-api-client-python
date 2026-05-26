# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_dataset_version_history_entries import (
        SecurityMonitoringDatasetVersionHistoryEntries,
    )


class SecurityMonitoringDatasetVersionHistoryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_version_history_entries import (
            SecurityMonitoringDatasetVersionHistoryEntries,
        )

        return {
            "count": (int,),
            "data": (SecurityMonitoringDatasetVersionHistoryEntries,),
        }

    attribute_map = {
        "count": "count",
        "data": "data",
    }

    def __init__(self_, count: int, data: SecurityMonitoringDatasetVersionHistoryEntries, **kwargs):
        """
        The attributes of a dataset version history response.

        :param count: The total number of versions available for this dataset.
        :type count: int

        :param data: A map from version number (as a string) to the dataset state at that version.
        :type data: SecurityMonitoringDatasetVersionHistoryEntries
        """
        super().__init__(kwargs)

        self_.count = count
        self_.data = data
