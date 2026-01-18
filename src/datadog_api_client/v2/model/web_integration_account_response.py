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
    from datadog_api_client.v2.model.web_integration_account_response_data import WebIntegrationAccountResponseData


class WebIntegrationAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_response_data import WebIntegrationAccountResponseData

        return {
            "data": (WebIntegrationAccountResponseData,),
            "integration_name": (str,),
        }

    attribute_map = {
        "data": "data",
        "integration_name": "integration_name",
    }

    def __init__(
        self_,
        data: Union[WebIntegrationAccountResponseData, UnsetType] = unset,
        integration_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a single web integration account.

        :param data: Data object for a web integration account response.
        :type data: WebIntegrationAccountResponseData, optional

        :param integration_name: The name of the integration.
        :type integration_name: str, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if integration_name is not unset:
            kwargs["integration_name"] = integration_name
        super().__init__(kwargs)
