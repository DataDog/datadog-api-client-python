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
    from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes import (
        ArbitraryCostUpsertRequestDataAttributes,
    )
    from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_type import ArbitraryCostUpsertRequestDataType


class ArbitraryCostUpsertRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes import (
            ArbitraryCostUpsertRequestDataAttributes,
        )
        from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_type import (
            ArbitraryCostUpsertRequestDataType,
        )

        return {
            "attributes": (ArbitraryCostUpsertRequestDataAttributes,),
            "id": (str,),
            "type": (ArbitraryCostUpsertRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ArbitraryCostUpsertRequestDataType,
        attributes: Union[ArbitraryCostUpsertRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryCostUpsertRequestData`` object.

        :param attributes: The definition of ``ArbitraryCostUpsertRequestDataAttributes`` object.
        :type attributes: ArbitraryCostUpsertRequestDataAttributes, optional

        :param id: The ``ArbitraryCostUpsertRequestData`` ``id``.
        :type id: str, optional

        :param type: Upsert arbitrary rule resource type.
        :type type: ArbitraryCostUpsertRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
