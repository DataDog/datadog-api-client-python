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
    from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
    from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType


class CustomDestinationCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
        from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType

        return {
            "attributes": (CustomDestinationAttributes,),
            "type": (CustomDestinationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CustomDestinationAttributes, type: CustomDestinationType, **kwargs):
        """
        The custom destination data object used for creation.

        :param attributes: The custom destination attributes.
        :type attributes: CustomDestinationAttributes

        :param type: The custom destination type.
        :type type: CustomDestinationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
