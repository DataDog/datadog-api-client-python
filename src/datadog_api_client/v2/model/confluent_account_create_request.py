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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.confluent_account_create_request_data import ConfluentAccountCreateRequestData
    from datadog_api_client.v2.model.confluent_account_resource_attributes import ConfluentAccountResourceAttributes


@dataclass
class ConfluentAccountCreateRequestJSON:
    api_key: Union[str, UnsetType] = unset
    api_secret: Union[str, UnsetType] = unset
    resources: Union[List[ConfluentAccountResourceAttributes], UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_create_request_data import ConfluentAccountCreateRequestData

        return {
            "data": (ConfluentAccountCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ConfluentAccountCreateRequestJSON

    def __init__(self_, data: ConfluentAccountCreateRequestData, **kwargs):
        """
        Payload schema when adding a Confluent account.

        :param data: The data body for adding a Confluent account.
        :type data: ConfluentAccountCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
