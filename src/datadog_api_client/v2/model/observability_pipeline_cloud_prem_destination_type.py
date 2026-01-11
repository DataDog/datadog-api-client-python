# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineCloudPremDestinationType(ModelSimple):
    """
    The destination type. The value should always be `cloud_prem`.

    :param value: If omitted defaults to "cloud_prem". Must be one of ["cloud_prem"].
    :type value: str
    """

    allowed_values = {
        "cloud_prem",
    }
    CLOUD_PREM: ClassVar["ObservabilityPipelineCloudPremDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineCloudPremDestinationType.CLOUD_PREM = ObservabilityPipelineCloudPremDestinationType("cloud_prem")
