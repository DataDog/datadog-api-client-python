# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.confluent_resource_response_attributes import ConfluentResourceResponseAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.confluent_resource_type import ConfluentResourceType


@dataclass
class ConfluentResourceResponseDataJSON:
    id: str
    resource_type: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentResourceResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_resource_type import ConfluentResourceType

        return {
            "attributes": (ConfluentResourceResponseAttributes,),
            "id": (str,),
            "type": (ConfluentResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = ConfluentResourceResponseDataJSON

    def __init__(
        self_, attributes: ConfluentResourceResponseAttributes, id: str, type: ConfluentResourceType, **kwargs
    ):
        """
        Confluent Cloud resource data.

        :param attributes: Model representation of a Confluent Cloud resource.
        :type attributes: ConfluentResourceResponseAttributes

        :param id: The ID associated with the Confluent resource.
        :type id: str

        :param type: The JSON:API type for this request.
        :type type: ConfluentResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
