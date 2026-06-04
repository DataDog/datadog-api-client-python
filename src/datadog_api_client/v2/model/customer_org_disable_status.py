# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomerOrgDisableStatus(ModelSimple):
    """
    Resulting lifecycle status of the organization after the disable action.

    :param value: Must be one of ["disabled", "pending_disable"].
    :type value: str
    """

    allowed_values = {
        "disabled",
        "pending_disable",
    }
    DISABLED: ClassVar["CustomerOrgDisableStatus"]
    PENDING_DISABLE: ClassVar["CustomerOrgDisableStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomerOrgDisableStatus.DISABLED = CustomerOrgDisableStatus("disabled")
CustomerOrgDisableStatus.PENDING_DISABLE = CustomerOrgDisableStatus("pending_disable")
