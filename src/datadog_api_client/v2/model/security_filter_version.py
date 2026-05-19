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
    from datadog_api_client.v2.model.security_filter_version_attributes import SecurityFilterVersionAttributes
    from datadog_api_client.v2.model.security_filter_version_type import SecurityFilterVersionType


class SecurityFilterVersion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_version_attributes import SecurityFilterVersionAttributes
        from datadog_api_client.v2.model.security_filter_version_type import SecurityFilterVersionType

        return {
            "attributes": (SecurityFilterVersionAttributes,),
            "id": (str,),
            "type": (SecurityFilterVersionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: SecurityFilterVersionAttributes, id: str, type: SecurityFilterVersionType, **kwargs
    ):
        """
        A snapshot of all security filters at a specific configuration version.

        :param attributes: The attributes describing a single security filter configuration version.
        :type attributes: SecurityFilterVersionAttributes

        :param id: The identifier of the configuration version.
        :type id: str

        :param type: The type of the resource. The value should always be ``security_filters_configuration``.
        :type type: SecurityFilterVersionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
