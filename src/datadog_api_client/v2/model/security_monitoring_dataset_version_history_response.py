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
    from datadog_api_client.v2.model.security_monitoring_dataset_version_history_data import (
        SecurityMonitoringDatasetVersionHistoryData,
    )


class SecurityMonitoringDatasetVersionHistoryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_version_history_data import (
            SecurityMonitoringDatasetVersionHistoryData,
        )

        return {
            "data": (SecurityMonitoringDatasetVersionHistoryData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringDatasetVersionHistoryData, **kwargs):
        """
        Response containing the version history of a Cloud SIEM dataset.

        :param data: The data wrapper of a dataset version history response.
        :type data: SecurityMonitoringDatasetVersionHistoryData
        """
        super().__init__(kwargs)

        self_.data = data
