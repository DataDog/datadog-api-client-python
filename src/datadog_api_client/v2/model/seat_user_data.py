# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.seat_user_data_attributes import SeatUserDataAttributes
    from datadog_api_client.v2.model.seat_user_data_type import SeatUserDataType


class SeatUserData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.seat_user_data_attributes import SeatUserDataAttributes
        from datadog_api_client.v2.model.seat_user_data_type import SeatUserDataType

        return {
            "attributes": (SeatUserDataAttributes,),
            "id": (str, none_type),
            "type": (SeatUserDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SeatUserDataAttributes, UnsetType] = unset,
        id: Union[str, none_type, UnsetType] = unset,
        type: Union[SeatUserDataType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: SeatUserDataAttributes, optional

        :param id: The ID of the seat user.
        :type id: str, none_type, optional

        :param type: Seat users resource type.
        :type type: SeatUserDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
