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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_app_request_data_attributes import CreateAppRequestDataAttributes
    from datadog_api_client.v2.model.app_definition_type import AppDefinitionType


class CreateAppRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_app_request_data_attributes import CreateAppRequestDataAttributes
        from datadog_api_client.v2.model.app_definition_type import AppDefinitionType

        return {
            "attributes": (CreateAppRequestDataAttributes,),
            "type": (AppDefinitionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, type: AppDefinitionType, attributes: Union[CreateAppRequestDataAttributes, UnsetType] = unset, **kwargs
    ):
        """
        The data object containing the app definition.

        :param attributes: App definition attributes such as name, description, and components.
        :type attributes: CreateAppRequestDataAttributes, optional

        :param type: The app definition type.
        :type type: AppDefinitionType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
