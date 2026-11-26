# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class StructuredAnalysisDestructureColumnsItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "keys": ([str],),
            "source_column": (str,),
            "target_column": (str,),
        }

    attribute_map = {
        "keys": "keys",
        "source_column": "source_column",
        "target_column": "target_column",
    }

    def __init__(self_, keys: List[str], source_column: str, target_column: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param keys: Test-only generated schema for the dashboard versioning proof of concept.
        :type keys: [str]

        :param source_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type source_column: str

        :param target_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_column: str
        """
        super().__init__(kwargs)

        self_.keys = keys
        self_.source_column = source_column
        self_.target_column = target_column
