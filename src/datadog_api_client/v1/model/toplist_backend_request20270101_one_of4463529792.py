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


class ToplistBackendRequest20270101OneOf4463529792(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "audit_query": (LogQueryDefinition,),
            "conditional_formats": ([ThresholdFormattingRule],),
        }

    attribute_map = {
        "audit_query": "audit_query",
        "conditional_formats": "conditional_formats",
    }

    def __init__(
        self_,
        audit_query: LogQueryDefinition,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param audit_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type audit_query: LogQueryDefinition

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        super().__init__(kwargs)

        self_.audit_query = audit_query
