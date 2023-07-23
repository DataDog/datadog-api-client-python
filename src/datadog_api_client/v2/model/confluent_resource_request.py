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
    from datadog_api_client.v2.model.confluent_resource_request_data import ConfluentResourceRequestData


@dataclass
class ConfluentResourceRequestJSON:
    id: str
    resource_type: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentResourceRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_resource_request_data import ConfluentResourceRequestData

        return {
            "data": (ConfluentResourceRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ConfluentResourceRequestJSON

    def __init__(self_, data: ConfluentResourceRequestData, **kwargs):
        """
        The JSON:API request for updating a Confluent resource.

        :param data: JSON:API request for updating a Confluent resource.
        :type data: ConfluentResourceRequestData
        """
        super().__init__(kwargs)

        self_.data = data
