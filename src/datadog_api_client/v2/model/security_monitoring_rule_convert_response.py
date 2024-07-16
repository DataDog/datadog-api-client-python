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


class SecurityMonitoringRuleConvertResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "terraform_content": (str,),
        }

    attribute_map = {
        "terraform_content": "terraformContent",
    }

    def __init__(self_, terraform_content: Union[str, UnsetType] = unset, **kwargs):
        """
        Result of the convert rule request containing Terraform content.

        :param terraform_content: Terraform string as a result of converting the rule from JSON.
        :type terraform_content: str, optional
        """
        if terraform_content is not unset:
            kwargs["terraform_content"] = terraform_content
        super().__init__(kwargs)
