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


from datadog_api_client.v2.model.fastly_service import FastlyService
from datadog_api_client.v2.model.fastly_account_create_request_attributes import FastlyAccountCreateRequestAttributes
from datadog_api_client.v2.model.fastly_service import FastlyService

if TYPE_CHECKING:
    from datadog_api_client.v2.model.fastly_account_type import FastlyAccountType


@dataclass
class FastlyAccountCreateRequestDataJSON:
    api_key: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    services: Union[List[FastlyService], UnsetType] = unset


class FastlyAccountCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_account_type import FastlyAccountType

        return {
            "attributes": (FastlyAccountCreateRequestAttributes,),
            "type": (FastlyAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = FastlyAccountCreateRequestDataJSON

    def __init__(self_, attributes: FastlyAccountCreateRequestAttributes, type: FastlyAccountType, **kwargs):
        """
        Data object for creating a Fastly account.

        :param attributes: Attributes object for creating a Fastly account.
        :type attributes: FastlyAccountCreateRequestAttributes

        :param type: The JSON:API type for this API. Should always be ``fastly-accounts``.
        :type type: FastlyAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
