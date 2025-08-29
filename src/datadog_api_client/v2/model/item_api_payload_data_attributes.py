# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.item_api_payload_data_attributes_value import ItemApiPayloadDataAttributesValue


class ItemApiPayloadDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.item_api_payload_data_attributes_value import ItemApiPayloadDataAttributesValue

        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "org_id": (int,),
            "primary_column_name": (str,),
            "signature": (str,),
            "store_id": (str,),
            "value": (ItemApiPayloadDataAttributesValue,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "org_id": "org_id",
        "primary_column_name": "primary_column_name",
        "signature": "signature",
        "store_id": "store_id",
        "value": "value",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        primary_column_name: Union[str, UnsetType] = unset,
        signature: Union[str, UnsetType] = unset,
        store_id: Union[str, UnsetType] = unset,
        value: Union[ItemApiPayloadDataAttributesValue, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ItemApiPayloadDataAttributes`` object.

        :param created_at: The ``attributes`` ``created_at``.
        :type created_at: datetime, optional

        :param modified_at: The ``attributes`` ``modified_at``.
        :type modified_at: datetime, optional

        :param org_id: The ``attributes`` ``org_id``.
        :type org_id: int, optional

        :param primary_column_name: The ``attributes`` ``primary_column_name``.
        :type primary_column_name: str, optional

        :param signature: The ``attributes`` ``signature``.
        :type signature: str, optional

        :param store_id: The ``attributes`` ``store_id``.
        :type store_id: str, optional

        :param value: The ``attributes`` ``value``.
        :type value: ItemApiPayloadDataAttributesValue, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if primary_column_name is not unset:
            kwargs["primary_column_name"] = primary_column_name
        if signature is not unset:
            kwargs["signature"] = signature
        if store_id is not unset:
            kwargs["store_id"] = store_id
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
