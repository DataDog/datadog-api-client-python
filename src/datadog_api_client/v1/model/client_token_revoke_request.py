# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ClientTokenRevokeRequest(ModelNormal):
    validations = {
        "hash": {
            "max_length": 35,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "hash": (str,),
        }

    attribute_map = {
        "hash": "hash",
    }

    def __init__(self_, hash: str, **kwargs):
        """
        Request to revoke a client token.

        :param hash: Hash value of the client token to revoke.
        :type hash: str
        """
        super().__init__(kwargs)

        self_.hash = hash
