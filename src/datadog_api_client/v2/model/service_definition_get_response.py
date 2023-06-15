# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.service_definition_meta import ServiceDefinitionMeta
from datadog_api_client.v2.model.service_definition_schema import ServiceDefinitionSchema
from datadog_api_client.v2.model.service_definition_meta import ServiceDefinitionMeta
from datadog_api_client.v2.model.service_definition_schema import ServiceDefinitionSchema
from datadog_api_client.v2.model.service_definition_v1 import ServiceDefinitionV1
from datadog_api_client.v2.model.service_definition_v2 import ServiceDefinitionV2
from datadog_api_client.v2.model.service_definition_v2_dot1 import ServiceDefinitionV2Dot1

if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_definition_data import ServiceDefinitionData


@dataclass
class ServiceDefinitionGetResponseJSON:
    meta: Union[ServiceDefinitionMeta, UnsetType] = unset
    schema: Union[
        ServiceDefinitionSchema, ServiceDefinitionV1, ServiceDefinitionV2, ServiceDefinitionV2Dot1, UnsetType
    ] = unset


class ServiceDefinitionGetResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_definition_data import ServiceDefinitionData

        return {
            "data": (ServiceDefinitionData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ServiceDefinitionGetResponseJSON

    def __init__(self_, data: Union[ServiceDefinitionData, UnsetType] = unset, **kwargs):
        """
        Get service definition response.

        :param data: Service definition data.
        :type data: ServiceDefinitionData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
