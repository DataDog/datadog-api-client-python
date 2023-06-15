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
    from datadog_api_client.v2.model.fastly_service_data import FastlyServiceData


@dataclass
class FastlyServiceRequestJSON:
    id: str
    tags: Union[List[str], UnsetType] = unset


class FastlyServiceRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_service_data import FastlyServiceData

        return {
            "data": (FastlyServiceData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = FastlyServiceRequestJSON

    def __init__(self_, data: FastlyServiceData, **kwargs):
        """
        Payload schema for Fastly service requests.

        :param data: Data object for Fastly service requests.
        :type data: FastlyServiceData
        """
        super().__init__(kwargs)

        self_.data = data
