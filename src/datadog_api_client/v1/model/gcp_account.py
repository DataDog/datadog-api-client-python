# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
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
            "cloud_run_revision_filters": ([str],),
            "errors": ([str],),
            "host_filters": (str,),
            "is_cspm_enabled": (bool,),
            "is_security_command_center_enabled": (bool,),
            "private_key": (str,),
            "private_key_id": (str,),
            "project_id": (str,),
            "resource_collection_enabled": (bool,),
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
        "cloud_run_revision_filters": "cloud_run_revision_filters",
        "errors": "errors",
        "host_filters": "host_filters",
        "is_cspm_enabled": "is_cspm_enabled",
        "is_security_command_center_enabled": "is_security_command_center_enabled",
        "private_key": "private_key",
        "private_key_id": "private_key_id",
        "project_id": "project_id",
        "resource_collection_enabled": "resource_collection_enabled",
        "token_uri": "token_uri",
        "type": "type",
    }

    def __init__(
        self_,
        auth_provider_x509_cert_url: Union[str, UnsetType] = unset,
        auth_uri: Union[str, UnsetType] = unset,
        automute: Union[bool, UnsetType] = unset,
        client_email: Union[str, UnsetType] = unset,
        client_id: Union[str, UnsetType] = unset,
        client_x509_cert_url: Union[str, UnsetType] = unset,
        cloud_run_revision_filters: Union[List[str], UnsetType] = unset,
        errors: Union[List[str], UnsetType] = unset,
        host_filters: Union[str, UnsetType] = unset,
        is_cspm_enabled: Union[bool, UnsetType] = unset,
        is_security_command_center_enabled: Union[bool, UnsetType] = unset,
        private_key: Union[str, UnsetType] = unset,
        private_key_id: Union[str, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        token_uri: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
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

        :param cloud_run_revision_filters: Limit the Cloud Run revisions that are pulled into Datadog by using tags.
            Only Cloud Run revision resources that apply to specified filters are imported into Datadog.
        :type cloud_run_revision_filters: [str], optional

        :param errors: An array of errors.
        :type errors: [str], optional

        :param host_filters: Limit the GCE instances that are pulled into Datadog by using tags.
            Only hosts that match one of the defined tags are imported into Datadog.
        :type host_filters: str, optional

        :param is_cspm_enabled: When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
        :type is_cspm_enabled: bool, optional

        :param is_security_command_center_enabled: When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
        :type is_security_command_center_enabled: bool, optional

        :param private_key: Your private key name found in your JSON service account key.
        :type private_key: str, optional

        :param private_key_id: Your private key ID found in your JSON service account key.
        :type private_key_id: str, optional

        :param project_id: Your Google Cloud project ID found in your JSON service account key.
        :type project_id: str, optional

        :param resource_collection_enabled: When enabled, Datadog scans for all resources in your GCP environment.
        :type resource_collection_enabled: bool, optional

        :param token_uri: Should be ``https://accounts.google.com/o/oauth2/token``.
        :type token_uri: str, optional

        :param type: The value for service_account found in your JSON service account key.
        :type type: str, optional
        """
        if auth_provider_x509_cert_url is not unset:
            kwargs["auth_provider_x509_cert_url"] = auth_provider_x509_cert_url
        if auth_uri is not unset:
            kwargs["auth_uri"] = auth_uri
        if automute is not unset:
            kwargs["automute"] = automute
        if client_email is not unset:
            kwargs["client_email"] = client_email
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if client_x509_cert_url is not unset:
            kwargs["client_x509_cert_url"] = client_x509_cert_url
        if cloud_run_revision_filters is not unset:
            kwargs["cloud_run_revision_filters"] = cloud_run_revision_filters
        if errors is not unset:
            kwargs["errors"] = errors
        if host_filters is not unset:
            kwargs["host_filters"] = host_filters
        if is_cspm_enabled is not unset:
            kwargs["is_cspm_enabled"] = is_cspm_enabled
        if is_security_command_center_enabled is not unset:
            kwargs["is_security_command_center_enabled"] = is_security_command_center_enabled
        if private_key is not unset:
            kwargs["private_key"] = private_key
        if private_key_id is not unset:
            kwargs["private_key_id"] = private_key_id
        if project_id is not unset:
            kwargs["project_id"] = project_id
        if resource_collection_enabled is not unset:
            kwargs["resource_collection_enabled"] = resource_collection_enabled
        if token_uri is not unset:
            kwargs["token_uri"] = token_uri
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
