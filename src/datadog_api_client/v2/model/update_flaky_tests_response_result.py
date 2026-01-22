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


class UpdateFlakyTestsResponseResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error": (str,),
            "id": (str,),
            "success": (bool,),
        }

    attribute_map = {
        "error": "error",
        "id": "id",
        "success": "success",
    }

    def __init__(self_, id: str, success: bool, error: Union[str, UnsetType] = unset, **kwargs):
        """
        Result of updating a single flaky test state.

        :param error: Error message if the update failed.
        :type error: str, optional

        :param id: The ID of the flaky test from the request. This is the same ID returned by the Search flaky tests endpoint and corresponds to the test_fingerprint_fqn field in test run events.
        :type id: str

        :param success: ``True`` if the update was successful, ``False`` if there were any errors.
        :type success: bool
        """
        if error is not unset:
            kwargs["error"] = error
        super().__init__(kwargs)

        self_.id = id
        self_.success = success
