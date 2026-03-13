# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumSegmentSource(ModelSimple):
    """
    The source of a segment.

    :param value: Must be one of ["user_created", "initial"].
    :type value: str
    """

    allowed_values = {
        "user_created",
        "initial",
    }
    USER_CREATED: ClassVar["RumSegmentSource"]
    INITIAL: ClassVar["RumSegmentSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumSegmentSource.USER_CREATED = RumSegmentSource("user_created")
RumSegmentSource.INITIAL = RumSegmentSource("initial")
