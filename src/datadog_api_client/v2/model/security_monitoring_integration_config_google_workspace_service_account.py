# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringIntegrationConfigGoogleWorkspaceServiceAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "client_email": (str,),
            "private_key": (str,),
            "project_id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "client_email": "client_email",
        "private_key": "private_key",
        "project_id": "project_id",
        "type": "type",
    }

    def __init__(self_, client_email: str, private_key: str, project_id: str, type: str, **kwargs):
        """
        The Google Cloud service account JSON used to authenticate against the Google Workspace Admin SDK. Additional keys beyond those documented are preserved.

        :param client_email: The service account client email.
        :type client_email: str

        :param private_key: The service account private key.
        :type private_key: str

        :param project_id: The Google Cloud project ID that owns the service account.
        :type project_id: str

        :param type: The service account type. Must be ``service_account``.
        :type type: str
        """
        super().__init__(kwargs)

        self_.client_email = client_email
        self_.private_key = private_key
        self_.project_id = project_id
        self_.type = type
