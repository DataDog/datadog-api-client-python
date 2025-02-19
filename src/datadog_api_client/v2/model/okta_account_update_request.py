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
    from datadog_api_client.v2.model.okta_account_update_request_data import OktaAccountUpdateRequestData


class OktaAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.okta_account_update_request_data import OktaAccountUpdateRequestData

        return {
            "data": (OktaAccountUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OktaAccountUpdateRequestData, **kwargs):
        """
        Payload schema when updating an Okta account.

        :param data: Data object for updating an Okta account.
        :type data: OktaAccountUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
