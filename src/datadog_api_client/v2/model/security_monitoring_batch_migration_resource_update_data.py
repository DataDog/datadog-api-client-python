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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_update_attributes import (
        SecurityMonitoringBatchMigrationResourceUpdateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_type import (
        SecurityMonitoringBatchMigrationResourceType,
    )


class SecurityMonitoringBatchMigrationResourceUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_update_attributes import (
            SecurityMonitoringBatchMigrationResourceUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_type import (
            SecurityMonitoringBatchMigrationResourceType,
        )

        return {
            "attributes": (SecurityMonitoringBatchMigrationResourceUpdateAttributes,),
            "type": (SecurityMonitoringBatchMigrationResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringBatchMigrationResourceUpdateAttributes,
        type: SecurityMonitoringBatchMigrationResourceType,
        **kwargs,
    ):
        """
        Data of the batch migration resource to update.

        :param attributes: Attributes of the batch migration resource to update. At least one attribute is required.
        :type attributes: SecurityMonitoringBatchMigrationResourceUpdateAttributes

        :param type: The type of resource for a batch migration resource.
        :type type: SecurityMonitoringBatchMigrationResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
