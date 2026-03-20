# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.environment_attributes import EnvironmentAttributes
    from datadog_api_client.v2.model.create_environment_data_type import CreateEnvironmentDataType


class Environment(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.environment_attributes import EnvironmentAttributes
        from datadog_api_client.v2.model.create_environment_data_type import CreateEnvironmentDataType

        return {
            "attributes": (EnvironmentAttributes,),
            "id": (UUID,),
            "type": (CreateEnvironmentDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: EnvironmentAttributes, id: UUID, type: CreateEnvironmentDataType, **kwargs):
        """
        A feature flag environment resource.

        :param attributes: Attributes of an environment.
        :type attributes: EnvironmentAttributes

        :param id: The unique identifier of the environment.
        :type id: UUID

        :param type: The resource type.
        :type type: CreateEnvironmentDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
