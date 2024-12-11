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


class AWSAuthConfigKeys(ModelNormal):
    validations = {
        "secret_access_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "access_key_id": (str,),
            "secret_access_key": (str,),
        }

    attribute_map = {
        "access_key_id": "access_key_id",
        "secret_access_key": "secret_access_key",
    }

    def __init__(self_, access_key_id: str, secret_access_key: Union[str, UnsetType] = unset, **kwargs):
        """
        AWS Authentication config to integrate your account using an access key pair.

        :param access_key_id: AWS Access Key ID.
        :type access_key_id: str

        :param secret_access_key: AWS Secret Access Key.
        :type secret_access_key: str, optional
        """
        if secret_access_key is not unset:
            kwargs["secret_access_key"] = secret_access_key
        super().__init__(kwargs)

        self_.access_key_id = access_key_id
