# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumSegmentTemplateStatus(ModelSimple):
    """
    The status of a segment template.

    :param value: Must be one of ["active", "deprecated", "archived"].
    :type value: str
    """

    allowed_values = {
        "active",
        "deprecated",
        "archived",
    }
    ACTIVE: ClassVar["RumSegmentTemplateStatus"]
    DEPRECATED: ClassVar["RumSegmentTemplateStatus"]
    ARCHIVED: ClassVar["RumSegmentTemplateStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumSegmentTemplateStatus.ACTIVE = RumSegmentTemplateStatus("active")
RumSegmentTemplateStatus.DEPRECATED = RumSegmentTemplateStatus("deprecated")
RumSegmentTemplateStatus.ARCHIVED = RumSegmentTemplateStatus("archived")
