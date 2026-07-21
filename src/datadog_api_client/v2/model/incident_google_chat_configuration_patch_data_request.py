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
    from datadog_api_client.v2.model.incident_google_chat_configuration_patch_data_attributes_request import (
        IncidentGoogleChatConfigurationPatchDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_google_chat_configuration_type import IncidentGoogleChatConfigurationType


class IncidentGoogleChatConfigurationPatchDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_chat_configuration_patch_data_attributes_request import (
            IncidentGoogleChatConfigurationPatchDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_google_chat_configuration_type import (
            IncidentGoogleChatConfigurationType,
        )

        return {
            "attributes": (IncidentGoogleChatConfigurationPatchDataAttributesRequest,),
            "id": (UUID,),
            "type": (IncidentGoogleChatConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: IncidentGoogleChatConfigurationType,
        attributes: Union[IncidentGoogleChatConfigurationPatchDataAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Chat configuration data in a patch request.

        :param attributes: Attributes for patching a Google Chat configuration. All fields are optional.
        :type attributes: IncidentGoogleChatConfigurationPatchDataAttributesRequest, optional

        :param id: The configuration identifier.
        :type id: UUID

        :param type: Google Chat configuration resource type.
        :type type: IncidentGoogleChatConfigurationType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
