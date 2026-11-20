# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "table". Must be one of ["table"].
    :type value: str
    """

    allowed_values = {
        "table",
    }
    TABLE: ClassVar["QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280.TABLE = (
    QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280("table")
)
