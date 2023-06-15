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
    from datadog_api_client.v2.model.confluent_account_update_request_data import ConfluentAccountUpdateRequestData


@dataclass
class ConfluentAccountUpdateRequestJSON:
    api_key: Union[str, UnsetType] = unset
    api_secret: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_update_request_data import ConfluentAccountUpdateRequestData

        return {
            "data": (ConfluentAccountUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ConfluentAccountUpdateRequestJSON

    def __init__(self_, data: ConfluentAccountUpdateRequestData, **kwargs):
        """
        The JSON:API request for updating a Confluent account.

        :param data: Data object for updating a Confluent account.
        :type data: ConfluentAccountUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
