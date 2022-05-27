# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBasicAuthSigv4(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth_sigv4_type import SyntheticsBasicAuthSigv4Type

        return {
            "access_key": (str,),
            "region": (str,),
            "secret_key": (str,),
            "service_name": (str,),
            "session_token": (str,),
            "type": (SyntheticsBasicAuthSigv4Type,),
        }

    attribute_map = {
        "access_key": "accessKey",
        "region": "region",
        "secret_key": "secretKey",
        "service_name": "serviceName",
        "session_token": "sessionToken",
        "type": "type",
    }

    def __init__(self, access_key, secret_key, type, *args, **kwargs):
        """
        Object to handle ``SIGV4`` authentication when performing the test.

        :param access_key: Access key for the ``SIGV4`` authentication.
        :type access_key: str

        :param region: Region for the ``SIGV4`` authentication.
        :type region: str, optional

        :param secret_key: Secret key for the ``SIGV4`` authentication.
        :type secret_key: str

        :param service_name: Service name for the ``SIGV4`` authentication.
        :type service_name: str, optional

        :param session_token: Session token for the ``SIGV4`` authentication.
        :type session_token: str, optional

        :param type: The type of authentication to use when performing the test.
        :type type: SyntheticsBasicAuthSigv4Type
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.access_key = access_key
        self.secret_key = secret_key
        self.type = type

    @classmethod
    def _from_openapi_data(cls, access_key, secret_key, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBasicAuthSigv4, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.access_key = access_key
        self.secret_key = secret_key
        self.type = type
        return self
