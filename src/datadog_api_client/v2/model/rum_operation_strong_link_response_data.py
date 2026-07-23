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
    from datadog_api_client.v2.model.rum_operation_strong_link_response_attributes import (
        RUMOperationStrongLinkResponseAttributes,
    )
    from datadog_api_client.v2.model.rum_operation_strong_link_type import RUMOperationStrongLinkType


class RUMOperationStrongLinkResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_strong_link_response_attributes import (
            RUMOperationStrongLinkResponseAttributes,
        )
        from datadog_api_client.v2.model.rum_operation_strong_link_type import RUMOperationStrongLinkType

        return {
            "attributes": (RUMOperationStrongLinkResponseAttributes,),
            "id": (str,),
            "type": (RUMOperationStrongLinkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_, attributes: RUMOperationStrongLinkResponseAttributes, id: str, type: RUMOperationStrongLinkType, **kwargs
    ):
        """
        The data object in a RUM operation strong link response.

        :param attributes: Attributes of a RUM operation strong link response.
        :type attributes: RUMOperationStrongLinkResponseAttributes

        :param id: The unique identifier of the strong link, formatted as ``<operation_id>:<feature_id>``.
        :type id: str

        :param type: The JSON:API type for RUM operation strong link resources.
        :type type: RUMOperationStrongLinkType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
