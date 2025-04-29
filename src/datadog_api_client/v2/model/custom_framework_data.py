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
    from datadog_api_client.v2.model.custom_framework_data_attributes import CustomFrameworkDataAttributes
    from datadog_api_client.v2.model.custom_framework_type import CustomFrameworkType


class CustomFrameworkData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_framework_data_attributes import CustomFrameworkDataAttributes
        from datadog_api_client.v2.model.custom_framework_type import CustomFrameworkType

        return {
            "attributes": (CustomFrameworkDataAttributes,),
            "type": (CustomFrameworkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CustomFrameworkDataAttributes, type: CustomFrameworkType, **kwargs):
        """
        Contains type and attributes for custom frameworks.

        :param attributes: Framework Data Attributes.
        :type attributes: CustomFrameworkDataAttributes

        :param type: The type of the resource. The value must be ``custom_framework``.
        :type type: CustomFrameworkType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
