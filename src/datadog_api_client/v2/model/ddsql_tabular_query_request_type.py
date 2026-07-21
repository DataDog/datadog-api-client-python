# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DdsqlTabularQueryRequestType(ModelSimple):
    """
    JSON:API resource type for a DDSQL tabular query request.

    :param value: If omitted defaults to "ddsql_query_request". Must be one of ["ddsql_query_request"].
    :type value: str
    """

    allowed_values = {
        "ddsql_query_request",
    }
    DDSQL_QUERY_REQUEST: ClassVar["DdsqlTabularQueryRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DdsqlTabularQueryRequestType.DDSQL_QUERY_REQUEST = DdsqlTabularQueryRequestType("ddsql_query_request")
