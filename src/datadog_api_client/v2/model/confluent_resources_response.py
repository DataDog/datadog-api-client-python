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
    from datadog_api_client.v2.model.confluent_resource_response_data import ConfluentResourceResponseData


@dataclass
class ConfluentResourcesResponseJSON:
    id: str
    resource_type: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentResourcesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_resource_response_data import ConfluentResourceResponseData

        return {
            "data": ([ConfluentResourceResponseData],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ConfluentResourcesResponseJSON

    def __init__(self_, data: Union[List[ConfluentResourceResponseData], UnsetType] = unset, **kwargs):
        """
        Response schema when interacting with a list of Confluent resources.

        :param data: The JSON:API data attribute.
        :type data: [ConfluentResourceResponseData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
