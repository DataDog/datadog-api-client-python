# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetTimeHideIncompleteData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "hide_incomplete_cost_data": (bool,),
        }

    attribute_map = {
        "hide_incomplete_cost_data": "hide_incomplete_cost_data",
    }

    def __init__(self_, hide_incomplete_cost_data: bool, **kwargs):
        """
        Widget time setting with hide incomplete cost data option.

        :param hide_incomplete_cost_data: Whether to hide incomplete cost data in the widget.
        :type hide_incomplete_cost_data: bool
        """
        super().__init__(kwargs)

        self_.hide_incomplete_cost_data = hide_incomplete_cost_data
