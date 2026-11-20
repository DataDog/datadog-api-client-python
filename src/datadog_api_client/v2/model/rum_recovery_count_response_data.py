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
    from datadog_api_client.v2.model.rum_recovery_count_response_attributes import RUMRecoveryCountResponseAttributes
    from datadog_api_client.v2.model.rum_recovery_count_response_data_type import RUMRecoveryCountResponseDataType


class RUMRecoveryCountResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_count_response_attributes import (
            RUMRecoveryCountResponseAttributes,
        )
        from datadog_api_client.v2.model.rum_recovery_count_response_data_type import RUMRecoveryCountResponseDataType

        return {
            "attributes": (RUMRecoveryCountResponseAttributes,),
            "id": (str,),
            "type": (RUMRecoveryCountResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RUMRecoveryCountResponseAttributes, id: str, type: RUMRecoveryCountResponseDataType, **kwargs
    ):
        """
        JSON:API resource.

        :param attributes: Approximate recoverable count.
        :type attributes: RUMRecoveryCountResponseAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: JSON:API resource type.
        :type type: RUMRecoveryCountResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
