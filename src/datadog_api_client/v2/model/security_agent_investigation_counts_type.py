# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentInvestigationCountsType(ModelSimple):
    """
    Type of the investigation counts resource.

    :param value: If omitted defaults to "investigation_counts". Must be one of ["investigation_counts"].
    :type value: str
    """

    allowed_values = {
        "investigation_counts",
    }
    INVESTIGATION_COUNTS: ClassVar["SecurityAgentInvestigationCountsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentInvestigationCountsType.INVESTIGATION_COUNTS = SecurityAgentInvestigationCountsType("investigation_counts")
