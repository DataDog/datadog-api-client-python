# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgAuthorizedClientType(ModelSimple):
    """
    The resource type for org authorized clients.

    :param value: If omitted defaults to "org_authorized_clients". Must be one of ["org_authorized_clients"].
    :type value: str
    """

    allowed_values = {
        "org_authorized_clients",
    }
    ORG_AUTHORIZED_CLIENTS: ClassVar["OrgAuthorizedClientType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgAuthorizedClientType.ORG_AUTHORIZED_CLIENTS = OrgAuthorizedClientType("org_authorized_clients")
