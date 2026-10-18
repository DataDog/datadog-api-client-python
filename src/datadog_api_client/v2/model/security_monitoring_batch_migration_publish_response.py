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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_data import (
        SecurityMonitoringBatchMigrationPublishedResourceData,
    )


class SecurityMonitoringBatchMigrationPublishResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_data import (
            SecurityMonitoringBatchMigrationPublishedResourceData,
        )

        return {
            "data": ([SecurityMonitoringBatchMigrationPublishedResourceData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SecurityMonitoringBatchMigrationPublishedResourceData], **kwargs):
        """
        Response containing the publication outcome of each resource.

        :param data: The publication outcome of each resource.
        :type data: [SecurityMonitoringBatchMigrationPublishedResourceData]
        """
        super().__init__(kwargs)

        self_.data = data
