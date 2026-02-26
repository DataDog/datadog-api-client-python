# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
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
        self_, bucket_name: str, bucket_region: str, report_name: str, report_prefix: str, report_type: str, **kwargs
    ):
        """
        AWS Cost and Usage Report data export configuration.

        :param bucket_name: Name of the S3 bucket where the Cost and Usage Report is stored.
        :type bucket_name: str

        :param bucket_region: AWS region of the S3 bucket.
        :type bucket_region: str

        :param report_name: Name of the Cost and Usage Report.
        :type report_name: str

        :param report_prefix: S3 prefix where the Cost and Usage Report is stored.
        :type report_prefix: str

        :param report_type: Type of the Cost and Usage Report. Currently only ``CUR2.0`` is supported.
        :type report_type: str
        """
        super().__init__(kwargs)

        self_.bucket_name = bucket_name
        self_.bucket_region = bucket_region
        self_.report_name = report_name
        self_.report_prefix = report_prefix
        self_.report_type = report_type
