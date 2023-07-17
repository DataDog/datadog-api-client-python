# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GCPSTSDelegateAccountType(ModelSimple):
    """
    The type of account.

    :param value: If omitted defaults to "gcp_sts_delegate". Must be one of ["gcp_sts_delegate"].
    :type value: str
    """

    allowed_values = {
        "gcp_sts_delegate",
    }
    GCP_STS_DELEGATE: ClassVar["GCPSTSDelegateAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GCPSTSDelegateAccountType.GCP_STS_DELEGATE = GCPSTSDelegateAccountType("gcp_sts_delegate")
