# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.azure_uc_config import AzureUCConfig


class AzureUCConfigPairAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_uc_config import AzureUCConfig

        return {
            "configs": ([AzureUCConfig],),
            "id": (int,),
        }

    attribute_map = {
        "configs": "configs",
        "id": "id",
    }

    def __init__(self_, configs: List[AzureUCConfig], id: Union[int, UnsetType] = unset, **kwargs):
        """
        Attributes for Azure config pair.

        :param configs: An Azure config.
        :type configs: [AzureUCConfig]

        :param id: The ID of the Azure config pair.
        :type id: int, optional
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.configs = configs
