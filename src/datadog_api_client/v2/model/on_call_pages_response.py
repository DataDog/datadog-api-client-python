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
    from datadog_api_client.v2.model.schedules_response_meta import SchedulesResponseMeta
    from datadog_api_client.v2.model.schedule_user import ScheduleUser
    from datadog_api_client.v2.model.team_reference import TeamReference
    from datadog_api_client.v2.model.on_call_page_scheduled_action import OnCallPageScheduledAction
    from datadog_api_client.v2.model.on_call_page_link import OnCallPageLink


class OnCallPagesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_data import OnCallPageData
        from datadog_api_client.v2.model.on_call_pages_included import OnCallPagesIncluded
        from datadog_api_client.v2.model.schedules_response_meta import SchedulesResponseMeta

        return {
            "data": ([OnCallPageData],),
            "included": ([OnCallPagesIncluded],),
            "meta": (SchedulesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[OnCallPageData],
        included: Union[
            List[Union[OnCallPagesIncluded, ScheduleUser, TeamReference, OnCallPageScheduledAction, OnCallPageLink]],
            UnsetType,
        ] = unset,
        meta: Union[SchedulesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A list of On-Call Pages with pagination metadata and related included resources.

        :param data: A list of pages.
        :type data: [OnCallPageData]

        :param included: Resources related to the pages, such as users, teams, and scheduled actions.
        :type included: [OnCallPagesIncluded], optional

        :param meta: Metadata that is included in the response when listing On-Call resources.
        :type meta: SchedulesResponseMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
