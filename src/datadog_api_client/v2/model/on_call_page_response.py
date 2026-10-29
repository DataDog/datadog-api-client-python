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
    from datadog_api_client.v2.model.on_call_page_data import OnCallPageData
    from datadog_api_client.v2.model.on_call_pages_included import OnCallPagesIncluded
    from datadog_api_client.v2.model.schedule_user import ScheduleUser
    from datadog_api_client.v2.model.team_reference import TeamReference
    from datadog_api_client.v2.model.on_call_page_scheduled_action import OnCallPageScheduledAction
    from datadog_api_client.v2.model.on_call_page_link import OnCallPageLink


class OnCallPageResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_data import OnCallPageData
        from datadog_api_client.v2.model.on_call_pages_included import OnCallPagesIncluded

        return {
            "data": (OnCallPageData,),
            "included": ([OnCallPagesIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: OnCallPageData,
        included: Union[
            List[Union[OnCallPagesIncluded, ScheduleUser, TeamReference, OnCallPageScheduledAction, OnCallPageLink]],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        A single On-Call Page with its related included resources.

        :param data: An On-Call Page.
        :type data: OnCallPageData

        :param included: Resources related to the Page, such as users, teams, scheduled actions, and links.
        :type included: [OnCallPagesIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
