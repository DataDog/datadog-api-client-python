# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GeomapBackendRegionsRequest20270101OneOf4457449888(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "conditional_formats": ([ThresholdFormattingRule],),
            "log_query": (LogQueryDefinition,),
            "style": (GeomapRequestStyle,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "log_query": "log_query",
        "style": "style",
    }

    def __init__(
        self_,
        log_query: LogQueryDefinition,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        style: Union[GeomapRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param log_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type log_query: LogQueryDefinition

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapRequestStyle, optional
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.log_query = log_query
