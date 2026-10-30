# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TemporaryGrantRequestType(ModelSimple):
    """
    The temporary grant request resource type.

    :param value: If omitted defaults to "temporary_grant_requests". Must be one of ["temporary_grant_requests"].
    :type value: str
    """

    allowed_values = {
        "temporary_grant_requests",
    }
    TEMPORARY_GRANT_REQUESTS: ClassVar["TemporaryGrantRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TemporaryGrantRequestType.TEMPORARY_GRANT_REQUESTS = TemporaryGrantRequestType("temporary_grant_requests")
