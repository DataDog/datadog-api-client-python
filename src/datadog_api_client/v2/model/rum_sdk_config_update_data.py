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
    from datadog_api_client.v2.model.rum_sdk_config_update_attributes import RumSdkConfigUpdateAttributes
    from datadog_api_client.v2.model.rum_sdk_config_type import RumSdkConfigType


class RumSdkConfigUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_update_attributes import RumSdkConfigUpdateAttributes
        from datadog_api_client.v2.model.rum_sdk_config_type import RumSdkConfigType

        return {
            "attributes": (RumSdkConfigUpdateAttributes,),
            "id": (str,),
            "type": (RumSdkConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumSdkConfigUpdateAttributes, id: str, type: RumSdkConfigType, **kwargs):
        """
        The data object for updating a RUM SDK configuration.

        :param attributes: Attributes of the RUM SDK configuration to update.
        :type attributes: RumSdkConfigUpdateAttributes

        :param id: The ID of the RUM SDK configuration to update.
        :type id: str

        :param type: The type of the resource. The value should always be ``rum_sdk_config``.
        :type type: RumSdkConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
