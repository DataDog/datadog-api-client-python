# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.azure_uc_config_pair_attributes import AzureUCConfigPairAttributes
    from datadog_api_client.v2.model.azure_uc_config_pair_type import AzureUCConfigPairType


class AzureUCConfigPair(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_uc_config_pair_attributes import AzureUCConfigPairAttributes
        from datadog_api_client.v2.model.azure_uc_config_pair_type import AzureUCConfigPairType

        return {
            "attributes": (AzureUCConfigPairAttributes,),
            "id": (int,),
            "type": (AzureUCConfigPairType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AzureUCConfigPairAttributes,
        type: AzureUCConfigPairType,
        id: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Azure config pair.

        :param attributes: Attributes for Azure config pair.
        :type attributes: AzureUCConfigPairAttributes

        :param id: The ID of Cloud Cost Management account.
        :type id: int, optional

        :param type: Type of Azure config pair.
        :type type: AzureUCConfigPairType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
