# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionFilterTrack(ModelSimple):
    """
    The product track a RUM retention filter applies to.

    :param value: Must be one of ["rum", "product_analytics"].
    :type value: str
    """

    allowed_values = {
        "rum",
        "product_analytics",
    }
    RUM: ClassVar["RumRetentionFilterTrack"]
    PRODUCT_ANALYTICS: ClassVar["RumRetentionFilterTrack"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionFilterTrack.RUM = RumRetentionFilterTrack("rum")
RumRetentionFilterTrack.PRODUCT_ANALYTICS = RumRetentionFilterTrack("product_analytics")
