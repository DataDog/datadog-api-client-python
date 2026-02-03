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


class CreateTenancyConfigDataAttributesAuthCredentials(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "fingerprint": (str,),
            "private_key": (str,),
        }

    attribute_map = {
        "fingerprint": "fingerprint",
        "private_key": "private_key",
    }

    def __init__(self_, private_key: str, fingerprint: Union[str, UnsetType] = unset, **kwargs):
        """


        :param fingerprint:
        :type fingerprint: str, optional

        :param private_key:
        :type private_key: str
        """
        if fingerprint is not unset:
            kwargs["fingerprint"] = fingerprint
        super().__init__(kwargs)

        self_.private_key = private_key
