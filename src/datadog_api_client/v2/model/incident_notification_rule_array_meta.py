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
    from datadog_api_client.v2.model.incident_notification_rule_array_meta_page import (
        IncidentNotificationRuleArrayMetaPage,
    )


class IncidentNotificationRuleArrayMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_rule_array_meta_page import (
            IncidentNotificationRuleArrayMetaPage,
        )

        return {
            "pagination": (IncidentNotificationRuleArrayMetaPage,),
        }

    attribute_map = {
        "pagination": "pagination",
    }

    def __init__(self_, pagination: Union[IncidentNotificationRuleArrayMetaPage, UnsetType] = unset, **kwargs):
        """
        Response metadata.

        :param pagination: Pagination metadata.
        :type pagination: IncidentNotificationRuleArrayMetaPage, optional
        """
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)
