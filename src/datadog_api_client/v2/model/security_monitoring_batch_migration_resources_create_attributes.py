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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_create_item import (
        SecurityMonitoringBatchMigrationResourceCreateItem,
    )


class SecurityMonitoringBatchMigrationResourcesCreateAttributes(ModelNormal):
    validations = {
        "resources": {
            "max_items": 1000,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_create_item import (
            SecurityMonitoringBatchMigrationResourceCreateItem,
        )

        return {
            "resources": ([SecurityMonitoringBatchMigrationResourceCreateItem],),
        }

    attribute_map = {
        "resources": "resources",
    }

    def __init__(self_, resources: List[SecurityMonitoringBatchMigrationResourceCreateItem], **kwargs):
        """
        Attributes of the resources to add to a batch migration.

        :param resources: The resources to add. From 1 to 1000 resources.
        :type resources: [SecurityMonitoringBatchMigrationResourceCreateItem]
        """
        super().__init__(kwargs)

        self_.resources = resources
