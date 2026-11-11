# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class NebiusCloudLogsIntegrationDataflowSettingsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "enabled_services": ([str],),
        }

    attribute_map = {
        "enabled_services": "enabled_services",
    }

    def __init__(self_, enabled_services: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Settings of the logs dataflow. Only the fields provided are changed.

        :param enabled_services: Nebius log integrations to collect. One of ``nebius-cloud-compute`` , ``nebius-cloud-kubernetes`` , ``nebius-cloud-mlflow`` , ``nebius-cloud-postgresql`` , ``nebius-cloud-applications`` , or ``default`` for the streams shared by every service. A non-empty list is the sole source of truth and replaces the stored list: those services are collected and any others stop. An empty list stops log collection entirely. Omit it to keep the stored list.
        :type enabled_services: [str], optional
        """
        if enabled_services is not unset:
            kwargs["enabled_services"] = enabled_services
        super().__init__(kwargs)
