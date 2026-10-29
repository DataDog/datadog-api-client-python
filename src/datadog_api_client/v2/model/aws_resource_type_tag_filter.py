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


class AWSResourceTypeTagFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "custom": (bool,),
            "expression": (str,),
            "resource_types": ([str],),
            "service": (str,),
        }

    attribute_map = {
        "custom": "custom",
        "expression": "expression",
        "resource_types": "resource_types",
        "service": "service",
    }

    def __init__(
        self_,
        expression: str,
        custom: Union[bool, UnsetType] = unset,
        resource_types: Union[List[str], UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Metrics Collection resource type tag filter.
        Each filter targets either a specific AWS service's resource types ( ``service`` and
        ``resource_types`` ) or custom metrics ( ``custom`` ). These two modes are mutually exclusive.
        The ``expression`` defines a tag filter that Datadog uses when collecting metrics from the
        resource types of a specified service. Wildcards, such as ``?`` (match a single character)
        and ``*`` (match multiple characters), and exclusion using ``!`` before the tag are supported.
        For example, ``env:production AND instance-type:c?.* AND !region:us-east-1``.

        :param custom: Whether the tag filter applies to custom metrics. When ``true`` , ``service`` and ``resource_types`` must be omitted.
        :type custom: bool, optional

        :param expression: The tag filter expression to apply when collecting metrics for the matching resource types.
        :type expression: str

        :param resource_types: The AWS resource types of the service to which the tag filter applies. Required when ``service`` is set. Use ``*`` as the only entry to match all resource types of the service; ``*`` cannot be combined with specific resource types.
        :type resource_types: [str], optional

        :param service: The AWS service for which the tag filter defined in ``expression`` will be applied. Required unless ``custom`` is ``true`` , and must be set together with ``resource_types``.
        :type service: str, optional
        """
        if custom is not unset:
            kwargs["custom"] = custom
        if resource_types is not unset:
            kwargs["resource_types"] = resource_types
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)

        self_.expression = expression
