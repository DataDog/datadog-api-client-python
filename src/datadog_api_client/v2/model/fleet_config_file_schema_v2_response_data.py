# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class FleetConfigFileSchemaV2ResponseData(ModelComposed):
    def __init__(self, **kwargs):
        """
        The schema resolved for the requested configuration file.

        :param attributes: Attributes for a single integration's configuration schema.
        :type attributes: FleetIntegrationSchemaDetailV2Attributes

        :param id: The integration name used to look up the schema, echoed back from the request.
        :type id: str

        :param type: The type of the integration schema resource.
        :type type: FleetIntegrationSchemaV2ResourceType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.fleet_integration_schema_detail_v2 import FleetIntegrationSchemaDetailV2
        from datadog_api_client.v2.model.fleet_config_file_schema_v2 import FleetConfigFileSchemaV2

        return {
            "oneOf": [
                FleetIntegrationSchemaDetailV2,
                FleetConfigFileSchemaV2,
            ],
        }
