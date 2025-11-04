# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryEventFilteredUsersRequestDataType(ModelSimple):
    """
    Query event filtered users request resource type.

    :param value: If omitted defaults to "query_event_filtered_users_request". Must be one of ["query_event_filtered_users_request"].
    :type value: str
    """

    allowed_values = {
        "query_event_filtered_users_request",
    }
    QUERY_EVENT_FILTERED_USERS_REQUEST: ClassVar["QueryEventFilteredUsersRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryEventFilteredUsersRequestDataType.QUERY_EVENT_FILTERED_USERS_REQUEST = QueryEventFilteredUsersRequestDataType(
    "query_event_filtered_users_request"
)
