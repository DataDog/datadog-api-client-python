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
    from datadog_api_client.v2.model.integration_account_dataflow_status import IntegrationAccountDataflowStatus


class TwilioEventsLogsIntegrationDataflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_dataflow_status import IntegrationAccountDataflowStatus

        return {
            "enabled": (bool,),
            "status": (IntegrationAccountDataflowStatus,),
        }

    attribute_map = {
        "enabled": "enabled",
        "status": "status",
    }
    read_only_vars = {
        "status",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        status: Union[IntegrationAccountDataflowStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Twilio Event resource logs, which record virtually every action taken in your Twilio account, such as provisioning a phone number, changing account security settings, or deleting a recording. Actions are recorded whether they came from the REST API, a user in the Twilio Console, or Twilio itself. `Cloud SIEM <https://docs.datadoghq.com/security/cloud_siem/>`_ analyzes and correlates these logs to detect threats in real time.

        :param enabled: Whether Datadog collects this data.
        :type enabled: bool, optional

        :param status: Read-only collection status of a dataflow.
        :type status: IntegrationAccountDataflowStatus, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
