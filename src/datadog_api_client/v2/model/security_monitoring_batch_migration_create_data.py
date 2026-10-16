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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_create_attributes import (
        SecurityMonitoringBatchMigrationCreateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_type import (
        SecurityMonitoringBatchMigrationType,
    )


class SecurityMonitoringBatchMigrationCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_create_attributes import (
            SecurityMonitoringBatchMigrationCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_type import (
            SecurityMonitoringBatchMigrationType,
        )

        return {
            "attributes": (SecurityMonitoringBatchMigrationCreateAttributes,),
            "type": (SecurityMonitoringBatchMigrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringBatchMigrationCreateAttributes,
        type: SecurityMonitoringBatchMigrationType,
        **kwargs,
    ):
        """
        Data of the batch migration to create.

        :param attributes: Attributes of the batch migration to create.
        :type attributes: SecurityMonitoringBatchMigrationCreateAttributes

        :param type: The type of resource for a batch migration.
        :type type: SecurityMonitoringBatchMigrationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
