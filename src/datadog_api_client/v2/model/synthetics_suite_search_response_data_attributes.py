# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_suite import SyntheticsSuite


class SyntheticsSuiteSearchResponseDataAttributes(ModelNormal):
    validations = {
        "total": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_suite import SyntheticsSuite

        return {
            "suites": ([SyntheticsSuite],),
            "total": (int,),
        }

    attribute_map = {
        "suites": "suites",
        "total": "total",
    }

    def __init__(
        self_, suites: Union[List[SyntheticsSuite], UnsetType] = unset, total: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Synthetics suite search response data attributes

        :param suites:
        :type suites: [SyntheticsSuite], optional

        :param total:
        :type total: int, optional
        """
        if suites is not unset:
            kwargs["suites"] = suites
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
