# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GuidedTableGroupKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "group_key": (str,),
            "query": (str,),
        }

    attribute_map = {
        "group_key": "group_key",
        "query": "query",
    }

    def __init__(self_, group_key: str, query: str, **kwargs):
        """
        Maps a specific base query to the field name used for grouping.

        :param group_key: Field name in the query result used as the grouping key.
        :type group_key: str

        :param query: Name of the source query.
        :type query: str
        """
        super().__init__(kwargs)

        self_.group_key = group_key
        self_.query = query
