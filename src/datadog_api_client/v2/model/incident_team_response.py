# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentTeamResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_team_response_data import IncidentTeamResponseData
        from datadog_api_client.v2.model.incident_team_included_items import IncidentTeamIncludedItems

        return {
            "data": (IncidentTeamResponseData,),
            "included": ([IncidentTeamIncludedItems],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    read_only_vars = {
        "included",
    }

    def __init__(self, data, *args, **kwargs):
        """
        Response with an incident team payload.

        :param data: Incident Team data from a response.
        :type data: IncidentTeamResponseData

        :param included: Included objects from relationships.
        :type included: [IncidentTeamIncludedItems], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentTeamResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
