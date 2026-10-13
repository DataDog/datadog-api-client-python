# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind(ModelSimple):
    """
    The Azure credential kind. The value should always be `workload_identity`.

    :param value: If omitted defaults to "workload_identity". Must be one of ["workload_identity"].
    :type value: str
    """

    allowed_values = {
        "workload_identity",
    }
    WORKLOAD_IDENTITY: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind.WORKLOAD_IDENTITY = (
    ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind("workload_identity")
)
