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
    from datadog_api_client.v2.model.governance_limit_query import GovernanceLimitQuery
    from datadog_api_client.v2.model.governance_limit_query_config import GovernanceLimitQueryConfig


class GovernanceResourceLimitAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_limit_query import GovernanceLimitQuery
        from datadog_api_client.v2.model.governance_limit_query_config import GovernanceLimitQueryConfig

        return {
            "current_limit": (float,),
            "current_value": (float,),
            "deep_link": (str,),
            "default_current_value": (float,),
            "default_limit_value": (float,),
            "description": (str,),
            "display_name": (str,),
            "limit_query": (GovernanceLimitQuery,),
            "product": (str,),
            "query": (GovernanceLimitQuery,),
            "query_config": (GovernanceLimitQueryConfig,),
            "time_range": (str,),
            "unit_name": (str,),
            "usage_status": (str,),
        }

    attribute_map = {
        "current_limit": "current_limit",
        "current_value": "current_value",
        "deep_link": "deep_link",
        "default_current_value": "default_current_value",
        "default_limit_value": "default_limit_value",
        "description": "description",
        "display_name": "display_name",
        "limit_query": "limit_query",
        "product": "product",
        "query": "query",
        "query_config": "query_config",
        "time_range": "time_range",
        "unit_name": "unit_name",
        "usage_status": "usage_status",
    }

    def __init__(
        self_,
        current_limit: float,
        current_value: float,
        deep_link: str,
        default_current_value: float,
        default_limit_value: float,
        description: str,
        display_name: str,
        limit_query: GovernanceLimitQuery,
        product: str,
        query: GovernanceLimitQuery,
        query_config: GovernanceLimitQueryConfig,
        time_range: str,
        unit_name: str,
        usage_status: str,
        **kwargs,
    ):
        """
        The attributes of a governance resource limit.

        :param current_limit: The current limit configured for the resource.
        :type current_limit: float

        :param current_value: The current value of the resource.
        :type current_value: float

        :param deep_link: A link to the Datadog page where the resource and its limit can be managed.
        :type deep_link: str

        :param default_current_value: The default current value used when the resource value cannot be computed from the query.
        :type default_current_value: float

        :param default_limit_value: The default limit value used when the limit cannot be computed from the query.
        :type default_limit_value: float

        :param description: A description of what the resource limit measures.
        :type description: str

        :param display_name: The human-readable name of the resource limit.
        :type display_name: str

        :param limit_query: A metric query used to compute usage against a limit.
        :type limit_query: GovernanceLimitQuery

        :param product: The Datadog product the resource limit belongs to.
        :type product: str

        :param query: A metric query used to compute usage against a limit.
        :type query: GovernanceLimitQuery

        :param query_config: The query execution context used to visualize a limit and its usage.
        :type query_config: GovernanceLimitQueryConfig

        :param time_range: The time range over which the resource value is measured.
        :type time_range: str

        :param unit_name: The unit in which the resource value and limit are measured.
        :type unit_name: str

        :param usage_status: The current usage status of the resource relative to its limit.
        :type usage_status: str
        """
        super().__init__(kwargs)

        self_.current_limit = current_limit
        self_.current_value = current_value
        self_.deep_link = deep_link
        self_.default_current_value = default_current_value
        self_.default_limit_value = default_limit_value
        self_.description = description
        self_.display_name = display_name
        self_.limit_query = limit_query
        self_.product = product
        self_.query = query
        self_.query_config = query_config
        self_.time_range = time_range
        self_.unit_name = unit_name
        self_.usage_status = usage_status
