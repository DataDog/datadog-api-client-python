# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class DemJourneyTestSuiteResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "dropped_test_ids": ([str],),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "dropped_test_ids": "dropped_test_ids",
        "name": "name",
    }
    read_only_vars = {
        "created_at",
    }

    def __init__(
        self_, created_at: datetime, name: str, dropped_test_ids: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Attributes of a DEM journey test suite response.

        :param created_at: The timestamp when the test suite was created.
        :type created_at: datetime

        :param dropped_test_ids: Test IDs omitted because the caller lacks read access.
        :type dropped_test_ids: [str], optional

        :param name: The name of the test suite.
        :type name: str
        """
        if dropped_test_ids is not unset:
            kwargs["dropped_test_ids"] = dropped_test_ids
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.name = name
