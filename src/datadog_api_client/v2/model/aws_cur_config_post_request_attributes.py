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


class AwsCURConfigPostRequestAttributes(ModelNormal):
    validations = {
        "months": {
            "inclusive_maximum": 36,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "bucket_name": (str,),
            "bucket_region": (str,),
            "is_enabled": (bool,),
            "months": (int,),
            "report_name": (str,),
            "report_prefix": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "bucket_name": "bucket_name",
        "bucket_region": "bucket_region",
        "is_enabled": "is_enabled",
        "months": "months",
        "report_name": "report_name",
        "report_prefix": "report_prefix",
    }

    def __init__(
        self_,
        account_id: str,
        bucket_name: str,
        report_name: str,
        report_prefix: str,
        bucket_region: Union[str, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        months: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for AWS CUR config Post Request.

        :param account_id: The AWS account ID.
        :type account_id: str

        :param bucket_name: The AWS bucket name used to store the Cost and Usage Report.
        :type bucket_name: str

        :param bucket_region: The region the bucket is located in.
        :type bucket_region: str, optional

        :param is_enabled: Whether or not the Cloud Cost Management account is enabled.
        :type is_enabled: bool, optional

        :param months: The month of the report.
        :type months: int, optional

        :param report_name: The name of the Cost and Usage Report.
        :type report_name: str

        :param report_prefix: The report prefix used for the Cost and Usage Report.
        :type report_prefix: str
        """
        if bucket_region is not unset:
            kwargs["bucket_region"] = bucket_region
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if months is not unset:
            kwargs["months"] = months
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.bucket_name = bucket_name
        self_.report_name = report_name
        self_.report_prefix = report_prefix
