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
    from datadog_api_client.v2.model.integration_service_now_sync_config139772721534496 import (
        IntegrationServiceNowSyncConfig139772721534496,
    )


class IntegrationServiceNowSyncConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_service_now_sync_config139772721534496 import (
            IntegrationServiceNowSyncConfig139772721534496,
        )

        return {
            "enabled": (bool,),
            "properties": (IntegrationServiceNowSyncConfig139772721534496,),
        }

    attribute_map = {
        "enabled": "enabled",
        "properties": "properties",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        properties: Union[IntegrationServiceNowSyncConfig139772721534496, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param enabled:
        :type enabled: bool, optional

        :param properties:
        :type properties: IntegrationServiceNowSyncConfig139772721534496, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if properties is not unset:
            kwargs["properties"] = properties
        super().__init__(kwargs)
