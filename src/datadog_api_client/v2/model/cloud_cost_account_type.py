# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudCostAccountType(ModelSimple):
    """
    Type of a cloud cost account.

    :param value: If omitted defaults to "cloud_account". Must be one of ["cloud_account"].
    :type value: str
    """

    allowed_values = {
        "cloud_account",
    }
    CLOUD_ACCOUNT: ClassVar["CloudCostAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudCostAccountType.CLOUD_ACCOUNT = CloudCostAccountType("cloud_account")
