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
    from datadog_api_client.v1_20270101.model.occurrence_filter import OccurrenceFilter


class ProductAnalyticsEventOccurrenceQuerySearch(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.occurrence_filter import OccurrenceFilter

        return {
            "occurrences": (OccurrenceFilter,),
            "query": (str,),
        }

    attribute_map = {
        "occurrences": "occurrences",
        "query": "query",
    }

    def __init__(self_, occurrences: OccurrenceFilter, query: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param occurrences: Test-only generated schema for the dashboard versioning proof of concept.
        :type occurrences: OccurrenceFilter

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str
        """
        super().__init__(kwargs)

        self_.occurrences = occurrences
        self_.query = query
