# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditTrafficSummaryV2DTODataType(ModelSimple):
    """
    Bandit traffic summary resource type.

    :param value: If omitted defaults to "bandit-traffic-summary". Must be one of ["bandit-traffic-summary"].
    :type value: str
    """

    allowed_values = {
        "bandit-traffic-summary",
    }
    BANDIT_TRAFFIC_SUMMARY: ClassVar["ExperimentsBanditTrafficSummaryV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditTrafficSummaryV2DTODataType.BANDIT_TRAFFIC_SUMMARY = ExperimentsBanditTrafficSummaryV2DTODataType(
    "bandit-traffic-summary"
)
