# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IntegrationMonitor(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "auto_resolve_enabled": (bool,),
            "case_type_id": (str,),
            "enabled": (bool,),
            "handle": (str,),
        }

    attribute_map = {
        "auto_resolve_enabled": "auto_resolve_enabled",
        "case_type_id": "case_type_id",
        "enabled": "enabled",
        "handle": "handle",
    }

    def __init__(
        self_,
        auto_resolve_enabled: Union[bool, UnsetType] = unset,
        case_type_id: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Monitor integration settings

        :param auto_resolve_enabled: Whether auto-resolve is enabled
        :type auto_resolve_enabled: bool, optional

        :param case_type_id: Case type ID for monitor integration
        :type case_type_id: str, optional

        :param enabled: Whether monitor integration is enabled
        :type enabled: bool, optional

        :param handle: Monitor handle
        :type handle: str, optional
        """
        if auto_resolve_enabled is not unset:
            kwargs["auto_resolve_enabled"] = auto_resolve_enabled
        if case_type_id is not unset:
            kwargs["case_type_id"] = case_type_id
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if handle is not unset:
            kwargs["handle"] = handle
        super().__init__(kwargs)
