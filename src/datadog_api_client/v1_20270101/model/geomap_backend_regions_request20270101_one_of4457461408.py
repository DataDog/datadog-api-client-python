# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.geomap_request_style import GeomapRequestStyle
    from datadog_api_client.v1_20270101.model.log_query_definition import LogQueryDefinition


class GeomapBackendRegionsRequest20270101OneOf4457461408(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.geomap_request_style import GeomapRequestStyle
        from datadog_api_client.v1_20270101.model.log_query_definition import LogQueryDefinition

        return {
            "conditional_formats": ([ThresholdFormattingRule],),
            "style": (GeomapRequestStyle,),
            "synthetics_batches": (LogQueryDefinition,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "style": "style",
        "synthetics_batches": "synthetics_batches",
    }

    def __init__(
        self_,
        synthetics_batches: LogQueryDefinition,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        style: Union[GeomapRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapRequestStyle, optional

        :param synthetics_batches: Test-only generated schema for the dashboard versioning proof of concept.
        :type synthetics_batches: LogQueryDefinition
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.synthetics_batches = synthetics_batches
