# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_version_diff_patches import SyntheticsTestVersionDiffPatches


class SyntheticsTestVersionActionMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_version_diff_patches import SyntheticsTestVersionDiffPatches

        return {
            "after_value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "before_value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "diff_patches": ([SyntheticsTestVersionDiffPatches], none_type),
            "property_path": (str,),
        }

    attribute_map = {
        "after_value": "after_value",
        "before_value": "before_value",
        "diff_patches": "diff_patches",
        "property_path": "property_path",
    }

    def __init__(
        self_,
        after_value: Union[Any, UnsetType] = unset,
        before_value: Union[Any, UnsetType] = unset,
        diff_patches: Union[List[SyntheticsTestVersionDiffPatches], none_type, UnsetType] = unset,
        property_path: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing metadata about a change action.

        :param after_value: The value of the property after the change.
        :type after_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param before_value: The value of the property before the change.
        :type before_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param diff_patches: List of diff patches for text changes.
        :type diff_patches: [SyntheticsTestVersionDiffPatches], none_type, optional

        :param property_path: The dot-separated path of the property that was changed.
        :type property_path: str, optional
        """
        if after_value is not unset:
            kwargs["after_value"] = after_value
        if before_value is not unset:
            kwargs["before_value"] = before_value
        if diff_patches is not unset:
            kwargs["diff_patches"] = diff_patches
        if property_path is not unset:
            kwargs["property_path"] = property_path
        super().__init__(kwargs)
