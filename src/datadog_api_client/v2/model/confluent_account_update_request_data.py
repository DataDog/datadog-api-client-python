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


from datadog_api_client.v2.model.confluent_account_update_request_attributes import (
    ConfluentAccountUpdateRequestAttributes,
)

if TYPE_CHECKING:
    from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType


@dataclass
class ConfluentAccountUpdateRequestDataJSON:
    api_key: Union[str, UnsetType] = unset
    api_secret: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class ConfluentAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_account_type import ConfluentAccountType

        return {
            "attributes": (ConfluentAccountUpdateRequestAttributes,),
            "type": (ConfluentAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = ConfluentAccountUpdateRequestDataJSON

    def __init__(self_, attributes: ConfluentAccountUpdateRequestAttributes, type: ConfluentAccountType, **kwargs):
        """
        Data object for updating a Confluent account.

        :param attributes: Attributes object for updating a Confluent account.
        :type attributes: ConfluentAccountUpdateRequestAttributes

        :param type: The JSON:API type for this API. Should always be ``confluent-cloud-accounts``.
        :type type: ConfluentAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
