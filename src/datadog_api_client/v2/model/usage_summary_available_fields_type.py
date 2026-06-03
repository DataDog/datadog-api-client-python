# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UsageSummaryAvailableFieldsType(ModelSimple):
    """
    Type of available-fields data.

    :param value: If omitted defaults to "usage_summary_available_fields". Must be one of ["usage_summary_available_fields"].
    :type value: str
    """

    allowed_values = {
        "usage_summary_available_fields",
    }
    USAGE_SUMMARY_AVAILABLE_FIELDS: ClassVar["UsageSummaryAvailableFieldsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UsageSummaryAvailableFieldsType.USAGE_SUMMARY_AVAILABLE_FIELDS = UsageSummaryAvailableFieldsType(
    "usage_summary_available_fields"
)
