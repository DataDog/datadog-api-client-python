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
    from datadog_api_client.v2.model.rum_operation_response_attributes import RUMOperationResponseAttributes
    from datadog_api_client.v2.model.rum_operation_type import RUMOperationType


class RUMOperationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_response_attributes import RUMOperationResponseAttributes
        from datadog_api_client.v2.model.rum_operation_type import RUMOperationType

        return {
            "attributes": (RUMOperationResponseAttributes,),
            "id": (str,),
            "type": (RUMOperationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(self_, attributes: RUMOperationResponseAttributes, id: str, type: RUMOperationType, **kwargs):
        """
        The data object in a RUM operation response.

        :param attributes: Attributes of a RUM operation response.
        :type attributes: RUMOperationResponseAttributes

        :param id: The unique identifier of the RUM operation.
        :type id: str

        :param type: The JSON:API type for RUM operation resources.
        :type type: RUMOperationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
