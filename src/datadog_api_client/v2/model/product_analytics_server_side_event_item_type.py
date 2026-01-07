# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsServerSideEventItemType(ModelSimple):
    """
    The type of Product Analytics event. Must be `server` for server-side events.

    :param value: If omitted defaults to "server". Must be one of ["server"].
    :type value: str
    """

    allowed_values = {
        "server",
    }
    SERVER: ClassVar["ProductAnalyticsServerSideEventItemType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsServerSideEventItemType.SERVER = ProductAnalyticsServerSideEventItemType("server")
