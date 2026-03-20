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
    from datadog_api_client.v2.model.create_environment_attributes import CreateEnvironmentAttributes
    from datadog_api_client.v2.model.create_environment_data_type import CreateEnvironmentDataType


class CreateEnvironmentData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_environment_attributes import CreateEnvironmentAttributes
        from datadog_api_client.v2.model.create_environment_data_type import CreateEnvironmentDataType

        return {
            "attributes": (CreateEnvironmentAttributes,),
            "type": (CreateEnvironmentDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CreateEnvironmentAttributes, type: CreateEnvironmentDataType, **kwargs):
        """
        Data for creating a new environment.

        :param attributes: Attributes for creating a new environment.
        :type attributes: CreateEnvironmentAttributes

        :param type: The resource type.
        :type type: CreateEnvironmentDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
