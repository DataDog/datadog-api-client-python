# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType(ModelSimple):
    """
    The destination type. The value should always be `crowdstrike_next_gen_siem`.

    :param value: If omitted defaults to "crowdstrike_next_gen_siem". Must be one of ["crowdstrike_next_gen_siem"].
    :type value: str
    """

    allowed_values = {
        "crowdstrike_next_gen_siem",
    }
    CROWDSTRIKE_NEXT_GEN_SIEM: ClassVar["ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType.CROWDSTRIKE_NEXT_GEN_SIEM = (
    ObservabilityPipelineCrowdStrikeNextGenSiemDestinationType("crowdstrike_next_gen_siem")
)
