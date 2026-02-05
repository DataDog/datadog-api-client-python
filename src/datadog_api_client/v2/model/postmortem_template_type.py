# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PostmortemTemplateType(ModelSimple):
    """
    Postmortem template resource type

    :param value: If omitted defaults to "postmortem_template". Must be one of ["postmortem_template"].
    :type value: str
    """

    allowed_values = {
        "postmortem_template",
    }
    POSTMORTEM_TEMPLATE: ClassVar["PostmortemTemplateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PostmortemTemplateType.POSTMORTEM_TEMPLATE = PostmortemTemplateType("postmortem_template")
