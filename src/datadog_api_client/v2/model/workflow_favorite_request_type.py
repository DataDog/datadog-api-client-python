# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WorkflowFavoriteRequestType(ModelSimple):
    """
    The type for workflow favorite request

    :param value: If omitted defaults to "workflow_favorite_request". Must be one of ["workflow_favorite_request"].
    :type value: str
    """

    allowed_values = {
        "workflow_favorite_request",
    }
    WORKFLOW_FAVORITE_REQUEST: ClassVar["WorkflowFavoriteRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WorkflowFavoriteRequestType.WORKFLOW_FAVORITE_REQUEST = WorkflowFavoriteRequestType("workflow_favorite_request")
