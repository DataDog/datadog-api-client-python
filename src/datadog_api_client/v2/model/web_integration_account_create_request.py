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
    from datadog_api_client.v2.model.web_integration_account_create_request_data import (
        WebIntegrationAccountCreateRequestData,
    )


class WebIntegrationAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_create_request_data import (
            WebIntegrationAccountCreateRequestData,
        )

        return {
            "data": (WebIntegrationAccountCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: WebIntegrationAccountCreateRequestData, **kwargs):
        """
        Payload for creating a web integration account.

        :param data: Data object for creating a web integration account.
        :type data: WebIntegrationAccountCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
