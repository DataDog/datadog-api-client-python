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
    from datadog_api_client.v2.model.fastly_account_update_request_data import FastlyAccountUpdateRequestData


@dataclass
class FastlyAccountUpdateRequestJSON:
    api_key: Union[str, UnsetType] = unset


class FastlyAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_account_update_request_data import FastlyAccountUpdateRequestData

        return {
            "data": (FastlyAccountUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = FastlyAccountUpdateRequestJSON

    def __init__(self_, data: FastlyAccountUpdateRequestData, **kwargs):
        """
        Payload schema when updating a Fastly account.

        :param data: Data object for updating a Fastly account.
        :type data: FastlyAccountUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
