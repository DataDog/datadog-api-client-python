# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind(ModelSimple):
    """
    The Azure credential kind. The value should always be `managed_identity_client_assertion`.

    :param value: If omitted defaults to "managed_identity_client_assertion". Must be one of ["managed_identity_client_assertion"].
    :type value: str
    """

    allowed_values = {
        "managed_identity_client_assertion",
    }
    MANAGED_IDENTITY_CLIENT_ASSERTION: ClassVar[
        "ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind"
    ]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind.MANAGED_IDENTITY_CLIENT_ASSERTION = ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind(
    "managed_identity_client_assertion"
)
