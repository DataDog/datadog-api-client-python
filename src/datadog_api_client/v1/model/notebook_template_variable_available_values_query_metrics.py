# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookTemplateVariableAvailableValuesQueryMetrics(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "data_source": (str,),
            "query": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "query": "query",
    }

    def __init__(self_, data_source: str, query: str, **kwargs):
        """
        Available values query for the metrics data source.

        :param data_source: The data source for the query. Must be ``metrics``.
        :type data_source: str

        :param query: The metrics query string.
        :type query: str
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query = query
