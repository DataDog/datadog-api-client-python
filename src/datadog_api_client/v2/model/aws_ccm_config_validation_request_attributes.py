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


class AWSCcmConfigValidationRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "bucket_name": (str,),
            "bucket_region": (str,),
            "report_name": (str,),
            "report_prefix": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "bucket_name": "bucket_name",
        "bucket_region": "bucket_region",
        "report_name": "report_name",
        "report_prefix": "report_prefix",
    }

    def __init__(
        self_,
        account_id: str,
        bucket_name: str,
        bucket_region: str,
        report_name: str,
        report_prefix: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an AWS CCM config validation request.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str

        :param bucket_name: Name of the S3 bucket where the Cost and Usage Report is stored.
        :type bucket_name: str

        :param bucket_region: AWS region of the S3 bucket.
        :type bucket_region: str

        :param report_name: Name of the Cost and Usage Report.
        :type report_name: str

        :param report_prefix: S3 prefix where the Cost and Usage Report is stored.
        :type report_prefix: str, optional
        """
        if report_prefix is not unset:
            kwargs["report_prefix"] = report_prefix
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.bucket_name = bucket_name
        self_.bucket_region = bucket_region
        self_.report_name = report_name
