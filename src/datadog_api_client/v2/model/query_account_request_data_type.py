# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryAccountRequestDataType(ModelSimple):
    """
    Query account request resource type.

    :param value: If omitted defaults to "query_account_request". Must be one of ["query_account_request"].
    :type value: str
    """

    allowed_values = {
        "query_account_request",
    }
    QUERY_ACCOUNT_REQUEST: ClassVar["QueryAccountRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryAccountRequestDataType.QUERY_ACCOUNT_REQUEST = QueryAccountRequestDataType("query_account_request")
