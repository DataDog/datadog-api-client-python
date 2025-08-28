# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgConnectionType(ModelSimple):
    """
    Org connection type.

    :param value: If omitted defaults to "org_connection". Must be one of ["org_connection"].
    :type value: str
    """

    allowed_values = {
        "org_connection",
    }
    ORG_CONNECTION: ClassVar["OrgConnectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgConnectionType.ORG_CONNECTION = OrgConnectionType("org_connection")
