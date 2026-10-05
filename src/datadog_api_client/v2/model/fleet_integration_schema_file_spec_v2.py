# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_integration_schema_spec_option_v2 import FleetIntegrationSchemaSpecOptionV2


class FleetIntegrationSchemaFileSpecV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_integration_schema_spec_option_v2 import (
            FleetIntegrationSchemaSpecOptionV2,
        )

        return {
            "example_name": (str,),
            "name": (str,),
            "options": ([FleetIntegrationSchemaSpecOptionV2],),
        }

    attribute_map = {
        "example_name": "example_name",
        "name": "name",
        "options": "options",
    }

    def __init__(self_, example_name: str, name: str, options: List[FleetIntegrationSchemaSpecOptionV2], **kwargs):
        """
        A configuration file specification for an integration.

        :param example_name: The name of the example configuration file.
        :type example_name: str

        :param name: The name of the configuration file.
        :type name: str

        :param options: The configuration options declared in the file.
        :type options: [FleetIntegrationSchemaSpecOptionV2]
        """
        super().__init__(kwargs)

        self_.example_name = example_name
        self_.name = name
        self_.options = options
