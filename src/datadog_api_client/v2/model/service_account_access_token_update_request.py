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
    from datadog_api_client.v2.model.service_account_access_token_update_data import ServiceAccountAccessTokenUpdateData


class ServiceAccountAccessTokenUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_account_access_token_update_data import (
            ServiceAccountAccessTokenUpdateData,
        )

        return {
            "data": (ServiceAccountAccessTokenUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ServiceAccountAccessTokenUpdateData, **kwargs):
        """
        Request used to update a service account access token.

        :param data: Object used to update a service account access token.
        :type data: ServiceAccountAccessTokenUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
