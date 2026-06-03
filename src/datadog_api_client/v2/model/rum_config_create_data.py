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
    from datadog_api_client.v2.model.rum_config_create_attributes import RumConfigCreateAttributes
    from datadog_api_client.v2.model.rum_config_type import RumConfigType


class RumConfigCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_config_create_attributes import RumConfigCreateAttributes
        from datadog_api_client.v2.model.rum_config_type import RumConfigType

        return {
            "attributes": (RumConfigCreateAttributes,),
            "type": (RumConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: RumConfigCreateAttributes, type: RumConfigType, **kwargs):
        """
        Object describing the RUM configuration to create.

        :param attributes: Attributes of the RUM configuration to create.
        :type attributes: RumConfigCreateAttributes

        :param type: The type of the resource. The value should always be ``rum_config``.
        :type type: RumConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
