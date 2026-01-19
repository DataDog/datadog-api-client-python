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
    from datadog_api_client.v2.model.web_integration_account_update_request_attributes import (
        WebIntegrationAccountUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType


class WebIntegrationAccountUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_update_request_attributes import (
            WebIntegrationAccountUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.web_integration_account_type import WebIntegrationAccountType

        return {
            "attributes": (WebIntegrationAccountUpdateRequestAttributes,),
            "type": (WebIntegrationAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: WebIntegrationAccountType,
        attributes: Union[WebIntegrationAccountUpdateRequestAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a web integration account.

        :param attributes: Attributes for updating a web integration account. All fields are optional -
            only provide the fields you want to update. Partial updates are supported,
            allowing you to modify specific settings or secrets without providing all fields.
        :type attributes: WebIntegrationAccountUpdateRequestAttributes, optional

        :param type: The JSON:API type for web integration accounts.
        :type type: WebIntegrationAccountType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
