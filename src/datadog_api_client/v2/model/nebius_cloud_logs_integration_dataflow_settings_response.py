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


class NebiusCloudLogsIntegrationDataflowSettingsResponse(ModelNormal):
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
        Settings of the logs dataflow.

        :param enabled_services: Nebius log integrations collected, such as ``nebius-cloud-compute`` and ``default``. Absent when no service is enabled.
        :type enabled_services: [str], optional
        """
        if enabled_services is not unset:
            kwargs["enabled_services"] = enabled_services
        super().__init__(kwargs)
