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
    from datadog_api_client.v2.model.assign_seats_user_response_data_attributes import (
        AssignSeatsUserResponseDataAttributes,
    )
    from datadog_api_client.v2.model.seat_assignments_data_type import SeatAssignmentsDataType


class AssignSeatsUserResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.assign_seats_user_response_data_attributes import (
            AssignSeatsUserResponseDataAttributes,
        )
        from datadog_api_client.v2.model.seat_assignments_data_type import SeatAssignmentsDataType

        return {
            "attributes": (AssignSeatsUserResponseDataAttributes,),
            "id": (str,),
            "type": (SeatAssignmentsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AssignSeatsUserResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SeatAssignmentsDataType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: AssignSeatsUserResponseDataAttributes, optional

        :param id: The ID of the assign seats user response.
        :type id: str, optional

        :param type: Seat assignments resource type.
        :type type: SeatAssignmentsDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
