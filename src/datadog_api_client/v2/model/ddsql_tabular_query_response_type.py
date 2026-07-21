# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DdsqlTabularQueryResponseType(ModelSimple):
    """
    JSON:API resource type for a DDSQL tabular query response.

    :param value: If omitted defaults to "ddsql_query_response". Must be one of ["ddsql_query_response"].
    :type value: str
    """

    allowed_values = {
        "ddsql_query_response",
    }
    DDSQL_QUERY_RESPONSE: ClassVar["DdsqlTabularQueryResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DdsqlTabularQueryResponseType.DDSQL_QUERY_RESPONSE = DdsqlTabularQueryResponseType("ddsql_query_response")
