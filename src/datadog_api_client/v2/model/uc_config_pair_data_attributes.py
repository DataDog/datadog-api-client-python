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
    from datadog_api_client.v2.model.uc_config_pair_data_attributes_configs_items import (
        UCConfigPairDataAttributesConfigsItems,
    )


class UCConfigPairDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.uc_config_pair_data_attributes_configs_items import (
            UCConfigPairDataAttributesConfigsItems,
        )

        return {
            "configs": ([UCConfigPairDataAttributesConfigsItems],),
        }

    attribute_map = {
        "configs": "configs",
    }

    def __init__(self_, configs: Union[List[UCConfigPairDataAttributesConfigsItems], UnsetType] = unset, **kwargs):
        """
        The definition of ``UCConfigPairDataAttributes`` object.

        :param configs: The ``attributes`` ``configs``.
        :type configs: [UCConfigPairDataAttributesConfigsItems], optional
        """
        if configs is not unset:
            kwargs["configs"] = configs
        super().__init__(kwargs)
