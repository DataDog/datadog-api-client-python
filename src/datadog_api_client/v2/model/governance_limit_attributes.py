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


class GovernanceLimitAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_limit_query import GovernanceLimitQuery
        from datadog_api_client.v2.model.governance_limit_query_config import GovernanceLimitQueryConfig

        return {
            "description": (str,),
            "display_name": (str,),
            "limit_type": (str,),
            "product": (str,),
            "query": (GovernanceLimitQuery,),
            "query_config": (GovernanceLimitQueryConfig,),
            "time_range": (str,),
            "times_hit_limit": (float,),
            "unit_name": (str,),
            "usage_status": (str,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "limit_type": "limit_type",
        "product": "product",
        "query": "query",
        "query_config": "query_config",
        "time_range": "time_range",
        "times_hit_limit": "times_hit_limit",
        "unit_name": "unit_name",
        "usage_status": "usage_status",
    }

    def __init__(
        self_,
        description: str,
        display_name: str,
        limit_type: str,
        product: str,
        query: GovernanceLimitQuery,
        query_config: GovernanceLimitQueryConfig,
        time_range: str,
        times_hit_limit: float,
        unit_name: str,
        usage_status: str,
        **kwargs,
    ):
        """
        The attributes of a governance limit.

        :param description: A description of what the limit measures.
        :type description: str

        :param display_name: The human-readable name of the limit.
        :type display_name: str

        :param limit_type: The type of limit, such as a rate limit or a usage limit.
        :type limit_type: str

        :param product: The Datadog product the limit belongs to.
        :type product: str

        :param query: A metric query used to compute usage against a limit.
        :type query: GovernanceLimitQuery

        :param query_config: The query execution context used to visualize a limit and its usage.
        :type query_config: GovernanceLimitQueryConfig

        :param time_range: The time range over which usage against the limit is measured.
        :type time_range: str

        :param times_hit_limit: The number of times usage has reached the limit within the measured time range.
        :type times_hit_limit: float

        :param unit_name: The unit in which the limit and its usage are measured.
        :type unit_name: str

        :param usage_status: The current usage status of the limit relative to its threshold.
        :type usage_status: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.display_name = display_name
        self_.limit_type = limit_type
        self_.product = product
        self_.query = query
        self_.query_config = query_config
        self_.time_range = time_range
        self_.times_hit_limit = times_hit_limit
        self_.unit_name = unit_name
        self_.usage_status = usage_status
