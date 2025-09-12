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
    from datadog_api_client.v2.model.incident_notification_rule_response_data import (
        IncidentNotificationRuleResponseData,
    )
    from datadog_api_client.v2.model.incident_notification_rule_included_items import (
        IncidentNotificationRuleIncludedItems,
    )
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.incident_type_object import IncidentTypeObject
    from datadog_api_client.v2.model.incident_notification_template_object import IncidentNotificationTemplateObject


class IncidentNotificationRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_rule_response_data import (
            IncidentNotificationRuleResponseData,
        )
        from datadog_api_client.v2.model.incident_notification_rule_included_items import (
            IncidentNotificationRuleIncludedItems,
        )

        return {
            "data": (IncidentNotificationRuleResponseData,),
            "included": ([IncidentNotificationRuleIncludedItems],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: IncidentNotificationRuleResponseData,
        included: Union[
            List[
                Union[
                    IncidentNotificationRuleIncludedItems, User, IncidentTypeObject, IncidentNotificationTemplateObject
                ]
            ],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Response with a notification rule.

        :param data: Notification rule data from a response.
        :type data: IncidentNotificationRuleResponseData

        :param included: Related objects that are included in the response.
        :type included: [IncidentNotificationRuleIncludedItems], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
