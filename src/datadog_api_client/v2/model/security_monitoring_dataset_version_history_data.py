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
    from datadog_api_client.v2.model.security_monitoring_dataset_version_history_attributes import (
        SecurityMonitoringDatasetVersionHistoryAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_version_history_type import (
        SecurityMonitoringDatasetVersionHistoryType,
    )


class SecurityMonitoringDatasetVersionHistoryData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_version_history_attributes import (
            SecurityMonitoringDatasetVersionHistoryAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_version_history_type import (
            SecurityMonitoringDatasetVersionHistoryType,
        )

        return {
            "attributes": (SecurityMonitoringDatasetVersionHistoryAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringDatasetVersionHistoryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringDatasetVersionHistoryAttributes,
        id: str,
        type: SecurityMonitoringDatasetVersionHistoryType,
        **kwargs,
    ):
        """
        The data wrapper of a dataset version history response.

        :param attributes: The attributes of a dataset version history response.
        :type attributes: SecurityMonitoringDatasetVersionHistoryAttributes

        :param id: The UUID of the dataset.
        :type id: str

        :param type: The type of resource for a dataset version history response.
        :type type: SecurityMonitoringDatasetVersionHistoryType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
