# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthCredentials(ModelNormal):
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

    def __init__(self_, fingerprint: str, private_key: str, **kwargs):
        """
        The auth credentials of the user. Consists of a public key fingerprint and private key.

        :param fingerprint: The public key fingerprint.
        :type fingerprint: str

        :param private_key: The ``RSA`` private key in ``PEM`` format.
        :type private_key: str
        """
        super().__init__(kwargs)

        self_.fingerprint = fingerprint
        self_.private_key = private_key
