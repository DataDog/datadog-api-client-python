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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_delete_attributes import (
        SecurityMonitoringBatchMigrationResourcesDeleteAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_type import (
        SecurityMonitoringBatchMigrationResourcesType,
    )


class SecurityMonitoringBatchMigrationResourcesDeleteData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_delete_attributes import (
            SecurityMonitoringBatchMigrationResourcesDeleteAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resources_type import (
            SecurityMonitoringBatchMigrationResourcesType,
        )

        return {
            "attributes": (SecurityMonitoringBatchMigrationResourcesDeleteAttributes,),
            "type": (SecurityMonitoringBatchMigrationResourcesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringBatchMigrationResourcesDeleteAttributes,
        type: SecurityMonitoringBatchMigrationResourcesType,
        **kwargs,
    ):
        """
        Data of the resources to delete from a batch migration.

        :param attributes: Attributes of the resources to delete from a batch migration.
        :type attributes: SecurityMonitoringBatchMigrationResourcesDeleteAttributes

        :param type: The type of resource for a request on a set of batch migration resources.
        :type type: SecurityMonitoringBatchMigrationResourcesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
