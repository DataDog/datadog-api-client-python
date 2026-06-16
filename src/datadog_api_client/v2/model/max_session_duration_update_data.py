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
    from datadog_api_client.v2.model.max_session_duration_update_attributes import MaxSessionDurationUpdateAttributes
    from datadog_api_client.v2.model.max_session_duration_type import MaxSessionDurationType


class MaxSessionDurationUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.max_session_duration_update_attributes import (
            MaxSessionDurationUpdateAttributes,
        )
        from datadog_api_client.v2.model.max_session_duration_type import MaxSessionDurationType

        return {
            "attributes": (MaxSessionDurationUpdateAttributes,),
            "type": (MaxSessionDurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: MaxSessionDurationUpdateAttributes, type: MaxSessionDurationType, **kwargs):
        """
        The data object for a maximum session duration update request.

        :param attributes: Attributes for the maximum session duration update request.
        :type attributes: MaxSessionDurationUpdateAttributes

        :param type: Data type of a maximum session duration update.
        :type type: MaxSessionDurationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
