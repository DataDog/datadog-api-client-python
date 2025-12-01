# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsRestrictionQueriesType(ModelSimple):
    """
    Restriction query resource type.

    :param value: If omitted defaults to "logs_restriction_queries". Must be one of ["logs_restriction_queries"].
    :type value: str
    """

    allowed_values = {
        "logs_restriction_queries",
    }
    LOGS_RESTRICTION_QUERIES: ClassVar["LogsRestrictionQueriesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES = LogsRestrictionQueriesType("logs_restriction_queries")
