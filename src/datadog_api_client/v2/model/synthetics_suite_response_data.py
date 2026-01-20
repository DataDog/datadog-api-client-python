# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_suite import SyntheticsSuite
    from datadog_api_client.v2.model.synthetics_suite_types import SyntheticsSuiteTypes


class SyntheticsSuiteResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_suite import SyntheticsSuite
        from datadog_api_client.v2.model.synthetics_suite_types import SyntheticsSuiteTypes

        return {
            "attributes": (SyntheticsSuite,),
            "id": (str,),
            "type": (SyntheticsSuiteTypes,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsSuite, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SyntheticsSuiteTypes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Synthetics suite response data

        :param attributes: Object containing details about a Synthetic suite.
        :type attributes: SyntheticsSuite, optional

        :param id: The public ID for the suite.
        :type id: str, optional

        :param type: Type for the Synthetics suites responses, ``suites``.
        :type type: SyntheticsSuiteTypes, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
