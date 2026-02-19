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
    from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
    from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType


class ChangeRequestUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
        from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType

        return {
            "change_request_plan": (str,),
            "change_request_risk": (ChangeRequestRiskLevel,),
            "change_request_type": (ChangeRequestChangeType,),
            "end_date": (datetime,),
            "id": (str,),
            "start_date": (datetime,),
        }

    attribute_map = {
        "change_request_plan": "change_request_plan",
        "change_request_risk": "change_request_risk",
        "change_request_type": "change_request_type",
        "end_date": "end_date",
        "id": "id",
        "start_date": "start_date",
    }

    def __init__(
        self_,
        change_request_plan: Union[str, UnsetType] = unset,
        change_request_risk: Union[ChangeRequestRiskLevel, UnsetType] = unset,
        change_request_type: Union[ChangeRequestChangeType, UnsetType] = unset,
        end_date: Union[datetime, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a change request.

        :param change_request_plan: The plan associated with the change request.
        :type change_request_plan: str, optional

        :param change_request_risk: The risk level of the change request.
        :type change_request_risk: ChangeRequestRiskLevel, optional

        :param change_request_type: The type of the change request.
        :type change_request_type: ChangeRequestChangeType, optional

        :param end_date: The planned end date of the change request.
        :type end_date: datetime, optional

        :param id: The identifier of the change request to update.
        :type id: str, optional

        :param start_date: The planned start date of the change request.
        :type start_date: datetime, optional
        """
        if change_request_plan is not unset:
            kwargs["change_request_plan"] = change_request_plan
        if change_request_risk is not unset:
            kwargs["change_request_risk"] = change_request_risk
        if change_request_type is not unset:
            kwargs["change_request_type"] = change_request_type
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if id is not unset:
            kwargs["id"] = id
        if start_date is not unset:
            kwargs["start_date"] = start_date
        super().__init__(kwargs)
