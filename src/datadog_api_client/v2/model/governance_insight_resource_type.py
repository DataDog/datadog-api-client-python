# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceInsightResourceType(ModelSimple):
    """
    JSON:API resource type for a governance insight.

    :param value: If omitted defaults to "insight". Must be one of ["insight"].
    :type value: str
    """

    allowed_values = {
        "insight",
    }
    INSIGHT: ClassVar["GovernanceInsightResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceInsightResourceType.INSIGHT = GovernanceInsightResourceType("insight")
