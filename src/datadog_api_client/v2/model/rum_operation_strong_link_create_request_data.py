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
    from datadog_api_client.v2.model.rum_operation_strong_link_create_request_attributes import (
        RUMOperationStrongLinkCreateRequestAttributes,
    )
    from datadog_api_client.v2.model.rum_operation_strong_link_type import RUMOperationStrongLinkType


class RUMOperationStrongLinkCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_strong_link_create_request_attributes import (
            RUMOperationStrongLinkCreateRequestAttributes,
        )
        from datadog_api_client.v2.model.rum_operation_strong_link_type import RUMOperationStrongLinkType

        return {
            "attributes": (RUMOperationStrongLinkCreateRequestAttributes,),
            "type": (RUMOperationStrongLinkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: RUMOperationStrongLinkCreateRequestAttributes, type: RUMOperationStrongLinkType, **kwargs
    ):
        """
        The data object for creating a RUM operation strong link.

        :param attributes: Attributes for creating a RUM operation strong link.
        :type attributes: RUMOperationStrongLinkCreateRequestAttributes

        :param type: The JSON:API type for RUM operation strong link resources.
        :type type: RUMOperationStrongLinkType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
