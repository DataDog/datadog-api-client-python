# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsAzureVMRIStatus(ModelSimple):
    """
    Status of an Azure VM Reserved Instance.

    :param value: Must be one of ["running", "expired", "cancelled"].
    :type value: str
    """

    allowed_values = {
        "running",
        "expired",
        "cancelled",
    }
    RUNNING: ClassVar["CommitmentsAzureVMRIStatus"]
    EXPIRED: ClassVar["CommitmentsAzureVMRIStatus"]
    CANCELLED: ClassVar["CommitmentsAzureVMRIStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsAzureVMRIStatus.RUNNING = CommitmentsAzureVMRIStatus("running")
CommitmentsAzureVMRIStatus.EXPIRED = CommitmentsAzureVMRIStatus("expired")
CommitmentsAzureVMRIStatus.CANCELLED = CommitmentsAzureVMRIStatus("cancelled")
