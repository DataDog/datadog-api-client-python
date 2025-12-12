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
    from datadog_api_client.v2.model.synthetics_suite_test_alerting_criticality import (
        SyntheticsSuiteTestAlertingCriticality,
    )


class SyntheticsSuiteTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_suite_test_alerting_criticality import (
            SyntheticsSuiteTestAlertingCriticality,
        )

        return {
            "alerting_criticality": (SyntheticsSuiteTestAlertingCriticality,),
            "public_id": (str,),
        }

    attribute_map = {
        "alerting_criticality": "alerting_criticality",
        "public_id": "public_id",
    }

    def __init__(
        self_,
        public_id: str,
        alerting_criticality: Union[SyntheticsSuiteTestAlertingCriticality, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing details about a Synthetic test included in a Synthetic suite.

        :param alerting_criticality: Alerting criticality for each the test.
        :type alerting_criticality: SyntheticsSuiteTestAlertingCriticality, optional

        :param public_id:
        :type public_id: str
        """
        if alerting_criticality is not unset:
            kwargs["alerting_criticality"] = alerting_criticality
        super().__init__(kwargs)

        self_.public_id = public_id
