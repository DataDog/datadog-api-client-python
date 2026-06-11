# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType(ModelSimple):
    """
    User authorized client resource type.

    :param value: If omitted defaults to "user_authorized_clients". Must be one of ["user_authorized_clients"].
    :type value: str
    """

    allowed_values = {
        "user_authorized_clients",
    }
    USER_AUTHORIZED_CLIENTS: ClassVar["OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType.USER_AUTHORIZED_CLIENTS = (
    OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType("user_authorized_clients")
)
