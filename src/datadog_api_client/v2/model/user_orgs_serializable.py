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
    from datadog_api_client.v2.model.user_orgs_serializable_attributes import UserOrgsSerializableAttributes
    from datadog_api_client.v2.model.user_orgs_serializable_type import UserOrgsSerializableType


class UserOrgsSerializable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_orgs_serializable_attributes import UserOrgsSerializableAttributes
        from datadog_api_client.v2.model.user_orgs_serializable_type import UserOrgsSerializableType

        return {
            "attributes": (UserOrgsSerializableAttributes,),
            "id": (str,),
            "type": (UserOrgsSerializableType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UserOrgsSerializableType,
        attributes: Union[UserOrgsSerializableAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UserOrgsSerializable`` object.

        :param attributes: The definition of ``UserOrgsSerializableAttributes`` object.
        :type attributes: UserOrgsSerializableAttributes, optional

        :param id: The ``UserOrgsSerializable`` ``id``.
        :type id: str, optional

        :param type: The definition of ``UserOrgsSerializableType`` object.
        :type type: UserOrgsSerializableType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
