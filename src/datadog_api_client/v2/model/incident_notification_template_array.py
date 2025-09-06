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
    from datadog_api_client.v2.model.incident_notification_template_response_data import (
        IncidentNotificationTemplateResponseData,
    )
    from datadog_api_client.v2.model.incident_notification_template_included_items import (
        IncidentNotificationTemplateIncludedItems,
    )
    from datadog_api_client.v2.model.incident_notification_template_array_meta import (
        IncidentNotificationTemplateArrayMeta,
    )
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.incident_type_object import IncidentTypeObject


class IncidentNotificationTemplateArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_template_response_data import (
            IncidentNotificationTemplateResponseData,
        )
        from datadog_api_client.v2.model.incident_notification_template_included_items import (
            IncidentNotificationTemplateIncludedItems,
        )
        from datadog_api_client.v2.model.incident_notification_template_array_meta import (
            IncidentNotificationTemplateArrayMeta,
        )

        return {
            "data": ([IncidentNotificationTemplateResponseData],),
            "included": ([IncidentNotificationTemplateIncludedItems],),
            "meta": (IncidentNotificationTemplateArrayMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[IncidentNotificationTemplateResponseData],
        included: Union[
            List[Union[IncidentNotificationTemplateIncludedItems, User, IncidentTypeObject]], UnsetType
        ] = unset,
        meta: Union[IncidentNotificationTemplateArrayMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response with notification templates.

        :param data: The ``NotificationTemplateArray`` ``data``.
        :type data: [IncidentNotificationTemplateResponseData]

        :param included: Related objects that are included in the response.
        :type included: [IncidentNotificationTemplateIncludedItems], optional

        :param meta: Response metadata.
        :type meta: IncidentNotificationTemplateArrayMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
