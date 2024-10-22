# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

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
            "namespaces": ([str],),
        }

    attribute_map = {
        "namespaces": "namespaces",
    }

    def __init__(self_, namespaces: Union[List[str], UnsetType] = unset, **kwargs):
        """
        AWS Namespaces response body

        :param namespaces: AWS CloudWatch namespace
        :type namespaces: [str], optional
        """
        if namespaces is not unset:
            kwargs["namespaces"] = namespaces
        super().__init__(kwargs)
