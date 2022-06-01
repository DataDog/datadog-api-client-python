# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBasicAuthNTLM(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth_ntlm_type import SyntheticsBasicAuthNTLMType

        return {
            "domain": (str,),
            "password": (str,),
            "type": (SyntheticsBasicAuthNTLMType,),
            "username": (str,),
            "workstation": (str,),
        }

    attribute_map = {
        "domain": "domain",
        "password": "password",
        "type": "type",
        "username": "username",
        "workstation": "workstation",
    }

    def __init__(self, type, *args, **kwargs):
        """
        Object to handle ``NTLM`` authentication when performing the test.

        :param domain: Domain for the authentication to use when performing the test.
        :type domain: str, optional

        :param password: Password for the authentication to use when performing the test.
        :type password: str, optional

        :param type: The type of authentication to use when performing the test.
        :type type: SyntheticsBasicAuthNTLMType

        :param username: Username for the authentication to use when performing the test.
        :type username: str, optional

        :param workstation: Workstation for the authentication to use when performing the test.
        :type workstation: str, optional
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
