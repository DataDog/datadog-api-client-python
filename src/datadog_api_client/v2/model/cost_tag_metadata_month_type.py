# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostTagMetadataMonthType(ModelSimple):
    """
    Type of the Cloud Cost Management tag metadata month resource.

    :param value: If omitted defaults to "cost_tag_metadata_month". Must be one of ["cost_tag_metadata_month"].
    :type value: str
    """

    allowed_values = {
        "cost_tag_metadata_month",
    }
    COST_TAG_METADATA_MONTH: ClassVar["CostTagMetadataMonthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostTagMetadataMonthType.COST_TAG_METADATA_MONTH = CostTagMetadataMonthType("cost_tag_metadata_month")
