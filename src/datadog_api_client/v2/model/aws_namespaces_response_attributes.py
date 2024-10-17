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


class AWSNamespacesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "namespace": (str,),
        }

    attribute_map = {
        "namespace": "namespace",
    }

    def __init__(self_, namespace: Union[str, UnsetType] = unset, **kwargs):
        """
        AWS Namespaces response body

        :param namespace: AWS CloudWatch namespace
        :type namespace: str, optional
        """
        if namespace is not unset:
            kwargs["namespace"] = namespace
        super().__init__(kwargs)
