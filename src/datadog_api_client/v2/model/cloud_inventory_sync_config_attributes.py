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
    from datadog_api_client.v2.model.cloud_inventory_cloud_provider_id import CloudInventoryCloudProviderId


class CloudInventorySyncConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_inventory_cloud_provider_id import CloudInventoryCloudProviderId

        return {
            "aws_account_id": (str,),
            "aws_bucket_name": (str,),
            "aws_region": (str,),
            "azure_client_id": (str,),
            "azure_container_name": (str,),
            "azure_storage_account_name": (str,),
            "azure_tenant_id": (str,),
            "cloud_provider": (CloudInventoryCloudProviderId,),
            "error": (str,),
            "error_code": (str,),
            "gcp_bucket_name": (str,),
            "gcp_project_id": (str,),
            "gcp_service_account_email": (str,),
            "prefix": (str,),
        }

    attribute_map = {
        "aws_account_id": "aws_account_id",
        "aws_bucket_name": "aws_bucket_name",
        "aws_region": "aws_region",
        "azure_client_id": "azure_client_id",
        "azure_container_name": "azure_container_name",
        "azure_storage_account_name": "azure_storage_account_name",
        "azure_tenant_id": "azure_tenant_id",
        "cloud_provider": "cloud_provider",
        "error": "error",
        "error_code": "error_code",
        "gcp_bucket_name": "gcp_bucket_name",
        "gcp_project_id": "gcp_project_id",
        "gcp_service_account_email": "gcp_service_account_email",
        "prefix": "prefix",
    }
    read_only_vars = {
        "error",
        "error_code",
        "prefix",
    }

    def __init__(
        self_,
        aws_account_id: str,
        aws_bucket_name: str,
        aws_region: str,
        azure_client_id: str,
        azure_container_name: str,
        azure_storage_account_name: str,
        azure_tenant_id: str,
        cloud_provider: CloudInventoryCloudProviderId,
        error: str,
        error_code: str,
        gcp_bucket_name: str,
        gcp_project_id: str,
        gcp_service_account_email: str,
        prefix: str,
        **kwargs,
    ):
        """
        Attributes for a cloud inventory sync configuration. Values beyond ``id`` may be omitted immediately after upsert.

        :param aws_account_id: AWS account ID for the inventory bucket.
        :type aws_account_id: str

        :param aws_bucket_name: AWS S3 bucket name for inventory files.
        :type aws_bucket_name: str

        :param aws_region: AWS Region for the inventory bucket.
        :type aws_region: str

        :param azure_client_id: Azure AD application (client) ID.
        :type azure_client_id: str

        :param azure_container_name: Azure blob container name.
        :type azure_container_name: str

        :param azure_storage_account_name: Azure storage account name.
        :type azure_storage_account_name: str

        :param azure_tenant_id: Azure AD tenant ID.
        :type azure_tenant_id: str

        :param cloud_provider: Cloud provider for this sync configuration ( ``aws`` , ``gcp`` , or ``azure`` ). For requests, must match the provider block supplied under ``attributes``.
        :type cloud_provider: CloudInventoryCloudProviderId

        :param error: Human-readable error detail when sync is unhealthy.
        :type error: str

        :param error_code: Machine-readable error code when sync is unhealthy.
        :type error_code: str

        :param gcp_bucket_name: GCS bucket name for inventory files Datadog reads.
        :type gcp_bucket_name: str

        :param gcp_project_id: GCP project ID.
        :type gcp_project_id: str

        :param gcp_service_account_email: Service account email for bucket access.
        :type gcp_service_account_email: str

        :param prefix: Object key prefix or ``/`` when the entire bucket is synced.
        :type prefix: str
        """
        super().__init__(kwargs)

        self_.aws_account_id = aws_account_id
        self_.aws_bucket_name = aws_bucket_name
        self_.aws_region = aws_region
        self_.azure_client_id = azure_client_id
        self_.azure_container_name = azure_container_name
        self_.azure_storage_account_name = azure_storage_account_name
        self_.azure_tenant_id = azure_tenant_id
        self_.cloud_provider = cloud_provider
        self_.error = error
        self_.error_code = error_code
        self_.gcp_bucket_name = gcp_bucket_name
        self_.gcp_project_id = gcp_project_id
        self_.gcp_service_account_email = gcp_service_account_email
        self_.prefix = prefix
