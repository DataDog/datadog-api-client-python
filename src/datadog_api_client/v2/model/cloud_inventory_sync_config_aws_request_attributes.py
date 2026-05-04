# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CloudInventorySyncConfigAWSRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aws_account_id": (str,),
            "destination_bucket_name": (str,),
            "destination_bucket_region": (str,),
            "destination_prefix": (str,),
        }

    attribute_map = {
        "aws_account_id": "aws_account_id",
        "destination_bucket_name": "destination_bucket_name",
        "destination_bucket_region": "destination_bucket_region",
        "destination_prefix": "destination_prefix",
    }

    def __init__(
        self_,
        aws_account_id: str,
        destination_bucket_name: str,
        destination_bucket_region: str,
        destination_prefix: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS settings for the customer bucket that stores inventory reports.

        :param aws_account_id: AWS account ID that owns the inventory bucket.
        :type aws_account_id: str

        :param destination_bucket_name: Name of the S3 bucket containing inventory files.
        :type destination_bucket_name: str

        :param destination_bucket_region: AWS Region of the inventory bucket.
        :type destination_bucket_region: str

        :param destination_prefix: Optional object key prefix for inventory files. Use ``/`` or omit for the entire bucket.
        :type destination_prefix: str, optional
        """
        if destination_prefix is not unset:
            kwargs["destination_prefix"] = destination_prefix
        super().__init__(kwargs)

        self_.aws_account_id = aws_account_id
        self_.destination_bucket_name = destination_bucket_name
        self_.destination_bucket_region = destination_bucket_region
