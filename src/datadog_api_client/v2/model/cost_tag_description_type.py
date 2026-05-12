# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostTagDescriptionType(ModelSimple):
    """
    Type of the Cloud Cost Management tag description resource.

    :param value: If omitted defaults to "cost_tag_description". Must be one of ["cost_tag_description"].
    :type value: str
    """

    allowed_values = {
        "cost_tag_description",
    }
    COST_TAG_DESCRIPTION: ClassVar["CostTagDescriptionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostTagDescriptionType.COST_TAG_DESCRIPTION = CostTagDescriptionType("cost_tag_description")
