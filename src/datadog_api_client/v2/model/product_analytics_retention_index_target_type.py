# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionIndexTargetType(ModelSimple):
    """
    The discriminator identifying a target selected by index.

    :param value: If omitted defaults to "index". Must be one of ["index"].
    :type value: str
    """

    allowed_values = {
        "index",
    }
    INDEX: ClassVar["ProductAnalyticsRetentionIndexTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionIndexTargetType.INDEX = ProductAnalyticsRetentionIndexTargetType("index")
