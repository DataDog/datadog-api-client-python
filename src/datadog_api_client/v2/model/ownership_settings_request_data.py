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
    from datadog_api_client.v2.model.ownership_settings_request_attributes import OwnershipSettingsRequestAttributes
    from datadog_api_client.v2.model.ownership_settings_type import OwnershipSettingsType


class OwnershipSettingsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_settings_request_attributes import OwnershipSettingsRequestAttributes
        from datadog_api_client.v2.model.ownership_settings_type import OwnershipSettingsType

        return {
            "attributes": (OwnershipSettingsRequestAttributes,),
            "type": (OwnershipSettingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: OwnershipSettingsRequestAttributes, type: OwnershipSettingsType, **kwargs):
        """
        The data wrapper for an ownership settings request.

        :param attributes: The attributes of an ownership settings request.
        :type attributes: OwnershipSettingsRequestAttributes

        :param type: The type of the ownership settings resource. The value should always be ``ownership_settings``.
        :type type: OwnershipSettingsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
