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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_attributes import (
        SecurityMonitoringBatchMigrationPublishAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_type import (
        SecurityMonitoringBatchMigrationPublishType,
    )


class SecurityMonitoringBatchMigrationPublishData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_attributes import (
            SecurityMonitoringBatchMigrationPublishAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_type import (
            SecurityMonitoringBatchMigrationPublishType,
        )

        return {
            "attributes": (SecurityMonitoringBatchMigrationPublishAttributes,),
            "type": (SecurityMonitoringBatchMigrationPublishType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringBatchMigrationPublishAttributes,
        type: SecurityMonitoringBatchMigrationPublishType,
        **kwargs,
    ):
        """
        Data of the batch migration publish request.

        :param attributes: Attributes of the batch migration publish request.
        :type attributes: SecurityMonitoringBatchMigrationPublishAttributes

        :param type: The type of resource for a batch migration publish request.
        :type type: SecurityMonitoringBatchMigrationPublishType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
