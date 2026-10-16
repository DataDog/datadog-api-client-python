# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_create_item import (
        SecurityMonitoringBatchMigrationResourceCreateItem,
    )


class SecurityMonitoringBatchMigrationCreateAttributes(ModelNormal):
    validations = {
        "description": {
            "max_length": 4096,
        },
        "name": {
            "max_length": 512,
        },
        "resources": {
            "max_items": 100,
            "min_items": 1,
        },
        "tags": {
            "max_items": 50,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_create_item import (
            SecurityMonitoringBatchMigrationResourceCreateItem,
        )

        return {
            "description": (str,),
            "name": (str,),
            "resources": ([SecurityMonitoringBatchMigrationResourceCreateItem],),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "resources": "resources",
        "tags": "tags",
    }

    def __init__(
        self_,
        resources: List[SecurityMonitoringBatchMigrationResourceCreateItem],
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the batch migration to create.

        :param description: The description of the batch migration.
        :type description: str, optional

        :param name: The name of the batch migration.
        :type name: str, optional

        :param resources: The initial resources of the batch migration. From 1 to 100 resources.
        :type resources: [SecurityMonitoringBatchMigrationResourceCreateItem]

        :param tags: Tags of the batch migration. Up to 50 tags, each up to 256 characters.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.resources = resources
