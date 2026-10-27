# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HistoricalJobFailureReason(ModelSimple):
    """
    The reason why the job failed.

    :param value: Must be one of ["rule_configuration", "query_too_expensive", "internal_error"].
    :type value: str
    """

    allowed_values = {
        "rule_configuration",
        "query_too_expensive",
        "internal_error",
    }
    RULE_CONFIGURATION: ClassVar["HistoricalJobFailureReason"]
    QUERY_TOO_EXPENSIVE: ClassVar["HistoricalJobFailureReason"]
    INTERNAL_ERROR: ClassVar["HistoricalJobFailureReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HistoricalJobFailureReason.RULE_CONFIGURATION = HistoricalJobFailureReason("rule_configuration")
HistoricalJobFailureReason.QUERY_TOO_EXPENSIVE = HistoricalJobFailureReason("query_too_expensive")
HistoricalJobFailureReason.INTERNAL_ERROR = HistoricalJobFailureReason("internal_error")
