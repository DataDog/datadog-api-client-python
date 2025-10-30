# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryUsersRequestDataType(ModelSimple):
    """
    Query users request resource type.

    :param value: If omitted defaults to "query_users_request". Must be one of ["query_users_request"].
    :type value: str
    """

    allowed_values = {
        "query_users_request",
    }
    QUERY_USERS_REQUEST: ClassVar["QueryUsersRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryUsersRequestDataType.QUERY_USERS_REQUEST = QueryUsersRequestDataType("query_users_request")
