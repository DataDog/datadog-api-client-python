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


class StructuredAnalysisCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "column": (str,),
            "name": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "column": "column",
        "name": "name",
    }

    def __init__(self_, aggregation: str, column: str, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: str

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.column = column
