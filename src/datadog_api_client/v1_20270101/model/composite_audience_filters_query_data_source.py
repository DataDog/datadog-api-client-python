# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CompositeAudienceFiltersQueryDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "product_analytics_audience_filters". Must be one of ["product_analytics_audience_filters"].
    :type value: str
    """

    allowed_values = {
        "product_analytics_audience_filters",
    }
    PRODUCT_ANALYTICS_AUDIENCE_FILTERS: ClassVar["CompositeAudienceFiltersQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CompositeAudienceFiltersQueryDataSource.PRODUCT_ANALYTICS_AUDIENCE_FILTERS = CompositeAudienceFiltersQueryDataSource(
    "product_analytics_audience_filters"
)
