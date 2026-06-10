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
    from datadog_api_client.v2.model.ownership_feedback_request_attributes import OwnershipFeedbackRequestAttributes
    from datadog_api_client.v2.model.ownership_feedback_type import OwnershipFeedbackType


class OwnershipFeedbackRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_feedback_request_attributes import OwnershipFeedbackRequestAttributes
        from datadog_api_client.v2.model.ownership_feedback_type import OwnershipFeedbackType

        return {
            "attributes": (OwnershipFeedbackRequestAttributes,),
            "type": (OwnershipFeedbackType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: OwnershipFeedbackRequestAttributes, type: OwnershipFeedbackType, **kwargs):
        """
        The data wrapper for an ownership feedback request.

        :param attributes: The attributes of an ownership feedback request.
        :type attributes: OwnershipFeedbackRequestAttributes

        :param type: The type of the ownership feedback request resource. The value should always be ``ownership_feedback``.
        :type type: OwnershipFeedbackType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
