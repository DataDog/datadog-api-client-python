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


class TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAwsDetail(ModelNormal):
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

    def __init__(
        self_,
        aws_account_id: Union[str, UnsetType] = unset,
        aws_bucket_name: Union[str, UnsetType] = unset,
        file_path: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Amazon Web Services S3 storage access configuration.

        :param aws_account_id: AWS account ID where the S3 bucket is located.
        :type aws_account_id: str, optional

        :param aws_bucket_name: S3 bucket containing the CSV file.
        :type aws_bucket_name: str, optional

        :param file_path: The relative file path from the S3 bucket root to the CSV file.
        :type file_path: str, optional
        """
        if aws_account_id is not unset:
            kwargs["aws_account_id"] = aws_account_id
        if aws_bucket_name is not unset:
            kwargs["aws_bucket_name"] = aws_bucket_name
        if file_path is not unset:
            kwargs["file_path"] = file_path
        super().__init__(kwargs)
