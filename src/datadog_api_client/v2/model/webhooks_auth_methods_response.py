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
    from datadog_api_client.v2.model.webhooks_auth_method_response_data import WebhooksAuthMethodResponseData
    from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_response_data import (
        WebhooksOAuth2ClientCredentialsResponseData,
    )


class WebhooksAuthMethodsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_auth_method_response_data import WebhooksAuthMethodResponseData
        from datadog_api_client.v2.model.webhooks_o_auth2_client_credentials_response_data import (
            WebhooksOAuth2ClientCredentialsResponseData,
        )

        return {
            "data": ([WebhooksAuthMethodResponseData],),
            "included": ([WebhooksOAuth2ClientCredentialsResponseData],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[WebhooksAuthMethodResponseData],
        included: Union[List[WebhooksOAuth2ClientCredentialsResponseData], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of webhooks auth methods.

        :param data: An array of webhooks auth methods.
        :type data: [WebhooksAuthMethodResponseData]

        :param included: Resources related to the auth methods, included when requested via the ``include`` query parameter.
        :type included: [WebhooksOAuth2ClientCredentialsResponseData], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
