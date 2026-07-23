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
    from datadog_api_client.v2.model.ownership_settings_attributes import OwnershipSettingsAttributes
    from datadog_api_client.v2.model.ownership_settings_type import OwnershipSettingsType


class OwnershipSettingsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_settings_attributes import OwnershipSettingsAttributes
        from datadog_api_client.v2.model.ownership_settings_type import OwnershipSettingsType

        return {
            "attributes": (OwnershipSettingsAttributes,),
            "id": (str,),
            "type": (OwnershipSettingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OwnershipSettingsAttributes, id: str, type: OwnershipSettingsType, **kwargs):
        """
        The data wrapper for an ownership settings response.

        :param attributes: The attributes of the ownership settings response.
        :type attributes: OwnershipSettingsAttributes

        :param id: The identifier of the ownership settings resource.
        :type id: str

        :param type: The type of the ownership settings resource. The value should always be ``ownership_settings``.
        :type type: OwnershipSettingsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
