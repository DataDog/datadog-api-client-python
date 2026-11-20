# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineCrowdStrikeFdrSourceType(ModelSimple):
    """
    The source type. Always `crowdstrike_fdr`.

    :param value: If omitted defaults to "crowdstrike_fdr". Must be one of ["crowdstrike_fdr"].
    :type value: str
    """

    allowed_values = {
        "crowdstrike_fdr",
    }
    CROWDSTRIKE_FDR: ClassVar["ObservabilityPipelineCrowdStrikeFdrSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineCrowdStrikeFdrSourceType.CROWDSTRIKE_FDR = ObservabilityPipelineCrowdStrikeFdrSourceType(
    "crowdstrike_fdr"
)
