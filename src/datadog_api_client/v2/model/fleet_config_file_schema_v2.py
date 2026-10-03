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
    from datadog_api_client.v2.model.fleet_config_file_schema_v2_attributes import FleetConfigFileSchemaV2Attributes
    from datadog_api_client.v2.model.fleet_config_file_schema_v2_resource_type import (
        FleetConfigFileSchemaV2ResourceType,
    )


class FleetConfigFileSchemaV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_config_file_schema_v2_attributes import FleetConfigFileSchemaV2Attributes
        from datadog_api_client.v2.model.fleet_config_file_schema_v2_resource_type import (
            FleetConfigFileSchemaV2ResourceType,
        )

        return {
            "attributes": (FleetConfigFileSchemaV2Attributes,),
            "id": (str,),
            "type": (FleetConfigFileSchemaV2ResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: FleetConfigFileSchemaV2Attributes,
        id: str,
        type: FleetConfigFileSchemaV2ResourceType,
        **kwargs,
    ):
        """
        A configuration file's schema.

        :param attributes: Attributes for a configuration file's schema.
        :type attributes: FleetConfigFileSchemaV2Attributes

        :param id: An identifier for the resolved schema.
        :type id: str

        :param type: The type of the configuration file schema resource.
        :type type: FleetConfigFileSchemaV2ResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
