# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.service_definition_meta import ServiceDefinitionMeta
from datadog_api_client.v2.model.service_definition_schema import ServiceDefinitionSchema
from datadog_api_client.v2.model.service_definition_data_attributes import ServiceDefinitionDataAttributes
from datadog_api_client.v2.model.service_definition_meta import ServiceDefinitionMeta
from datadog_api_client.v2.model.service_definition_schema import ServiceDefinitionSchema
from datadog_api_client.v2.model.service_definition_v1 import ServiceDefinitionV1
from datadog_api_client.v2.model.service_definition_v2 import ServiceDefinitionV2
from datadog_api_client.v2.model.service_definition_v2_dot1 import ServiceDefinitionV2Dot1


@dataclass
class ServiceDefinitionDataJSON:
    meta: Union[ServiceDefinitionMeta, UnsetType] = unset
    schema: Union[
        ServiceDefinitionSchema, ServiceDefinitionV1, ServiceDefinitionV2, ServiceDefinitionV2Dot1, UnsetType
    ] = unset


class ServiceDefinitionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attributes": (ServiceDefinitionDataAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = ServiceDefinitionDataJSON

    def __init__(
        self_,
        attributes: Union[ServiceDefinitionDataAttributes, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Service definition data.

        :param attributes: Service definition attributes.
        :type attributes: ServiceDefinitionDataAttributes, optional

        :param type: Service definition type.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
