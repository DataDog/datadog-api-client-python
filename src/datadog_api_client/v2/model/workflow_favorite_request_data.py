# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.workflow_favorite_request_attributes import WorkflowFavoriteRequestAttributes
    from datadog_api_client.v2.model.workflow_favorite_request_type import WorkflowFavoriteRequestType


class WorkflowFavoriteRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_favorite_request_attributes import WorkflowFavoriteRequestAttributes
        from datadog_api_client.v2.model.workflow_favorite_request_type import WorkflowFavoriteRequestType

        return {
            "attributes": (WorkflowFavoriteRequestAttributes,),
            "type": (WorkflowFavoriteRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: WorkflowFavoriteRequestAttributes, type: WorkflowFavoriteRequestType, **kwargs):
        """


        :param attributes:
        :type attributes: WorkflowFavoriteRequestAttributes

        :param type: The type for workflow favorite request
        :type type: WorkflowFavoriteRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
