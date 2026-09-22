# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TerraformBackendUpdateAttributes(ModelNormal):
    validations = {
        "bucket_names": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "bucket_names": ([str],),
        }

    attribute_map = {
        "bucket_names": "bucket_names",
    }

    def __init__(self_, bucket_names: List[str], **kwargs):
        """
        Replacement bucket set for a Terraform backend sync configuration.

        :param bucket_names: Complete set of S3 bucket names to synchronize. Names must be nonempty and unique.
        :type bucket_names: [str]
        """
        super().__init__(kwargs)

        self_.bucket_names = bucket_names
