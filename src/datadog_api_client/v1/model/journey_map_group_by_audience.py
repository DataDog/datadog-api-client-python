# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JourneyMapGroupByAudience(ModelSimple):
    """
    Audience the group by facet is read from.

    :param value: Must be one of ["product_analytics_audience_filters.users", "product_analytics_audience_filters.accounts"].
    :type value: str
    """

    allowed_values = {
        "product_analytics_audience_filters.users",
        "product_analytics_audience_filters.accounts",
    }
    USERS: ClassVar["JourneyMapGroupByAudience"]
    ACCOUNTS: ClassVar["JourneyMapGroupByAudience"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JourneyMapGroupByAudience.USERS = JourneyMapGroupByAudience("product_analytics_audience_filters.users")
JourneyMapGroupByAudience.ACCOUNTS = JourneyMapGroupByAudience("product_analytics_audience_filters.accounts")
