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
    from datadog_api_client.v2.model.incident_notification_template_array_meta_page import (
        IncidentNotificationTemplateArrayMetaPage,
    )


class IncidentNotificationTemplateArrayMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_template_array_meta_page import (
            IncidentNotificationTemplateArrayMetaPage,
        )

        return {
            "page": (IncidentNotificationTemplateArrayMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[IncidentNotificationTemplateArrayMetaPage, UnsetType] = unset, **kwargs):
        """
        Response metadata.

        :param page: Pagination metadata.
        :type page: IncidentNotificationTemplateArrayMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
