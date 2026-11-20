# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.sql_analysis_query_type import SqlAnalysisQueryType


class SqlAnalysisQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.sql_analysis_query_type import SqlAnalysisQueryType

        return {
            "sql_query": (str,),
            "type": (SqlAnalysisQueryType,),
        }

    attribute_map = {
        "sql_query": "sql_query",
        "type": "type",
    }

    def __init__(self_, sql_query: str, type: SqlAnalysisQueryType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param sql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type sql_query: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: SqlAnalysisQueryType
        """
        super().__init__(kwargs)

        self_.sql_query = sql_query
        self_.type = type
