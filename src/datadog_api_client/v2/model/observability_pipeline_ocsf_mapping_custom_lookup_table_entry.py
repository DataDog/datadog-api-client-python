# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

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


class ObservabilityPipelineOcsfMappingCustomLookupTableEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "contains": (str,),
            "equals": (
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
            "equals_source": (str,),
            "matches": (str,),
            "not_matches": (str,),
            "value": (
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
        }

    attribute_map = {
        "contains": "contains",
        "equals": "equals",
        "equals_source": "equals_source",
        "matches": "matches",
        "not_matches": "not_matches",
        "value": "value",
    }

    def __init__(
        self_,
        contains: Union[str, UnsetType] = unset,
        equals: Union[Any, UnsetType] = unset,
        equals_source: Union[str, UnsetType] = unset,
        matches: Union[str, UnsetType] = unset,
        not_matches: Union[str, UnsetType] = unset,
        value: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single entry in a lookup table for value transformation.

        :param contains: The substring to match in the source value.
        :type contains: str, optional

        :param equals: The exact value to match in the source.
        :type equals: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param equals_source: The source field to match against.
        :type equals_source: str, optional

        :param matches: A regex pattern to match in the source value.
        :type matches: str, optional

        :param not_matches: A regex pattern that must not match the source value.
        :type not_matches: str, optional

        :param value: The value to use when a match is found.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if contains is not unset:
            kwargs["contains"] = contains
        if equals is not unset:
            kwargs["equals"] = equals
        if equals_source is not unset:
            kwargs["equals_source"] = equals_source
        if matches is not unset:
            kwargs["matches"] = matches
        if not_matches is not unset:
            kwargs["not_matches"] = not_matches
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
