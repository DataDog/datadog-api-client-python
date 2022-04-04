# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_basic_auth_web import SyntheticsBasicAuthWeb
    from datadog_api_client.v1.model.synthetics_basic_auth_sigv4 import SyntheticsBasicAuthSigv4
    from datadog_api_client.v1.model.synthetics_basic_auth_ntlm import SyntheticsBasicAuthNTLM

    globals()["SyntheticsBasicAuthWeb"] = SyntheticsBasicAuthWeb
    globals()["SyntheticsBasicAuthSigv4"] = SyntheticsBasicAuthSigv4
    globals()["SyntheticsBasicAuthNTLM"] = SyntheticsBasicAuthNTLM


class SyntheticsBasicAuth(ModelComposed):
    def __init__(self, *args, **kwargs):
        """
        Object to handle basic authentication when performing the test.

        :param password: Password to use for the basic authentication.
        :type password: str

        :param type: The type of basic authentication to use when performing the test.
        :type type: SyntheticsBasicAuthWebType, optional

        :param username: Username to use for the basic authentication.
        :type username: str

        :param access_key: Access key for the `SIGV4` authentication.
        :type access_key: str

        :param region: Region for the `SIGV4` authentication.
        :type region: str, optional

        :param secret_key: Secret key for the `SIGV4` authentication.
        :type secret_key: str

        :param service_name: Service name for the `SIGV4` authentication.
        :type service_name: str, optional

        :param session_token: Session token for the `SIGV4` authentication.
        :type session_token: str, optional

        :param domain: Domain for the authentication to use when performing the test.
        :type domain: str, optional

        :param workstation: Workstation for the authentication to use when performing the test.
        :type workstation: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBasicAuth, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                SyntheticsBasicAuthWeb,
                SyntheticsBasicAuthSigv4,
                SyntheticsBasicAuthNTLM,
            ],
        }
