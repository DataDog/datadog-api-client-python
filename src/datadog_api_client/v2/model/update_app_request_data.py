# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.update_app_request_data_attributes import UpdateAppRequestDataAttributes
    from datadog_api_client.v2.model.app_definition_type import AppDefinitionType


class UpdateAppRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_app_request_data_attributes import UpdateAppRequestDataAttributes
        from datadog_api_client.v2.model.app_definition_type import AppDefinitionType

        return {
            "attributes": (UpdateAppRequestDataAttributes,),
            "id": (UUID,),
            "type": (AppDefinitionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: AppDefinitionType,
        attributes: Union[UpdateAppRequestDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object containing the new app definition. Any fields not included in the request remain unchanged.

        :param attributes: App definition attributes to be updated, such as name, description, and components.
        :type attributes: UpdateAppRequestDataAttributes, optional

        :param id: The ID of the app to update. The app ID must match the ID in the URL path.
        :type id: UUID, optional

        :param type: The app definition type.
        :type type: AppDefinitionType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
