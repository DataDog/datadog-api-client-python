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


class WidgetTime20270101OneOf4464105952(ModelNormal):
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

    def __init__(self_, hide_incomplete_cost_data: Union[bool, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param hide_incomplete_cost_data: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_incomplete_cost_data: bool, optional
        """
        if hide_incomplete_cost_data is not unset:
            kwargs["hide_incomplete_cost_data"] = hide_incomplete_cost_data
        super().__init__(kwargs)
