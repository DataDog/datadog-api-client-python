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


class ObservabilityPipelineClientIdentityRule(ModelNormal):
    validations = {
        "common_names": {
            "max_items": 1000,
            "min_items": 1,
        },
        "dns_sans": {
            "max_items": 1000,
            "min_items": 1,
        },
        "name": {
            "max_length": 64,
            "min_length": 1,
        },
        "uri_sans": {
            "max_items": 1000,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "common_names": ([str],),
            "dns_sans": ([str],),
            "name": (str,),
            "uri_sans": ([str],),
        }

    attribute_map = {
        "common_names": "common_names",
        "dns_sans": "dns_sans",
        "name": "name",
        "uri_sans": "uri_sans",
    }

    def __init__(
        self_,
        name: str,
        common_names: Union[List[str], UnsetType] = unset,
        dns_sans: Union[List[str], UnsetType] = unset,
        uri_sans: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A named rule. It matches when every constraint it defines matches at least one identity in the client's certificate. It must define at least one of ``common_names`` , ``dns_sans`` , or ``uri_sans``.

        :param common_names: Patterns for the certificate subject common name. Matching is case-sensitive, and ``*`` matches any characters, including dots.
        :type common_names: [str], optional

        :param dns_sans: Patterns for DNS subject alternative names. Matching is case-insensitive, and ``*`` matches any characters within one DNS label.
        :type dns_sans: [str], optional

        :param name: Unique rule name, reported in metrics.
        :type name: str

        :param uri_sans: Patterns for URI subject alternative names. Matching is case-sensitive. ``*`` matches any characters within one path segment, and a trailing ``/**`` matches the path and everything below it. Wildcards are only supported in the path.
        :type uri_sans: [str], optional
        """
        if common_names is not unset:
            kwargs["common_names"] = common_names
        if dns_sans is not unset:
            kwargs["dns_sans"] = dns_sans
        if uri_sans is not unset:
            kwargs["uri_sans"] = uri_sans
        super().__init__(kwargs)

        self_.name = name
