# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GCPSTSDelegateAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "delegate_account_email": (str,),
        }

    attribute_map = {
        "delegate_account_email": "delegate_account_email",
    }

    def __init__(self_, delegate_account_email: Union[str, UnsetType] = unset, **kwargs):
        """
        Your delegate account attributes.

        :param delegate_account_email: Your organization's Datadog principal email address.
        :type delegate_account_email: str, optional
        """
        if delegate_account_email is not unset:
            kwargs["delegate_account_email"] = delegate_account_email
        super().__init__(kwargs)
