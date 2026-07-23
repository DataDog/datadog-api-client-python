# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMOperationType(ModelSimple):
    """
    The JSON:API type for RUM operation resources.

    :param value: If omitted defaults to "operations". Must be one of ["operations"].
    :type value: str
    """

    allowed_values = {
        "operations",
    }
    OPERATIONS: ClassVar["RUMOperationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMOperationType.OPERATIONS = RUMOperationType("operations")
