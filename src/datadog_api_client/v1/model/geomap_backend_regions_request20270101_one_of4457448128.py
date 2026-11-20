# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class GeomapBackendRegionsRequest20270101OneOf4457448128(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "_query_options": (
                {
                    str: (
                        DashboardInlineSchema6,
                        none_type,
                    )
                },
            ),
            "conditional_formats": ([ThresholdFormattingRule],),
            "q": (str,),
            "style": (GeomapRequestStyle,),
        }

    attribute_map = {
        "_query_options": "_query_options",
        "conditional_formats": "conditional_formats",
        "q": "q",
        "style": "style",
    }

    def __init__(
        self_,
        q: str,
        _query_options: Union[Dict[str, Union[DashboardInlineSchema6, str, float, bool]], UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        style: Union[GeomapRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema6, none_type,)}, optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapRequestStyle, optional
        """
        if _query_options is not unset:
            kwargs["_query_options"] = _query_options
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.q = q
