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


class UpdateTenancyConfigDataAttributesLogsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "compartment_tag_filters": ([str],),
            "enabled": (bool,),
            "enabled_services": ([str],),
        }

    attribute_map = {
        "compartment_tag_filters": "compartment_tag_filters",
        "enabled": "enabled",
        "enabled_services": "enabled_services",
    }

    def __init__(
        self_,
        compartment_tag_filters: Union[List[str], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        enabled_services: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param compartment_tag_filters:
        :type compartment_tag_filters: [str], optional

        :param enabled:
        :type enabled: bool, optional

        :param enabled_services:
        :type enabled_services: [str], optional
        """
        if compartment_tag_filters is not unset:
            kwargs["compartment_tag_filters"] = compartment_tag_filters
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if enabled_services is not unset:
            kwargs["enabled_services"] = enabled_services
        super().__init__(kwargs)
