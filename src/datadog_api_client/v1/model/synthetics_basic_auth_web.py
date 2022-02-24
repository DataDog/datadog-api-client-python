# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_basic_auth_web_type import SyntheticsBasicAuthWebType

    globals()["SyntheticsBasicAuthWebType"] = SyntheticsBasicAuthWebType


class SyntheticsBasicAuthWeb(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "password": (str,),
            "type": (SyntheticsBasicAuthWebType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    read_only_vars = {}

    def __init__(self, password, type, username, *args, **kwargs):
        """
        Object to handle basic authentication when performing the test.

        :param password: Password to use for the basic authentication.
        :type password: str

        :param type: The type of basic authentication to use when performing the test.
        :type type: SyntheticsBasicAuthWebType

        :param username: Username to use for the basic authentication.
        :type username: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.password = password
        self.type = type
        self.username = username

    @classmethod
    def _from_openapi_data(cls, password, type, username, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBasicAuthWeb, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.password = password
        self.type = type
        self.username = username
        return self
