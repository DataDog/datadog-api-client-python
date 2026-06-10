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
    from datadog_api_client.v2.model.ownership_feedback_result_attributes import OwnershipFeedbackResultAttributes
    from datadog_api_client.v2.model.ownership_feedback_result_type import OwnershipFeedbackResultType


class OwnershipFeedbackResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_feedback_result_attributes import OwnershipFeedbackResultAttributes
        from datadog_api_client.v2.model.ownership_feedback_result_type import OwnershipFeedbackResultType

        return {
            "attributes": (OwnershipFeedbackResultAttributes,),
            "id": (str,),
            "type": (OwnershipFeedbackResultType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: OwnershipFeedbackResultAttributes, id: str, type: OwnershipFeedbackResultType, **kwargs
    ):
        """
        The data wrapper for an ownership feedback result response.

        :param attributes: The attributes of an ownership feedback result.
        :type attributes: OwnershipFeedbackResultAttributes

        :param id: The identifier of the resource that the feedback was applied to.
        :type id: str

        :param type: The type of the ownership feedback result resource. The value should always be ``ownership_feedback_result``.
        :type type: OwnershipFeedbackResultType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
