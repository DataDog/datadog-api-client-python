# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostByOrg(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_by_org_attributes import CostByOrgAttributes
        from datadog_api_client.v2.model.cost_by_org_type import CostByOrgType

        return {
            "attributes": (CostByOrgAttributes,),
            "id": (str,),
            "type": (CostByOrgType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Cost data.

        :param attributes: Cost attributes data.
        :type attributes: CostByOrgAttributes, optional

        :param id: Unique ID of the response.
        :type id: str, optional

        :param type: Type of cost data.
        :type type: CostByOrgType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CostByOrg, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
