# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RulesValidateQueryRequestDataType(ModelSimple):
    """
    Validate query resource type.

    :param value: If omitted defaults to "validate_query". Must be one of ["validate_query"].
    :type value: str
    """

    allowed_values = {
        "validate_query",
    }
    VALIDATE_QUERY: ClassVar["RulesValidateQueryRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RulesValidateQueryRequestDataType.VALIDATE_QUERY = RulesValidateQueryRequestDataType("validate_query")
