# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_basic_auth_ntlm_type import SyntheticsBasicAuthNTLMType

    globals()["SyntheticsBasicAuthNTLMType"] = SyntheticsBasicAuthNTLMType


class SyntheticsBasicAuthNTLM(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "domain": (str,),
            "password": (str,),
            "type": (SyntheticsBasicAuthNTLMType,),
            "username": (str,),
            "workstation": (str,),
        }

    attribute_map = {
        "type": "type",
        "domain": "domain",
        "password": "password",
        "username": "username",
        "workstation": "workstation",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """SyntheticsBasicAuthNTLM - a model defined in OpenAPI

        Args:
            type (SyntheticsBasicAuthNTLMType):

        Keyword Args:
            domain (str): [optional] Domain for the authentication to use when performing the test.
            password (str): [optional] Password for the authentication to use when performing the test.
            username (str): [optional] Username for the authentication to use when performing the test.
            workstation (str): [optional] Workstation for the authentication to use when performing the test.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBasicAuthNTLM, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
