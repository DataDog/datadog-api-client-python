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
from datadog_api_client.v2.model.confluent_account_response_attributes import ConfluentAccountResponseAttributes
from datadog_api_client.v2.model.confluent_resource_response_attributes import ConfluentResourceResponseAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType


@dataclass
class ConfluentAccountResponseDataJSON:
    id: str
    api_key: Union[str, UnsetType] = unset
    resources: Union[List[ConfluentResourceResponseAttributes], UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentAccountResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType

        return {
            "attributes": (ConfluentAccountResponseAttributes,),
            "id": (str,),
            "type": (ConfluentAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = ConfluentAccountResponseDataJSON

    def __init__(self_, attributes: ConfluentAccountResponseAttributes, id: str, type: ConfluentAccountType, **kwargs):
        """
        An API key and API secret pair that represents a Confluent account.

        :param attributes: The attributes of a Confluent account.
        :type attributes: ConfluentAccountResponseAttributes

        :param id: A randomly generated ID associated with a Confluent account.
        :type id: str

        :param type: The JSON:API type for this API. Should always be ``confluent-cloud-accounts``.
        :type type: ConfluentAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
