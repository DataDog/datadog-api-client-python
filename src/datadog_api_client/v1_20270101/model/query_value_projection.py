# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.query_value_projection_type import QueryValueProjectionType


class QueryValueProjection(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.query_value_projection_type import QueryValueProjectionType

        return {
            "dimensions": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
            "type": (QueryValueProjectionType,),
        }

    attribute_map = {
        "dimensions": "dimensions",
        "type": "type",
    }

    def __init__(self_, dimensions: List[Any], type: QueryValueProjectionType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimensions: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: QueryValueProjectionType
        """
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
