# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class CIAppCreatePipelineEventRequestDataType(StringEnum):
    """
    Type of the event.

    :param value: If omitted defaults to "cipipeline_resource_request". Must be one of ["cipipeline_resource_request"].
    :type value: str
    """

    allowed_values = {
        "cipipeline_resource_request",
    }
    CIPIPELINE_RESOURCE_REQUEST: ClassVar["CIAppCreatePipelineEventRequestDataType"]


CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST = CIAppCreatePipelineEventRequestDataType(
    "cipipeline_resource_request"
)
