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
    from datadog_api_client.v1.model.heatgrid_text_format_match import HeatgridTextFormatMatch
    from datadog_api_client.v1.model.heatgrid_text_format_replace import HeatgridTextFormatReplace
    from datadog_api_client.v1.model.heatgrid_text_format_replace_all import HeatgridTextFormatReplaceAll
    from datadog_api_client.v1.model.heatgrid_text_format_replace_substring import HeatgridTextFormatReplaceSubstring


class HeatgridTextFormatRule(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_text_format_match import HeatgridTextFormatMatch
        from datadog_api_client.v1.model.heatgrid_text_format_replace import HeatgridTextFormatReplace

        return {
            "match": (HeatgridTextFormatMatch,),
            "replace": (HeatgridTextFormatReplace,),
        }

    attribute_map = {
        "match": "match",
        "replace": "replace",
    }

    def __init__(
        self_,
        match: HeatgridTextFormatMatch,
        replace: Union[
            HeatgridTextFormatReplace, HeatgridTextFormatReplaceAll, HeatgridTextFormatReplaceSubstring, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        A rule for matching and optionally replacing a group label.

        :param match: Match a group label against a string.
        :type match: HeatgridTextFormatMatch

        :param replace: Replace all or part of a matching group label.
        :type replace: HeatgridTextFormatReplace, optional
        """
        if replace is not unset:
            kwargs["replace"] = replace
        super().__init__(kwargs)

        self_.match = match
