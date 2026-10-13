# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationType(ModelSimple):
    """
    The destination type. The value should always be `azure_data_explorer`.

    :param value: If omitted defaults to "azure_data_explorer". Must be one of ["azure_data_explorer"].
    :type value: str
    """

    allowed_values = {
        "azure_data_explorer",
    }
    AZURE_DATA_EXPLORER: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationType.AZURE_DATA_EXPLORER = (
    ObservabilityPipelineAzureDataExplorerDestinationType("azure_data_explorer")
)
