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
from datadog_api_client.v2.model.confluent_resource_response_attributes import ConfluentResourceResponseAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.confluent_account_response_data import ConfluentAccountResponseData


@dataclass
class ConfluentAccountResponseJSON:
    id: str
    api_key: Union[str, UnsetType] = unset
    resources: Union[List[ConfluentResourceResponseAttributes], UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_response_data import ConfluentAccountResponseData

        return {
            "data": (ConfluentAccountResponseData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ConfluentAccountResponseJSON

    def __init__(self_, data: Union[ConfluentAccountResponseData, UnsetType] = unset, **kwargs):
        """
        The expected response schema when getting a Confluent account.

        :param data: An API key and API secret pair that represents a Confluent account.
        :type data: ConfluentAccountResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
