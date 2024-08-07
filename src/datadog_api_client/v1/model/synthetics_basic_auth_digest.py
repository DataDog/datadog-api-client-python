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
    from datadog_api_client.v1.model.synthetics_basic_auth_digest_type import SyntheticsBasicAuthDigestType


class SyntheticsBasicAuthDigest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth_digest_type import SyntheticsBasicAuthDigestType

        return {
            "password": (str,),
            "type": (SyntheticsBasicAuthDigestType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(self_, password: str, type: SyntheticsBasicAuthDigestType, username: str, **kwargs):
        """
        Object to handle digest authentication when performing the test.

        :param password: Password to use for the digest authentication.
        :type password: str

        :param type: The type of basic authentication to use when performing the test.
        :type type: SyntheticsBasicAuthDigestType

        :param username: Username to use for the digest authentication.
        :type username: str
        """
        super().__init__(kwargs)

        self_.password = password
        self_.type = type
        self_.username = username
