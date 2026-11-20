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
    from datadog_api_client.v2.model.rum_sdk_config_update_attributes import RUMSdkConfigUpdateAttributes
    from datadog_api_client.v2.model.rum_sdk_config_type import RUMSdkConfigType


class RUMSdkConfigUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_update_attributes import RUMSdkConfigUpdateAttributes
        from datadog_api_client.v2.model.rum_sdk_config_type import RUMSdkConfigType

        return {
            "attributes": (RUMSdkConfigUpdateAttributes,),
            "id": (str,),
            "type": (RUMSdkConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RUMSdkConfigUpdateAttributes, id: str, type: RUMSdkConfigType, **kwargs):
        """
        The data object for updating a RUM SDK configuration.

        :param attributes: Attributes of the RUM SDK configuration to update.
        :type attributes: RUMSdkConfigUpdateAttributes

        :param id: The ID of the RUM SDK configuration to update.
        :type id: str

        :param type: The type of the resource. The value should always be ``rum_sdk_config``.
        :type type: RUMSdkConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
