# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceSummaryLayout(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["one_column", "two_column", "three_column"].
    :type value: str
    """

    allowed_values = {
        "one_column",
        "two_column",
        "three_column",
    }
    ONE_COLUMN: ClassVar["ServiceSummaryLayout"]
    TWO_COLUMN: ClassVar["ServiceSummaryLayout"]
    THREE_COLUMN: ClassVar["ServiceSummaryLayout"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceSummaryLayout.ONE_COLUMN = ServiceSummaryLayout("one_column")
ServiceSummaryLayout.TWO_COLUMN = ServiceSummaryLayout("two_column")
ServiceSummaryLayout.THREE_COLUMN = ServiceSummaryLayout("three_column")
