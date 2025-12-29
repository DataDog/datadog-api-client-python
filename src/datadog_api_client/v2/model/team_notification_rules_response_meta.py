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
    from datadog_api_client.v2.model.team_notification_rules_response_meta_page import (
        TeamNotificationRulesResponseMetaPage,
    )


class TeamNotificationRulesResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_notification_rules_response_meta_page import (
            TeamNotificationRulesResponseMetaPage,
        )

        return {
            "page": (TeamNotificationRulesResponseMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[TeamNotificationRulesResponseMetaPage, UnsetType] = unset, **kwargs):
        """
        Metadata that is included in the response when querying the team notification rules

        :param page: Metadata related to paging information that is included in the response when querying the team notification rules
        :type page: TeamNotificationRulesResponseMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
