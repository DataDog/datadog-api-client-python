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
    from datadog_api_client.v2.model.terraform_backend_bucket import TerraformBackendBucket


class TerraformBackendAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.terraform_backend_kind import TerraformBackendKind
        from datadog_api_client.v2.model.terraform_backend_bucket import TerraformBackendBucket

        return {
            "account_id": (str,),
            "backend_type": (TerraformBackendKind,),
            "buckets": ([TerraformBackendBucket],),
            "org_id": (str,),
            "region": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "backend_type": "backend_type",
        "buckets": "buckets",
        "org_id": "org_id",
        "region": "region",
    }

    def __init__(
        self_,
        account_id: str,
        backend_type: TerraformBackendKind,
        buckets: List[TerraformBackendBucket],
        org_id: str,
        region: str,
        **kwargs,
    ):
        """
        Terraform backend sync configuration and bucket statuses.

        :param account_id: AWS account ID that owns the S3 buckets.
        :type account_id: str

        :param backend_type: Backend type to synchronize.
        :type backend_type: TerraformBackendKind

        :param buckets: Source buckets and their synchronization statuses.
        :type buckets: [TerraformBackendBucket]

        :param org_id: Datadog organization ID.
        :type org_id: str

        :param region: AWS region containing the S3 buckets.
        :type region: str
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.backend_type = backend_type
        self_.buckets = buckets
        self_.org_id = org_id
        self_.region = region
