# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType(ModelSimple):
    """
    The type of the user-assigned managed identity ID.

    :param value: Must be one of ["client_id", "object_id", "resource_id"].
    :type value: str
    """

    allowed_values = {
        "client_id",
        "object_id",
        "resource_id",
    }
    CLIENT_ID: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType"]
    OBJECT_ID: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType"]
    RESOURCE_ID: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType.CLIENT_ID = (
    ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType("client_id")
)
ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType.OBJECT_ID = (
    ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType("object_id")
)
ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType.RESOURCE_ID = (
    ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType("resource_id")
)
