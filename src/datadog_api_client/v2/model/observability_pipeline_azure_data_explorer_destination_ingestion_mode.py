# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAzureDataExplorerDestinationIngestionMode(ModelSimple):
    """
    The ingestion method used to send data to Azure Data Explorer.

        - `streaming`: Sends events directly to the table using streaming ingestion.
        - `queue`: Sends events through queued (batched) ingestion.

        Defaults to `streaming`.

    :param value: If omitted defaults to "streaming". Must be one of ["streaming", "queue"].
    :type value: str
    """

    allowed_values = {
        "streaming",
        "queue",
    }
    STREAMING: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationIngestionMode"]
    QUEUE: ClassVar["ObservabilityPipelineAzureDataExplorerDestinationIngestionMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAzureDataExplorerDestinationIngestionMode.STREAMING = (
    ObservabilityPipelineAzureDataExplorerDestinationIngestionMode("streaming")
)
ObservabilityPipelineAzureDataExplorerDestinationIngestionMode.QUEUE = (
    ObservabilityPipelineAzureDataExplorerDestinationIngestionMode("queue")
)
