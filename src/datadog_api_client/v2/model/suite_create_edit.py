# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_suite import SyntheticsSuite
    from datadog_api_client.v2.model.synthetics_suite_types import SyntheticsSuiteTypes


class SuiteCreateEdit(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_suite import SyntheticsSuite
        from datadog_api_client.v2.model.synthetics_suite_types import SyntheticsSuiteTypes

        return {
            "attributes": (SyntheticsSuite,),
            "type": (SyntheticsSuiteTypes,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: SyntheticsSuite, type: SyntheticsSuiteTypes, **kwargs):
        """


        :param attributes: Object containing details about a Synthetic suite.
        :type attributes: SyntheticsSuite

        :param type: Type for the Synthetics suites responses, ``suites``.
        :type type: SyntheticsSuiteTypes
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
