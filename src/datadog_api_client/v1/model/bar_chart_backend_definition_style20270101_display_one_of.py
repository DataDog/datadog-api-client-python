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


class BarChartBackendDefinitionStyle20270101DisplayOneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "legend": (BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend,),
            "type": (BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemType,),
        }

    attribute_map = {
        "legend": "legend",
        "type": "type",
    }

    def __init__(
        self_,
        type: BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemType,
        legend: Union[BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param legend: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend: BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: BarChartBackendDefinitionStyleDisplayAnyOfAnyOfItemType
        """
        if legend is not unset:
            kwargs["legend"] = legend
        super().__init__(kwargs)

        self_.type = type
