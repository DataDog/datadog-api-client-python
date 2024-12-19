# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AwsScanOptionsType(ModelSimple):
    """
    The type of the resource. The value should always be `aws_scan_options`.

    :param value: If omitted defaults to "aws_scan_options". Must be one of ["aws_scan_options"].
    :type value: str
    """

    allowed_values = {
        "aws_scan_options",
    }
    AWS_SCAN_OPTIONS: ClassVar["AwsScanOptionsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AwsScanOptionsType.AWS_SCAN_OPTIONS = AwsScanOptionsType("aws_scan_options")
