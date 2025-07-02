# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSIntegrationIamPermissionsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "permissions": ([str],),
        }

    attribute_map = {
        "permissions": "permissions",
    }

    def __init__(self_, permissions: List[str], **kwargs):
        """
        AWS Integration IAM Permissions response attributes.

        :param permissions: List of AWS IAM permissions required for the integration.
        :type permissions: [str]
        """
        super().__init__(kwargs)

        self_.permissions = permissions
