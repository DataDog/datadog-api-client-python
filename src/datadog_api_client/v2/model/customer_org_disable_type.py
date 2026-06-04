# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomerOrgDisableType(ModelSimple):
    """
    JSON:API resource type for a customer org disable request.

    :param value: If omitted defaults to "customer_org_disable". Must be one of ["customer_org_disable"].
    :type value: str
    """

    allowed_values = {
        "customer_org_disable",
    }
    CUSTOMER_ORG_DISABLE: ClassVar["CustomerOrgDisableType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomerOrgDisableType.CUSTOMER_ORG_DISABLE = CustomerOrgDisableType("customer_org_disable")
