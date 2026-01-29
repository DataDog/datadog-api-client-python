# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IntegrationServiceNowSyncConfigPriority(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "impact_mapping": ({str: (str,)},),
            "sync_type": (str,),
            "urgency_mapping": ({str: (str,)},),
        }

    attribute_map = {
        "impact_mapping": "impact_mapping",
        "sync_type": "sync_type",
        "urgency_mapping": "urgency_mapping",
    }

    def __init__(
        self_,
        impact_mapping: Union[Dict[str, str], UnsetType] = unset,
        sync_type: Union[str, UnsetType] = unset,
        urgency_mapping: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param impact_mapping:
        :type impact_mapping: {str: (str,)}, optional

        :param sync_type:
        :type sync_type: str, optional

        :param urgency_mapping:
        :type urgency_mapping: {str: (str,)}, optional
        """
        if impact_mapping is not unset:
            kwargs["impact_mapping"] = impact_mapping
        if sync_type is not unset:
            kwargs["sync_type"] = sync_type
        if urgency_mapping is not unset:
            kwargs["urgency_mapping"] = urgency_mapping
        super().__init__(kwargs)
