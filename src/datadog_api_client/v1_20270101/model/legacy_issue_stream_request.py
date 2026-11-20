# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.issue_stream_column import IssueStreamColumn
    from datadog_api_client.v1_20270101.model.legacy_issue_stream_request20270101_query import (
        LegacyIssueStreamRequest20270101Query,
    )
    from datadog_api_client.v1_20270101.model.legacy_issue_stream_request_response_format import (
        LegacyIssueStreamRequestResponseFormat,
    )
    from datadog_api_client.v1_20270101.model.apm_issue_stream_query import APMIssueStreamQuery
    from datadog_api_client.v1_20270101.model.rum_issue_stream_query import RUMIssueStreamQuery
    from datadog_api_client.v1_20270101.model.logs_issue_stream_query import LogsIssueStreamQuery


class LegacyIssueStreamRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.issue_stream_column import IssueStreamColumn
        from datadog_api_client.v1_20270101.model.legacy_issue_stream_request20270101_query import (
            LegacyIssueStreamRequest20270101Query,
        )
        from datadog_api_client.v1_20270101.model.legacy_issue_stream_request_response_format import (
            LegacyIssueStreamRequestResponseFormat,
        )

        return {
            "columns": ([IssueStreamColumn],),
            "query": (LegacyIssueStreamRequest20270101Query,),
            "response_format": (LegacyIssueStreamRequestResponseFormat,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        columns: List[IssueStreamColumn],
        query: Union[
            LegacyIssueStreamRequest20270101Query, APMIssueStreamQuery, RUMIssueStreamQuery, LogsIssueStreamQuery
        ],
        response_format: LegacyIssueStreamRequestResponseFormat,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [IssueStreamColumn]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: LegacyIssueStreamRequest20270101Query

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: LegacyIssueStreamRequestResponseFormat
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.response_format = response_format
