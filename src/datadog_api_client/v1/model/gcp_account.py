# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GCPAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "auth_provider_x509_cert_url": (str,),
            "auth_uri": (str,),
            "automute": (bool,),
            "client_email": (str,),
            "client_id": (str,),
            "client_x509_cert_url": (str,),
            "errors": ([str],),
            "host_filters": (str,),
            "private_key": (str,),
            "private_key_id": (str,),
            "project_id": (str,),
            "token_uri": (str,),
            "type": (str,),
        }

    attribute_map = {
        "auth_provider_x509_cert_url": "auth_provider_x509_cert_url",
        "auth_uri": "auth_uri",
        "automute": "automute",
        "client_email": "client_email",
        "client_id": "client_id",
        "client_x509_cert_url": "client_x509_cert_url",
        "errors": "errors",
        "host_filters": "host_filters",
        "private_key": "private_key",
        "private_key_id": "private_key_id",
        "project_id": "project_id",
        "token_uri": "token_uri",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Your Google Cloud Platform Account.

        :param auth_provider_x509_cert_url: Should be ``https://www.googleapis.com/oauth2/v1/certs``.
        :type auth_provider_x509_cert_url: str, optional

        :param auth_uri: Should be ``https://accounts.google.com/o/oauth2/auth``.
        :type auth_uri: str, optional

        :param automute: Silence monitors for expected GCE instance shutdowns.
        :type automute: bool, optional

        :param client_email: Your email found in your JSON service account key.
        :type client_email: str, optional

        :param client_id: Your ID found in your JSON service account key.
        :type client_id: str, optional

        :param client_x509_cert_url: Should be ``https://www.googleapis.com/robot/v1/metadata/x509/$CLIENT_EMAIL``
            where ``$CLIENT_EMAIL`` is the email found in your JSON service account key.
        :type client_x509_cert_url: str, optional

        :param errors: An array of errors.
        :type errors: [str], optional

        :param host_filters: Limit the GCE instances that are pulled into Datadog by using tags.
            Only hosts that match one of the defined tags are imported into Datadog.
        :type host_filters: str, optional

        :param private_key: Your private key name found in your JSON service account key.
        :type private_key: str, optional

        :param private_key_id: Your private key ID found in your JSON service account key.
        :type private_key_id: str, optional

        :param project_id: Your Google Cloud project ID found in your JSON service account key.
        :type project_id: str, optional

        :param token_uri: Should be ``https://accounts.google.com/o/oauth2/token``.
        :type token_uri: str, optional

        :param type: The value for service_account found in your JSON service account key.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(GCPAccount, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
