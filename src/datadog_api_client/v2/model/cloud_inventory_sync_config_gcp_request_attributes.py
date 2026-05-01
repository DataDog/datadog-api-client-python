# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudInventorySyncConfigGCPRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "destination_bucket_name": (str,),
            "project_id": (str,),
            "service_account_email": (str,),
            "source_bucket_name": (str,),
        }

    attribute_map = {
        "destination_bucket_name": "destination_bucket_name",
        "project_id": "project_id",
        "service_account_email": "service_account_email",
        "source_bucket_name": "source_bucket_name",
    }

    def __init__(
        self_,
        destination_bucket_name: str,
        project_id: str,
        service_account_email: str,
        source_bucket_name: str,
        **kwargs,
    ):
        """
        GCP settings for buckets involved in inventory reporting.

        :param destination_bucket_name: GCS bucket name where Datadog reads inventory reports.
        :type destination_bucket_name: str

        :param project_id: GCP project ID for the inventory destination bucket.
        :type project_id: str

        :param service_account_email: Service account email used to read the destination bucket.
        :type service_account_email: str

        :param source_bucket_name: GCS bucket name that inventory reports are generated for.
        :type source_bucket_name: str
        """
        super().__init__(kwargs)

        self_.destination_bucket_name = destination_bucket_name
        self_.project_id = project_id
        self_.service_account_email = service_account_email
        self_.source_bucket_name = source_bucket_name
