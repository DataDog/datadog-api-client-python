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
    from datadog_api_client.v2.model.entity_v3_datadog_integration_opsgenie import EntityV3DatadogIntegrationOpsgenie
    from datadog_api_client.v2.model.entity_v3_datadog_integration_pagerduty import EntityV3DatadogIntegrationPagerduty


class EntityV3Integrations(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_v3_datadog_integration_opsgenie import (
            EntityV3DatadogIntegrationOpsgenie,
        )
        from datadog_api_client.v2.model.entity_v3_datadog_integration_pagerduty import (
            EntityV3DatadogIntegrationPagerduty,
        )

        return {
            "opsgenie": (EntityV3DatadogIntegrationOpsgenie,),
            "pagerduty": (EntityV3DatadogIntegrationPagerduty,),
        }

    attribute_map = {
        "opsgenie": "opsgenie",
        "pagerduty": "pagerduty",
    }

    def __init__(
        self_,
        opsgenie: Union[EntityV3DatadogIntegrationOpsgenie, UnsetType] = unset,
        pagerduty: Union[EntityV3DatadogIntegrationPagerduty, UnsetType] = unset,
        **kwargs,
    ):
        """
        A base schema for defining third party integrations

        :param opsgenie: An Opsgenie integration schema
        :type opsgenie: EntityV3DatadogIntegrationOpsgenie, optional

        :param pagerduty: An PagerDuty integration schema
        :type pagerduty: EntityV3DatadogIntegrationPagerduty, optional
        """
        if opsgenie is not unset:
            kwargs["opsgenie"] = opsgenie
        if pagerduty is not unset:
            kwargs["pagerduty"] = pagerduty
        super().__init__(kwargs)
