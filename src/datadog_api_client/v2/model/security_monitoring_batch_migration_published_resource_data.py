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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_attributes import (
        SecurityMonitoringBatchMigrationPublishedResourceAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_type import (
        SecurityMonitoringBatchMigrationPublishedResourceType,
    )


class SecurityMonitoringBatchMigrationPublishedResourceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_attributes import (
            SecurityMonitoringBatchMigrationPublishedResourceAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_type import (
            SecurityMonitoringBatchMigrationPublishedResourceType,
        )

        return {
            "attributes": (SecurityMonitoringBatchMigrationPublishedResourceAttributes,),
            "id": (UUID,),
            "type": (SecurityMonitoringBatchMigrationPublishedResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringBatchMigrationPublishedResourceAttributes,
        id: UUID,
        type: SecurityMonitoringBatchMigrationPublishedResourceType,
        **kwargs,
    ):
        """
        The publication outcome of a batch migration resource.

        :param attributes: Attributes of the publication outcome of a batch migration resource.
        :type attributes: SecurityMonitoringBatchMigrationPublishedResourceAttributes

        :param id: The UUID of the batch migration resource.
        :type id: UUID

        :param type: The type of resource for a published batch migration resource.
        :type type: SecurityMonitoringBatchMigrationPublishedResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
