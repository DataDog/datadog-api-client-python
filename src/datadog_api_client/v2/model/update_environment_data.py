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
    from datadog_api_client.v2.model.update_environment_attributes import UpdateEnvironmentAttributes
    from datadog_api_client.v2.model.update_environment_data_type import UpdateEnvironmentDataType


class UpdateEnvironmentData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_environment_attributes import UpdateEnvironmentAttributes
        from datadog_api_client.v2.model.update_environment_data_type import UpdateEnvironmentDataType

        return {
            "attributes": (UpdateEnvironmentAttributes,),
            "type": (UpdateEnvironmentDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpdateEnvironmentAttributes, type: UpdateEnvironmentDataType, **kwargs):
        """
        Data for updating an environment.

        :param attributes: Attributes for updating an environment.
        :type attributes: UpdateEnvironmentAttributes

        :param type: The resource type.
        :type type: UpdateEnvironmentDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
