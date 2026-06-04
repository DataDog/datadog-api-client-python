# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomerOrgDisableResponseType(ModelSimple):
    """
    JSON:API resource type for a customer org disable response.

    :param value: If omitted defaults to "org_disable". Must be one of ["org_disable"].
    :type value: str
    """

    allowed_values = {
        "org_disable",
    }
    ORG_DISABLE: ClassVar["CustomerOrgDisableResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomerOrgDisableResponseType.ORG_DISABLE = CustomerOrgDisableResponseType("org_disable")
