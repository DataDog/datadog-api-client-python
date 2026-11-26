# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.apm_recommendations_stream_request_columns_items import (
        ApmRecommendationsStreamRequestColumnsItems,
    )
    from datadog_api_client.v1_20270101.model.apm_recommendations_stream_query import ApmRecommendationsStreamQuery
    from datadog_api_client.v1_20270101.model.apm_recommendations_stream_request_response_format import (
        ApmRecommendationsStreamRequestResponseFormat,
    )


class ApmRecommendationsStreamRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.apm_recommendations_stream_request_columns_items import (
            ApmRecommendationsStreamRequestColumnsItems,
        )
        from datadog_api_client.v1_20270101.model.apm_recommendations_stream_query import ApmRecommendationsStreamQuery
        from datadog_api_client.v1_20270101.model.apm_recommendations_stream_request_response_format import (
            ApmRecommendationsStreamRequestResponseFormat,
        )

        return {
            "columns": ([ApmRecommendationsStreamRequestColumnsItems],),
            "query": (ApmRecommendationsStreamQuery,),
            "response_format": (ApmRecommendationsStreamRequestResponseFormat,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        columns: List[ApmRecommendationsStreamRequestColumnsItems],
        query: ApmRecommendationsStreamQuery,
        response_format: ApmRecommendationsStreamRequestResponseFormat,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [ApmRecommendationsStreamRequestColumnsItems]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: ApmRecommendationsStreamQuery

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ApmRecommendationsStreamRequestResponseFormat
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.response_format = response_format
