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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.api_key_create_data import APIKeyCreateData


@dataclass
class APIKeyCreateRequestJSON:
    name: Union[str, UnsetType] = unset


class APIKeyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.api_key_create_data import APIKeyCreateData

        return {
            "data": (APIKeyCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = APIKeyCreateRequestJSON

    def __init__(self_, data: APIKeyCreateData, **kwargs):
        """
        Request used to create an API key.

        :param data: Object used to create an API key.
        :type data: APIKeyCreateData
        """
        super().__init__(kwargs)

        self_.data = data
