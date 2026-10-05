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
    from datadog_api_client.v2.model.fleet_integration_schema_detail_v2_attributes import (
        FleetIntegrationSchemaDetailV2Attributes,
    )
    from datadog_api_client.v2.model.fleet_integration_schema_v2_resource_type import (
        FleetIntegrationSchemaV2ResourceType,
    )


class FleetIntegrationSchemaDetailV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_integration_schema_detail_v2_attributes import (
            FleetIntegrationSchemaDetailV2Attributes,
        )
        from datadog_api_client.v2.model.fleet_integration_schema_v2_resource_type import (
            FleetIntegrationSchemaV2ResourceType,
        )

        return {
            "attributes": (FleetIntegrationSchemaDetailV2Attributes,),
            "id": (str,),
            "type": (FleetIntegrationSchemaV2ResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: FleetIntegrationSchemaDetailV2Attributes,
        id: str,
        type: FleetIntegrationSchemaV2ResourceType,
        **kwargs,
    ):
        """
        The detailed configuration schema for a single integration.

        :param attributes: Attributes for a single integration's configuration schema.
        :type attributes: FleetIntegrationSchemaDetailV2Attributes

        :param id: The integration name used to look up the schema, echoed back from the request.
        :type id: str

        :param type: The type of the integration schema resource.
        :type type: FleetIntegrationSchemaV2ResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
