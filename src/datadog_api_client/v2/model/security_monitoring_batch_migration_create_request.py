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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_create_data import (
        SecurityMonitoringBatchMigrationCreateData,
    )


class SecurityMonitoringBatchMigrationCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_create_data import (
            SecurityMonitoringBatchMigrationCreateData,
        )

        return {
            "data": (SecurityMonitoringBatchMigrationCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringBatchMigrationCreateData, **kwargs):
        """
        Request to create a batch migration.

        :param data: Data of the batch migration to create.
        :type data: SecurityMonitoringBatchMigrationCreateData
        """
        super().__init__(kwargs)

        self_.data = data
