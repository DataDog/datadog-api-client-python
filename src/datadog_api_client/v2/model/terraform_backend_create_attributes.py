# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.terraform_backend_kind import TerraformBackendKind


class TerraformBackendCreateAttributes(ModelNormal):
    validations = {
        "bucket_names": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_backend_kind import TerraformBackendKind

        return {
            "account_id": (str,),
            "backend_type": (TerraformBackendKind,),
            "bucket_names": ([str],),
            "region": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "backend_type": "backend_type",
        "bucket_names": "bucket_names",
        "region": "region",
    }

    def __init__(
        self_, account_id: str, backend_type: TerraformBackendKind, bucket_names: List[str], region: str, **kwargs
    ):
        """
        Settings for a new Terraform backend sync configuration.

        :param account_id: AWS account ID that owns the S3 buckets.
        :type account_id: str

        :param backend_type: Backend type to synchronize.
        :type backend_type: TerraformBackendKind

        :param bucket_names: Complete set of S3 bucket names to synchronize. Names must be nonempty and unique.
        :type bucket_names: [str]

        :param region: AWS region containing the S3 buckets.
        :type region: str
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.backend_type = backend_type
        self_.bucket_names = bucket_names
        self_.region = region
