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
    from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_settings_request import (
        NebiusCloudLogsIntegrationDataflowSettingsRequest,
    )


class NebiusCloudLogsIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_logs_integration_dataflow_settings_request import (
            NebiusCloudLogsIntegrationDataflowSettingsRequest,
        )

        return {
            "enabled": (bool,),
            "settings": (NebiusCloudLogsIntegrationDataflowSettingsRequest,),
        }

    attribute_map = {
        "enabled": "enabled",
        "settings": "settings",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        settings: Union[NebiusCloudLogsIntegrationDataflowSettingsRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Logs from your Nebius tenant: Kubernetes control plane and audit logs, tenant-level audit events, compute serial console logs, cloud apps and AI inference logs, PostgreSQL logs, and MLflow logs, collected from the services named in ``settings.enabled_services``. ``enabled_services`` is the sole source of truth for what is collected; ``enabled`` set to ``false`` stops log collection, while ``true`` on its own changes nothing. Defaults to no services.

        :param enabled: Whether Datadog collects logs. Defaults to ``false``. Set to ``false`` to stop log collection; sending ``true`` on its own changes nothing, because ``settings.enabled_services`` is the sole source of truth.
        :type enabled: bool, optional

        :param settings: Settings of the logs dataflow. Only the fields provided are changed.
        :type settings: NebiusCloudLogsIntegrationDataflowSettingsRequest, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
