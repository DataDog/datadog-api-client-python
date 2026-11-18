# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SegmentEntity(ModelSimple):
    """
    Kind of entity that a segment contains.

    :param value: Must be one of ["user", "account"].
    :type value: str
    """

    allowed_values = {
        "user",
        "account",
    }
    USER: ClassVar["SegmentEntity"]
    ACCOUNT: ClassVar["SegmentEntity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SegmentEntity.USER = SegmentEntity("user")
SegmentEntity.ACCOUNT = SegmentEntity("account")
