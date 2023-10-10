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
    from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie import ServiceDefinitionV2Dot2Opsgenie
    from datadog_api_client.v2.model.service_definition_v2_dot2_pagerduty import ServiceDefinitionV2Dot2Pagerduty


class ServiceDefinitionV2Dot2Integrations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie import ServiceDefinitionV2Dot2Opsgenie
        from datadog_api_client.v2.model.service_definition_v2_dot2_pagerduty import ServiceDefinitionV2Dot2Pagerduty

        return {
            "opsgenie": (ServiceDefinitionV2Dot2Opsgenie,),
            "pagerduty": (ServiceDefinitionV2Dot2Pagerduty,),
        }

    attribute_map = {
        "opsgenie": "opsgenie",
        "pagerduty": "pagerduty",
    }

    def __init__(
        self_,
        opsgenie: Union[ServiceDefinitionV2Dot2Opsgenie, UnsetType] = unset,
        pagerduty: Union[ServiceDefinitionV2Dot2Pagerduty, UnsetType] = unset,
        **kwargs,
    ):
        """
        Third party integrations that Datadog supports.

        :param opsgenie: Opsgenie integration for the service.
        :type opsgenie: ServiceDefinitionV2Dot2Opsgenie, optional

        :param pagerduty: PagerDuty integration for the service.
        :type pagerduty: ServiceDefinitionV2Dot2Pagerduty, optional
        """
        if opsgenie is not unset:
            kwargs["opsgenie"] = opsgenie
        if pagerduty is not unset:
            kwargs["pagerduty"] = pagerduty
        super().__init__(kwargs)
