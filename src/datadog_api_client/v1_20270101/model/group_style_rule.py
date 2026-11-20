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
    from datadog_api_client.v1_20270101.model.group_style_rule_match import GroupStyleRuleMatch


class GroupStyleRule(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.group_style_rule_match import GroupStyleRuleMatch

        return {
            "match": (GroupStyleRuleMatch,),
            "palette": (str,),
            "palette_index": (float,),
        }

    attribute_map = {
        "match": "match",
        "palette": "palette",
        "palette_index": "palette_index",
    }

    def __init__(
        self_,
        palette: str,
        match: Union[GroupStyleRuleMatch, UnsetType] = unset,
        palette_index: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param match: Test-only generated schema for the dashboard versioning proof of concept.
        :type match: GroupStyleRuleMatch, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str

        :param palette_index: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette_index: float, optional
        """
        if match is not unset:
            kwargs["match"] = match
        if palette_index is not unset:
            kwargs["palette_index"] = palette_index
        super().__init__(kwargs)

        self_.palette = palette
