# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DeploymentGateRuleFailureNarrative(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hostgroup": (str,),
            "id": (str,),
        }

    attribute_map = {
        "hostgroup": "hostgroup",
        "id": "id",
    }

    def __init__(self_, hostgroup: str, id: str, **kwargs):
        """
        Faulty deployment detection narrative reference.

        :param hostgroup: Host group associated with the narrative.
        :type hostgroup: str

        :param id: Narrative ID.
        :type id: str
        """
        super().__init__(kwargs)

        self_.hostgroup = hostgroup
        self_.id = id
