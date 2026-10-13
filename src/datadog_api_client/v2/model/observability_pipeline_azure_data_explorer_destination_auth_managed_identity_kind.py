# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityKind(ModelSimple):
    """
    The Azure credential kind. The value should always be `managed_identity`.

    :param value: If omitted defaults to "managed_identity". Must be one of ["managed_identity"].
    :type value: str
    """

    allowed_values = {
        "managed_identity",
    }
    MANAGED_IDENTITY: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityKind.MANAGED_IDENTITY = (
    ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityKind("managed_identity")
)
