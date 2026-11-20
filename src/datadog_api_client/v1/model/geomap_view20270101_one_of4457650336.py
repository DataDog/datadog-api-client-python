# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class GeomapView20270101OneOf4457650336(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "custom_extent": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
        }

    attribute_map = {
        "custom_extent": "custom_extent",
    }

    def __init__(self_, custom_extent: List[Any], **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param custom_extent: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_extent: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]
        """
        super().__init__(kwargs)

        self_.custom_extent = custom_extent
