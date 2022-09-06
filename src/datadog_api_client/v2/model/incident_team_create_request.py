# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentTeamCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_team_create_data import IncidentTeamCreateData

        return {
            "data": (IncidentTeamCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        Create request with an incident team payload.

        :param data: Incident Team data for a create request.
        :type data: IncidentTeamCreateData
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
