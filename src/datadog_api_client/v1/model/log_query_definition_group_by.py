# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogQueryDefinitionGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.log_query_definition_group_by_sort import LogQueryDefinitionGroupBySort

        return {
            "facet": (str,),
            "limit": (int,),
            "sort": (LogQueryDefinitionGroupBySort,),
        }

    attribute_map = {
        "facet": "facet",
        "limit": "limit",
        "sort": "sort",
    }

    def __init__(self_, facet, *args, **kwargs):
        """
        Defined items in the group.

        :param facet: Facet name.
        :type facet: str

        :param limit: Maximum number of items in the group.
        :type limit: int, optional

        :param sort: Define a sorting method.
        :type sort: LogQueryDefinitionGroupBySort, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.facet = facet
