# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_status_page_notice_update_data import IncidentStatusPageNoticeUpdateData


class IncidentStatusPageNoticeUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_status_page_notice_update_data import (
            IncidentStatusPageNoticeUpdateData,
        )

        return {
            "data": (IncidentStatusPageNoticeUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentStatusPageNoticeUpdateData, **kwargs):
        """
        Request to update a status page notice.

        :param data: Data for updating a status page notice.
        :type data: IncidentStatusPageNoticeUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
