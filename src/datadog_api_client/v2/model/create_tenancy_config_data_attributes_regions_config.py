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


class CreateTenancyConfigDataAttributesRegionsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "available": ([str],),
            "disabled": ([str],),
            "enabled": ([str],),
        }

    attribute_map = {
        "available": "available",
        "disabled": "disabled",
        "enabled": "enabled",
    }

    def __init__(
        self_,
        available: Union[List[str], UnsetType] = unset,
        disabled: Union[List[str], UnsetType] = unset,
        enabled: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Region configuration for an OCI tenancy, specifying which regions are available, enabled, or disabled for data collection.

        :param available: List of OCI regions available for data collection in the tenancy.
        :type available: [str], optional

        :param disabled: List of OCI regions explicitly disabled for data collection.
        :type disabled: [str], optional

        :param enabled: List of OCI regions enabled for data collection.
        :type enabled: [str], optional
        """
        if available is not unset:
            kwargs["available"] = available
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)
