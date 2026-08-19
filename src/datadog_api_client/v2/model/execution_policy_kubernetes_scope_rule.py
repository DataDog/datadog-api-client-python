# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExecutionPolicyKubernetesScopeRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "target_namespaces": ([str],),
        }

    attribute_map = {
        "target_namespaces": "target_namespaces",
    }

    def __init__(self_, target_namespaces: List[str], **kwargs):
        """
        A rule restricting a Kubernetes scope to specific namespaces.

        :param target_namespaces: The Kubernetes namespaces this rule applies to.
        :type target_namespaces: [str]
        """
        super().__init__(kwargs)

        self_.target_namespaces = target_namespaces
