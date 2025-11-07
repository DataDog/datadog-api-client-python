# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aws_account_id": (str,),
            "aws_bucket_name": (str,),
            "file_path": (str,),
        }

    attribute_map = {
        "aws_account_id": "aws_account_id",
        "aws_bucket_name": "aws_bucket_name",
        "file_path": "file_path",
    }

    def __init__(self_, aws_account_id: str, aws_bucket_name: str, file_path: str, **kwargs):
        """
        Amazon Web Services S3 storage access configuration.

        :param aws_account_id: AWS account ID where the S3 bucket is located.
        :type aws_account_id: str

        :param aws_bucket_name: S3 bucket containing the CSV file.
        :type aws_bucket_name: str

        :param file_path: The relative file path from the S3 bucket root to the CSV file.
        :type file_path: str
        """
        super().__init__(kwargs)

        self_.aws_account_id = aws_account_id
        self_.aws_bucket_name = aws_bucket_name
        self_.file_path = file_path
