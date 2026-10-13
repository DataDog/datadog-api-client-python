# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DeploymentGateRuleFailureMonitor(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "state": (str,),
            "url": (str,),
        }

    attribute_map = {
        "id": "id",
        "state": "state",
        "url": "url",
    }

    def __init__(self_, id: str, state: str, url: str, **kwargs):
        """
        Failed monitor reference.

        :param id: Monitor ID.
        :type id: str

        :param state: Monitor state that caused the failure.
        :type state: str

        :param url: URL for inspecting the monitor during the evaluation window.
        :type url: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.state = state
        self_.url = url
