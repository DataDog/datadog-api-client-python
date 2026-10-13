# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind(ModelSimple):
    """
    The Azure credential kind. The value should always be `azure_cli`.

    :param value: If omitted defaults to "azure_cli". Must be one of ["azure_cli"].
    :type value: str
    """

    allowed_values = {
        "azure_cli",
    }
    AZURE_CLI: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind.AZURE_CLI = (
    ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind("azure_cli")
)
