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


class DataExportConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bucket_name": (str,),
            "bucket_region": (str,),
            "report_name": (str,),
            "report_prefix": (str,),
            "report_type": (str,),
        }

    attribute_map = {
        "bucket_name": "bucket_name",
        "bucket_region": "bucket_region",
        "report_name": "report_name",
        "report_prefix": "report_prefix",
        "report_type": "report_type",
    }

    def __init__(
        self_,
        bucket_name: Union[str, UnsetType] = unset,
        bucket_region: Union[str, UnsetType] = unset,
        report_name: Union[str, UnsetType] = unset,
        report_prefix: Union[str, UnsetType] = unset,
        report_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Cost and Usage Report data export configuration.

        :param bucket_name: Name of the S3 bucket where the Cost and Usage Report is stored.
        :type bucket_name: str, optional

        :param bucket_region: AWS region of the S3 bucket.
        :type bucket_region: str, optional

        :param report_name: Name of the Cost and Usage Report.
        :type report_name: str, optional

        :param report_prefix: S3 prefix where the Cost and Usage Report is stored.
        :type report_prefix: str, optional

        :param report_type: Type of the Cost and Usage Report.
        :type report_type: str, optional
        """
        if bucket_name is not unset:
            kwargs["bucket_name"] = bucket_name
        if bucket_region is not unset:
            kwargs["bucket_region"] = bucket_region
        if report_name is not unset:
            kwargs["report_name"] = report_name
        if report_prefix is not unset:
            kwargs["report_prefix"] = report_prefix
        if report_type is not unset:
            kwargs["report_type"] = report_type
        super().__init__(kwargs)
