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


class SecurityAgentInvestigationCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rerun": (bool,),
            "signal_id": (str,),
        }

    attribute_map = {
        "rerun": "rerun",
        "signal_id": "signal_id",
    }

    def __init__(self_, signal_id: str, rerun: Union[bool, UnsetType] = unset, **kwargs):
        """
        Attributes of the investigation to start.

        :param rerun: Start a new investigation even if the signal already has one. If the signal's investigation is still
            running, the response has that investigation instead. A rerun counts toward the monthly investigation
            limit like any investigation.
        :type rerun: bool, optional

        :param signal_id: ID of the signal to investigate, in its V1 form, which starts with ``AQ`` , or in its longer V3 form, which
            starts with ``Aw``. Investigations carry the V1 form, so their ``signal_id`` can differ from the ID you pass.
        :type signal_id: str
        """
        if rerun is not unset:
            kwargs["rerun"] = rerun
        super().__init__(kwargs)

        self_.signal_id = signal_id
