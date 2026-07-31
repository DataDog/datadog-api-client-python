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
    from datadog_api_client.v2.model.twilio_account_data import TwilioAccountData


class TwilioAccountResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.twilio_account_data import TwilioAccountData

        return {
            "data": (TwilioAccountData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[TwilioAccountData, UnsetType] = unset, **kwargs):
        """
        Response payload for a single Twilio integration account.

        :param data: Data envelope of a Twilio integration account, including server-assigned identity.
        :type data: TwilioAccountData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
