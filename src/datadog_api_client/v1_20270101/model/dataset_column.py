# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.advanced_query_data_type import AdvancedQueryDataType


class DatasetColumn(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.advanced_query_data_type import AdvancedQueryDataType

        return {
            "alias": (str,),
            "column": (str,),
            "type": (AdvancedQueryDataType,),
        }

    attribute_map = {
        "alias": "alias",
        "column": "column",
        "type": "type",
    }

    def __init__(self_, column: str, type: AdvancedQueryDataType, alias: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: AdvancedQueryDataType
        """
        if alias is not unset:
            kwargs["alias"] = alias
        super().__init__(kwargs)

        self_.column = column
        self_.type = type
