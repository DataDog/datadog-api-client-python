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
    from datadog_api_client.v2.model.max_session_duration_update_request_data_type import (
        MaxSessionDurationUpdateRequestDataType,
    )


class MaxSessionDurationUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.max_session_duration_update_attributes import (
            MaxSessionDurationUpdateAttributes,
        )
        from datadog_api_client.v2.model.max_session_duration_update_request_data_type import (
            MaxSessionDurationUpdateRequestDataType,
        )

        return {
            "attributes": (MaxSessionDurationUpdateAttributes,),
            "type": (MaxSessionDurationUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: MaxSessionDurationUpdateAttributes, type: MaxSessionDurationUpdateRequestDataType, **kwargs
    ):
        """
        Data wrapper for maximum session duration update.

        :param attributes: Attributes for updating maximum session duration.
        :type attributes: MaxSessionDurationUpdateAttributes

        :param type: Type of the resource.
        :type type: MaxSessionDurationUpdateRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
