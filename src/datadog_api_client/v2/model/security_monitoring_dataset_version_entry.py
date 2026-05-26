# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_dataset_version_field_change import (
        SecurityMonitoringDatasetVersionFieldChange,
    )
    from datadog_api_client.v2.model.security_monitoring_dataset_attributes_response import (
        SecurityMonitoringDatasetAttributesResponse,
    )


class SecurityMonitoringDatasetVersionEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_version_field_change import (
            SecurityMonitoringDatasetVersionFieldChange,
        )
        from datadog_api_client.v2.model.security_monitoring_dataset_attributes_response import (
            SecurityMonitoringDatasetAttributesResponse,
        )

        return {
            "changes": ([SecurityMonitoringDatasetVersionFieldChange],),
            "dataset": (SecurityMonitoringDatasetAttributesResponse,),
        }

    attribute_map = {
        "changes": "changes",
        "dataset": "dataset",
    }

    def __init__(
        self_,
        changes: List[SecurityMonitoringDatasetVersionFieldChange],
        dataset: SecurityMonitoringDatasetAttributesResponse,
        **kwargs,
    ):
        """
        A single entry in the version history of a dataset.

        :param changes: The list of field changes between this version of the dataset and the previous one.
        :type changes: [SecurityMonitoringDatasetVersionFieldChange]

        :param dataset: The attributes of a Cloud SIEM dataset.
        :type dataset: SecurityMonitoringDatasetAttributesResponse
        """
        super().__init__(kwargs)

        self_.changes = changes
        self_.dataset = dataset
