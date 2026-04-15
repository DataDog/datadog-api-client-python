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


class FlakyTestsSearchFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_history": (bool,),
            "query": (str,),
        }

    attribute_map = {
        "include_history": "include_history",
        "query": "query",
    }

    def __init__(
        self_, include_history: Union[bool, UnsetType] = unset, query: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Search filter settings.

        :param include_history: Whether to include the status change history for each flaky test in the response.
            When set to true, each test will include a ``history`` array with chronological status changes.
            Defaults to false.
        :type include_history: bool, optional

        :param query: Search query following log syntax used to filter flaky tests, same as on Flaky Tests Management UI. The supported search keys are:

            * ``flaky_test_state``
            * ``flaky_test_category``
            * ``@test.name``
            * ``@test.suite``
            * ``@test.module``
            * ``@test.service``
            * ``@git.repository.id_v2``
            * ``@git.branch``
            * ``@test.codeowners``
            * ``env``
        :type query: str, optional
        """
        if include_history is not unset:
            kwargs["include_history"] = include_history
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
