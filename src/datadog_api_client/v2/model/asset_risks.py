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


class AssetRisks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "has_access_to_sensitive_data": (bool,),
            "has_privileged_access": (bool,),
            "in_production": (bool,),
            "is_publicly_accessible": (bool,),
            "under_attack": (bool,),
        }

    attribute_map = {
        "has_access_to_sensitive_data": "has_access_to_sensitive_data",
        "has_privileged_access": "has_privileged_access",
        "in_production": "in_production",
        "is_publicly_accessible": "is_publicly_accessible",
        "under_attack": "under_attack",
    }

    def __init__(
        self_,
        in_production: bool,
        has_access_to_sensitive_data: Union[bool, UnsetType] = unset,
        has_privileged_access: Union[bool, UnsetType] = unset,
        is_publicly_accessible: Union[bool, UnsetType] = unset,
        under_attack: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Asset risks.

        :param has_access_to_sensitive_data: Whether the asset has access to sensitive data or not.
        :type has_access_to_sensitive_data: bool, optional

        :param has_privileged_access: Whether the asset has privileged access or not.
        :type has_privileged_access: bool, optional

        :param in_production: Whether the asset is in production or not.
        :type in_production: bool

        :param is_publicly_accessible: Whether the asset is publicly accessible or not.
        :type is_publicly_accessible: bool, optional

        :param under_attack: Whether the asset is under attack or not.
        :type under_attack: bool, optional
        """
        if has_access_to_sensitive_data is not unset:
            kwargs["has_access_to_sensitive_data"] = has_access_to_sensitive_data
        if has_privileged_access is not unset:
            kwargs["has_privileged_access"] = has_privileged_access
        if is_publicly_accessible is not unset:
            kwargs["is_publicly_accessible"] = is_publicly_accessible
        if under_attack is not unset:
            kwargs["under_attack"] = under_attack
        super().__init__(kwargs)

        self_.in_production = in_production
