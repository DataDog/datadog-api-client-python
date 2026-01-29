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
    from datadog_api_client.v2.model.integration_service_now_auto_creation import IntegrationServiceNowAutoCreation
    from datadog_api_client.v2.model.integration_service_now_sync_config import IntegrationServiceNowSyncConfig


class IntegrationServiceNow(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_service_now_auto_creation import IntegrationServiceNowAutoCreation
        from datadog_api_client.v2.model.integration_service_now_sync_config import IntegrationServiceNowSyncConfig

        return {
            "assignment_group": (str,),
            "auto_creation": (IntegrationServiceNowAutoCreation,),
            "enabled": (bool,),
            "instance_name": (str,),
            "sync_config": (IntegrationServiceNowSyncConfig,),
        }

    attribute_map = {
        "assignment_group": "assignment_group",
        "auto_creation": "auto_creation",
        "enabled": "enabled",
        "instance_name": "instance_name",
        "sync_config": "sync_config",
    }

    def __init__(
        self_,
        assignment_group: Union[str, UnsetType] = unset,
        auto_creation: Union[IntegrationServiceNowAutoCreation, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        instance_name: Union[str, UnsetType] = unset,
        sync_config: Union[IntegrationServiceNowSyncConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        ServiceNow integration settings

        :param assignment_group: Assignment group
        :type assignment_group: str, optional

        :param auto_creation:
        :type auto_creation: IntegrationServiceNowAutoCreation, optional

        :param enabled: Whether ServiceNow integration is enabled
        :type enabled: bool, optional

        :param instance_name: ServiceNow instance name
        :type instance_name: str, optional

        :param sync_config:
        :type sync_config: IntegrationServiceNowSyncConfig, optional
        """
        if assignment_group is not unset:
            kwargs["assignment_group"] = assignment_group
        if auto_creation is not unset:
            kwargs["auto_creation"] = auto_creation
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if instance_name is not unset:
            kwargs["instance_name"] = instance_name
        if sync_config is not unset:
            kwargs["sync_config"] = sync_config
        super().__init__(kwargs)
