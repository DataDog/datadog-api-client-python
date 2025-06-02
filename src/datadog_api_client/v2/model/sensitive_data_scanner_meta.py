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


class SensitiveDataScannerMeta(ModelNormal):
    validations = {
        "min_sampling_rate": {
            "inclusive_maximum": 100.0,
            "inclusive_minimum": 0.0,
        },
        "version": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "count_limit": (int,),
            "group_count_limit": (int,),
            "has_highlight_enabled": (bool,),
            "has_multi_pass_enabled": (bool,),
            "is_float_sampling_rate_enabled": (bool,),
            "is_pci_compliant": (bool,),
            "min_sampling_rate": (float,),
            "version": (int,),
        }

    attribute_map = {
        "count_limit": "count_limit",
        "group_count_limit": "group_count_limit",
        "has_highlight_enabled": "has_highlight_enabled",
        "has_multi_pass_enabled": "has_multi_pass_enabled",
        "is_float_sampling_rate_enabled": "is_float_sampling_rate_enabled",
        "is_pci_compliant": "is_pci_compliant",
        "min_sampling_rate": "min_sampling_rate",
        "version": "version",
    }

    def __init__(
        self_,
        count_limit: Union[int, UnsetType] = unset,
        group_count_limit: Union[int, UnsetType] = unset,
        has_highlight_enabled: Union[bool, UnsetType] = unset,
        has_multi_pass_enabled: Union[bool, UnsetType] = unset,
        is_float_sampling_rate_enabled: Union[bool, UnsetType] = unset,
        is_pci_compliant: Union[bool, UnsetType] = unset,
        min_sampling_rate: Union[float, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Meta response containing information about the API.

        :param count_limit: Maximum number of scanning rules allowed for the org.
        :type count_limit: int, optional

        :param group_count_limit: Maximum number of scanning groups allowed for the org.
        :type group_count_limit: int, optional

        :param has_highlight_enabled: (Deprecated) Whether or not scanned events are highlighted in Logs or RUM for the org. **Deprecated**.
        :type has_highlight_enabled: bool, optional

        :param has_multi_pass_enabled: (Deprecated) Whether or not scanned events have multi-pass enabled. **Deprecated**.
        :type has_multi_pass_enabled: bool, optional

        :param is_float_sampling_rate_enabled: Whether or not the sampling rate for products can be set to a float point number (as opposed to an integer).
        :type is_float_sampling_rate_enabled: bool, optional

        :param is_pci_compliant: Whether or not the org is compliant to the payment card industry standard.
        :type is_pci_compliant: bool, optional

        :param min_sampling_rate: Global minimum sampling rate allowed for all product within the org.
        :type min_sampling_rate: float, optional

        :param version: Version of the API.
        :type version: int, optional
        """
        if count_limit is not unset:
            kwargs["count_limit"] = count_limit
        if group_count_limit is not unset:
            kwargs["group_count_limit"] = group_count_limit
        if has_highlight_enabled is not unset:
            kwargs["has_highlight_enabled"] = has_highlight_enabled
        if has_multi_pass_enabled is not unset:
            kwargs["has_multi_pass_enabled"] = has_multi_pass_enabled
        if is_float_sampling_rate_enabled is not unset:
            kwargs["is_float_sampling_rate_enabled"] = is_float_sampling_rate_enabled
        if is_pci_compliant is not unset:
            kwargs["is_pci_compliant"] = is_pci_compliant
        if min_sampling_rate is not unset:
            kwargs["min_sampling_rate"] = min_sampling_rate
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
