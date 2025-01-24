# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.get_app_response_data_attributes import GetAppResponseDataAttributes
    from datadog_api_client.v2.model.app_definition_type import AppDefinitionType


class GetAppResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_app_response_data_attributes import GetAppResponseDataAttributes
        from datadog_api_client.v2.model.app_definition_type import AppDefinitionType

        return {
            "attributes": (GetAppResponseDataAttributes,),
            "id": (UUID,),
            "type": (AppDefinitionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: GetAppResponseDataAttributes, id: UUID, type: AppDefinitionType, **kwargs):
        """
        The data object containing the app definition.

        :param attributes: The app definition attributes, such as name, description, and components.
        :type attributes: GetAppResponseDataAttributes

        :param id: The ID of the app.
        :type id: UUID

        :param type: The app definition type.
        :type type: AppDefinitionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
