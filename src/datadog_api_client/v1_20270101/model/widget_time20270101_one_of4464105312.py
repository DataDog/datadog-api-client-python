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
    from datadog_api_client.v1_20270101.model.legacy_live_span import LegacyLiveSpan


class WidgetTime20270101OneOf4464105312(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.legacy_live_span import LegacyLiveSpan

        return {
            "hide_incomplete_cost_data": (bool,),
            "live_span": (LegacyLiveSpan,),
        }

    attribute_map = {
        "hide_incomplete_cost_data": "hide_incomplete_cost_data",
        "live_span": "live_span",
    }

    def __init__(
        self_,
        live_span: Union[LegacyLiveSpan, str],
        hide_incomplete_cost_data: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param hide_incomplete_cost_data: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_incomplete_cost_data: bool, optional

        :param live_span: Test-only generated schema for the dashboard versioning proof of concept.
        :type live_span: LegacyLiveSpan
        """
        if hide_incomplete_cost_data is not unset:
            kwargs["hide_incomplete_cost_data"] = hide_incomplete_cost_data
        super().__init__(kwargs)

        self_.live_span = live_span
