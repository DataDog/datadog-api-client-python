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


from datadog_api_client.v2.model.fastly_service_attributes import FastlyServiceAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.fastly_service_type import FastlyServiceType


@dataclass
class FastlyServiceDataJSON:
    id: str
    tags: Union[List[str], UnsetType] = unset


class FastlyServiceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_service_type import FastlyServiceType

        return {
            "attributes": (FastlyServiceAttributes,),
            "id": (str,),
            "type": (FastlyServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = FastlyServiceDataJSON

    def __init__(
        self_, id: str, type: FastlyServiceType, attributes: Union[FastlyServiceAttributes, UnsetType] = unset, **kwargs
    ):
        """
        Data object for Fastly service requests.

        :param attributes: Attributes object for Fastly service requests.
        :type attributes: FastlyServiceAttributes, optional

        :param id: The ID of the Fastly service.
        :type id: str

        :param type: The JSON:API type for this API. Should always be ``fastly-services``.
        :type type: FastlyServiceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
