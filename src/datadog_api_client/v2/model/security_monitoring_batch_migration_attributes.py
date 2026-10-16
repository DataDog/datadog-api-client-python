# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_batch_migration_input_source import (
        SecurityMonitoringBatchMigrationInputSource,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_status_counts import (
        SecurityMonitoringBatchMigrationResourceStatusCounts,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_status import (
        SecurityMonitoringBatchMigrationStatus,
    )


class SecurityMonitoringBatchMigrationAttributes(ModelNormal):
    validations = {
        "tags": {
            "max_items": 50,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_input_source import (
            SecurityMonitoringBatchMigrationInputSource,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_status_counts import (
            SecurityMonitoringBatchMigrationResourceStatusCounts,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_status import (
            SecurityMonitoringBatchMigrationStatus,
        )

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "description": (str,),
            "input_source": (SecurityMonitoringBatchMigrationInputSource,),
            "last_updated_at": (datetime,),
            "last_updated_by": (str,),
            "name": (str,),
            "org_id": (int,),
            "resource_status_counts": (SecurityMonitoringBatchMigrationResourceStatusCounts,),
            "status": (SecurityMonitoringBatchMigrationStatus,),
            "tags": ([str],),
        }

    attribute_map = {
        "created_at": "createdAt",
        "created_by": "createdBy",
        "description": "description",
        "input_source": "inputSource",
        "last_updated_at": "lastUpdatedAt",
        "last_updated_by": "lastUpdatedBy",
        "name": "name",
        "org_id": "orgId",
        "resource_status_counts": "resourceStatusCounts",
        "status": "status",
        "tags": "tags",
    }

    def __init__(
        self_,
        created_at: datetime,
        input_source: SecurityMonitoringBatchMigrationInputSource,
        last_updated_at: datetime,
        name: str,
        org_id: int,
        resource_status_counts: SecurityMonitoringBatchMigrationResourceStatusCounts,
        status: SecurityMonitoringBatchMigrationStatus,
        tags: List[str],
        created_by: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        last_updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a batch migration.

        :param created_at: The creation date of the batch migration, in RFC 3339 format.
        :type created_at: datetime

        :param created_by: The UUID of the user or service account who created the batch migration.
        :type created_by: str, optional

        :param description: The description of the batch migration.
        :type description: str, optional

        :param input_source: The origin of a batch migration. Always ``batch_migration`` for batch migrations
            created through this API.
        :type input_source: SecurityMonitoringBatchMigrationInputSource

        :param last_updated_at: The last update date of the batch migration, in RFC 3339 format.
        :type last_updated_at: datetime

        :param last_updated_by: The UUID of the user or service account who last updated the batch migration,
            or the name of a system actor.
        :type last_updated_by: str, optional

        :param name: The name of the batch migration.
        :type name: str

        :param org_id: The ID of the organization that owns the batch migration.
        :type org_id: int

        :param resource_status_counts: The number of resources of a batch migration in each status.
        :type resource_status_counts: SecurityMonitoringBatchMigrationResourceStatusCounts

        :param status: The status of a batch migration. A batch migration is created as ``draft`` and moves to
            ``in_progress`` when started. It moves to ``completed`` once no resource is ``pending`` or
            ``in_progress`` , or to ``canceled`` when canceled.
        :type status: SecurityMonitoringBatchMigrationStatus

        :param tags: Tags of the batch migration. Up to 50 tags, each up to 256 characters.
        :type tags: [str]
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if last_updated_by is not unset:
            kwargs["last_updated_by"] = last_updated_by
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.input_source = input_source
        self_.last_updated_at = last_updated_at
        self_.name = name
        self_.org_id = org_id
        self_.resource_status_counts = resource_status_counts
        self_.status = status
        self_.tags = tags
