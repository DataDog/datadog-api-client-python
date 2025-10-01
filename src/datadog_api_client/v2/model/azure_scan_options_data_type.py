# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AzureScanOptionsDataType(ModelSimple):
    """
    The type of the resource. The value should always be `azure_scan_options`.

    :param value: If omitted defaults to "azure_scan_options". Must be one of ["azure_scan_options"].
    :type value: str
    """

    allowed_values = {
        "azure_scan_options",
    }
    AZURE_SCAN_OPTIONS: ClassVar["AzureScanOptionsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AzureScanOptionsDataType.AZURE_SCAN_OPTIONS = AzureScanOptionsDataType("azure_scan_options")
