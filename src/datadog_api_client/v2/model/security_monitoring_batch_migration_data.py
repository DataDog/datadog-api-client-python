# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_batch_migration_attributes import (
        SecurityMonitoringBatchMigrationAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_type import (
        SecurityMonitoringBatchMigrationType,
    )


class SecurityMonitoringBatchMigrationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_attributes import (
            SecurityMonitoringBatchMigrationAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_type import (
            SecurityMonitoringBatchMigrationType,
        )

        return {
            "attributes": (SecurityMonitoringBatchMigrationAttributes,),
            "id": (UUID,),
            "type": (SecurityMonitoringBatchMigrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringBatchMigrationAttributes,
        id: UUID,
        type: SecurityMonitoringBatchMigrationType,
        **kwargs,
    ):
        """
        A batch migration.

        :param attributes: Attributes of a batch migration.
        :type attributes: SecurityMonitoringBatchMigrationAttributes

        :param id: The UUID of the batch migration.
        :type id: UUID

        :param type: The type of resource for a batch migration.
        :type type: SecurityMonitoringBatchMigrationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
