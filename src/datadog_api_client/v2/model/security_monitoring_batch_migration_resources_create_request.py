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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_create_data import (
        SecurityMonitoringBatchMigrationResourcesCreateData,
    )


class SecurityMonitoringBatchMigrationResourcesCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_create_data import (
            SecurityMonitoringBatchMigrationResourcesCreateData,
        )

        return {
            "data": (SecurityMonitoringBatchMigrationResourcesCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringBatchMigrationResourcesCreateData, **kwargs):
        """
        Request to add resources to a batch migration.

        :param data: Data of the resources to add to a batch migration.
        :type data: SecurityMonitoringBatchMigrationResourcesCreateData
        """
        super().__init__(kwargs)

        self_.data = data
