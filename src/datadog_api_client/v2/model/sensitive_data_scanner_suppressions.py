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


class SensitiveDataScannerSuppressions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ends_with": ([str],),
            "exact_match": ([str],),
            "starts_with": ([str],),
        }

    attribute_map = {
        "ends_with": "ends_with",
        "exact_match": "exact_match",
        "starts_with": "starts_with",
    }

    def __init__(
        self_,
        ends_with: Union[List[str], UnsetType] = unset,
        exact_match: Union[List[str], UnsetType] = unset,
        starts_with: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing the suppressions for a rule. There are three types of suppressions, ``starts_with`` , ``ends_with`` , and ``exact_match``.
        Suppressed matches are not obfuscated, counted in metrics, or displayed in the Findings page.

        :param ends_with: List of strings to use for suppression of matches ending with these strings.
        :type ends_with: [str], optional

        :param exact_match: List of strings to use for suppression of matches exactly matching these strings.
        :type exact_match: [str], optional

        :param starts_with: List of strings to use for suppression of matches starting with these strings.
        :type starts_with: [str], optional
        """
        if ends_with is not unset:
            kwargs["ends_with"] = ends_with
        if exact_match is not unset:
            kwargs["exact_match"] = exact_match
        if starts_with is not unset:
            kwargs["starts_with"] = starts_with
        super().__init__(kwargs)
