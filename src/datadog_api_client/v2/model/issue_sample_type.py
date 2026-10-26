# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueSampleType(ModelSimple):
    """
    Type of the object.

    :param value: If omitted defaults to "error_tracking_issue_sample". Must be one of ["error_tracking_issue_sample"].
    :type value: str
    """

    allowed_values = {
        "error_tracking_issue_sample",
    }
    ERROR_TRACKING_ISSUE_SAMPLE: ClassVar["IssueSampleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueSampleType.ERROR_TRACKING_ISSUE_SAMPLE = IssueSampleType("error_tracking_issue_sample")
