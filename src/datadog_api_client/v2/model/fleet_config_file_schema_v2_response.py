# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_config_file_schema_v2_response_data import (
        FleetConfigFileSchemaV2ResponseData,
    )
    from datadog_api_client.v2.model.fleet_integration_schema_detail_v2 import FleetIntegrationSchemaDetailV2
    from datadog_api_client.v2.model.fleet_config_file_schema_v2 import FleetConfigFileSchemaV2


class FleetConfigFileSchemaV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_config_file_schema_v2_response_data import (
            FleetConfigFileSchemaV2ResponseData,
        )

        return {
            "data": (FleetConfigFileSchemaV2ResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_,
        data: Union[FleetConfigFileSchemaV2ResponseData, FleetIntegrationSchemaDetailV2, FleetConfigFileSchemaV2],
        **kwargs,
    ):
        """
        Response containing the schema for a configuration file.

        :param data: The schema resolved for the requested configuration file.
        :type data: FleetConfigFileSchemaV2ResponseData
        """
        super().__init__(kwargs)

        self_.data = data
