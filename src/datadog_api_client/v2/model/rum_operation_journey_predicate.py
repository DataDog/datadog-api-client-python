# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMOperationJourneyPredicate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
        }

    attribute_map = {
        "query": "query",
    }

    def __init__(self_, query: str, **kwargs):
        """
        A single predicate within a composite rule, matching RUM events with a query.

        :param query: The RUM search query used to match events for this predicate.
        :type query: str
        """
        super().__init__(kwargs)

        self_.query = query
