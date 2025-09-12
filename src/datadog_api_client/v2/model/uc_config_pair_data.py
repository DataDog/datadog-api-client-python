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
    from datadog_api_client.v2.model.uc_config_pair_data_attributes import UCConfigPairDataAttributes
    from datadog_api_client.v2.model.uc_config_pair_data_type import UCConfigPairDataType


class UCConfigPairData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.uc_config_pair_data_attributes import UCConfigPairDataAttributes
        from datadog_api_client.v2.model.uc_config_pair_data_type import UCConfigPairDataType

        return {
            "attributes": (UCConfigPairDataAttributes,),
            "id": (str,),
            "type": (UCConfigPairDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UCConfigPairDataType,
        attributes: Union[UCConfigPairDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UCConfigPairData`` object.

        :param attributes: The definition of ``UCConfigPairDataAttributes`` object.
        :type attributes: UCConfigPairDataAttributes, optional

        :param id: The ``UCConfigPairData`` ``id``.
        :type id: str, optional

        :param type: Azure UC configs resource type.
        :type type: UCConfigPairDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
