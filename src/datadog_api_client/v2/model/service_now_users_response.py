# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_user_data import ServiceNowUserData


class ServiceNowUsersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_user_data import ServiceNowUserData

        return {
            "data": ([ServiceNowUserData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[ServiceNowUserData], **kwargs):
        """
        Response containing ServiceNow users

        :param data: Array of ServiceNow user data objects
        :type data: [ServiceNowUserData]
        """
        super().__init__(kwargs)

        self_.data = data
