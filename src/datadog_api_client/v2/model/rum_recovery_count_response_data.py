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
    from datadog_api_client.v2.model.rum_recovery_count_response_attributes import RumRecoveryCountResponseAttributes
    from datadog_api_client.v2.model.rum_recovery_count_response_data_type import RumRecoveryCountResponseDataType


class RumRecoveryCountResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_count_response_attributes import (
            RumRecoveryCountResponseAttributes,
        )
        from datadog_api_client.v2.model.rum_recovery_count_response_data_type import RumRecoveryCountResponseDataType

        return {
            "attributes": (RumRecoveryCountResponseAttributes,),
            "id": (str,),
            "type": (RumRecoveryCountResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RumRecoveryCountResponseAttributes, id: str, type: RumRecoveryCountResponseDataType, **kwargs
    ):
        """
        JSON:API resource.

        :param attributes: Approximate recoverable count.
        :type attributes: RumRecoveryCountResponseAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: JSON:API resource type.
        :type type: RumRecoveryCountResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
