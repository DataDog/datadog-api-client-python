# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GCPServiceAccountType(ModelSimple):
    """
    The type of account.

    :param value: If omitted defaults to "gcp_service_account". Must be one of ["gcp_service_account"].
    :type value: str
    """

    allowed_values = {
        "gcp_service_account",
    }
    GCP_SERVICE_ACCOUNT: ClassVar["GCPServiceAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GCPServiceAccountType.GCP_SERVICE_ACCOUNT = GCPServiceAccountType("gcp_service_account")
