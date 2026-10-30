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


class AWSCloudAuthIntakeMappingAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arn_pattern": (str,),
            "par_enrollment_enabled": (bool,),
        }

    attribute_map = {
        "arn_pattern": "arn_pattern",
        "par_enrollment_enabled": "par_enrollment_enabled",
    }
    read_only_vars = {
        "par_enrollment_enabled",
    }

    def __init__(self_, arn_pattern: str, par_enrollment_enabled: Union[bool, UnsetType] = unset, **kwargs):
        """
        Attributes for AWS cloud authentication intake mapping response.

        :param arn_pattern: AWS caller ARN pattern allowed to authenticate for telemetry submission. ARN syntax and AWS integration membership are validated by the server. For an assumed role, use the STS assumed-role ARN with a trailing /* wildcard to match its sessions.
        :type arn_pattern: str

        :param par_enrollment_enabled: Whether the mapping allows Private Action Runner enrollment. This attribute may be omitted when enrollment is disabled. Enrollment permission is managed separately from the ARN pattern.
        :type par_enrollment_enabled: bool, optional
        """
        if par_enrollment_enabled is not unset:
            kwargs["par_enrollment_enabled"] = par_enrollment_enabled
        super().__init__(kwargs)

        self_.arn_pattern = arn_pattern
