# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PostmortemStatus(ModelSimple):
    """
    The status of the postmortem.

    :param value: Must be one of ["draft", "in_review", "completed"].
    :type value: str
    """

    allowed_values = {
        "draft",
        "in_review",
        "completed",
    }
    DRAFT: ClassVar["PostmortemStatus"]
    IN_REVIEW: ClassVar["PostmortemStatus"]
    COMPLETED: ClassVar["PostmortemStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PostmortemStatus.DRAFT = PostmortemStatus("draft")
PostmortemStatus.IN_REVIEW = PostmortemStatus("in_review")
PostmortemStatus.COMPLETED = PostmortemStatus("completed")
