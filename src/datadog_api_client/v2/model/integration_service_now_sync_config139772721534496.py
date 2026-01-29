# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sync_property import SyncProperty
    from datadog_api_client.v2.model.integration_service_now_sync_config_priority import (
        IntegrationServiceNowSyncConfigPriority,
    )
    from datadog_api_client.v2.model.sync_property_with_mapping import SyncPropertyWithMapping


class IntegrationServiceNowSyncConfig139772721534496(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sync_property import SyncProperty
        from datadog_api_client.v2.model.integration_service_now_sync_config_priority import (
            IntegrationServiceNowSyncConfigPriority,
        )
        from datadog_api_client.v2.model.sync_property_with_mapping import SyncPropertyWithMapping

        return {
            "comments": (SyncProperty,),
            "priority": (IntegrationServiceNowSyncConfigPriority,),
            "status": (SyncPropertyWithMapping,),
        }

    attribute_map = {
        "comments": "comments",
        "priority": "priority",
        "status": "status",
    }

    def __init__(
        self_,
        comments: Union[SyncProperty, UnsetType] = unset,
        priority: Union[IntegrationServiceNowSyncConfigPriority, UnsetType] = unset,
        status: Union[SyncPropertyWithMapping, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param comments: Sync property configuration
        :type comments: SyncProperty, optional

        :param priority:
        :type priority: IntegrationServiceNowSyncConfigPriority, optional

        :param status: Sync property with mapping configuration
        :type status: SyncPropertyWithMapping, optional
        """
        if comments is not unset:
            kwargs["comments"] = comments
        if priority is not unset:
            kwargs["priority"] = priority
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
