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
    from datadog_api_client.v2.model.rum_operation_request_attributes import RUMOperationRequestAttributes
    from datadog_api_client.v2.model.rum_operation_type import RUMOperationType


class RUMOperationCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_request_attributes import RUMOperationRequestAttributes
        from datadog_api_client.v2.model.rum_operation_type import RUMOperationType

        return {
            "attributes": (RUMOperationRequestAttributes,),
            "type": (RUMOperationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: RUMOperationRequestAttributes, type: RUMOperationType, **kwargs):
        """
        The data object for creating a RUM operation.

        :param attributes: Attributes for creating or updating a RUM operation.
        :type attributes: RUMOperationRequestAttributes

        :param type: The JSON:API type for RUM operation resources.
        :type type: RUMOperationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
