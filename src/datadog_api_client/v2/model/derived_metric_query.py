# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DerivedMetricQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data_source": (str,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(self_, data_source: str, name: str, query: str, **kwargs):
        """
        A single query used in the definition of a derived metric.

        :param data_source: The data source that the query is run against.
        :type data_source: str

        :param name: The name used to reference this query from the formula.
        :type name: str

        :param query: The query string executed against the data source.
        :type query: str
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
