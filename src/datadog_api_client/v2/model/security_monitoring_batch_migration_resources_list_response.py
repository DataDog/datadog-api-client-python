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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_data import (
        SecurityMonitoringBatchMigrationResourceData,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_list_meta import (
        SecurityMonitoringBatchMigrationListMeta,
    )


class SecurityMonitoringBatchMigrationResourcesListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_data import (
            SecurityMonitoringBatchMigrationResourceData,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_list_meta import (
            SecurityMonitoringBatchMigrationListMeta,
        )

        return {
            "data": ([SecurityMonitoringBatchMigrationResourceData],),
            "meta": (SecurityMonitoringBatchMigrationListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[SecurityMonitoringBatchMigrationResourceData],
        meta: SecurityMonitoringBatchMigrationListMeta,
        **kwargs,
    ):
        """
        Response containing batch migration resources.

        :param data: The batch migration resources.
        :type data: [SecurityMonitoringBatchMigrationResourceData]

        :param meta: Metadata of a list response.
        :type meta: SecurityMonitoringBatchMigrationListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
