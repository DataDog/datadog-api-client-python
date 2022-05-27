# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class CostByOrgAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chargeback_breakdown import ChargebackBreakdown

        return {
            "charges": ([ChargebackBreakdown],),
            "date": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
            "total_cost": (float,),
        }

    attribute_map = {
        "charges": "charges",
        "date": "date",
        "org_name": "org_name",
        "public_id": "public_id",
        "total_cost": "total_cost",
    }

    def __init__(self, *args, **kwargs):
        """
        Cost attributes data.

        :param charges: List of charges data reported for the requested month.
        :type charges: [ChargebackBreakdown], optional

        :param date: The month requested.
        :type date: datetime, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param total_cost: The total cost of products for the month.
        :type total_cost: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CostByOrgAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
