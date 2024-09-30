# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_costs_file_usage_charge_period import CustomCostsFileUsageChargePeriod
    from datadog_api_client.v2.model.custom_costs_user import CustomCostsUser


class CustomCostsFileMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_costs_file_usage_charge_period import CustomCostsFileUsageChargePeriod
        from datadog_api_client.v2.model.custom_costs_user import CustomCostsUser

        return {
            "billed_cost": (float,),
            "billing_currency": (str,),
            "charge_period": (CustomCostsFileUsageChargePeriod,),
            "name": (str,),
            "provider_names": ([str],),
            "status": (str,),
            "uploaded_at": (float,),
            "uploaded_by": (CustomCostsUser,),
        }

    attribute_map = {
        "billed_cost": "billed_cost",
        "billing_currency": "billing_currency",
        "charge_period": "charge_period",
        "name": "name",
        "provider_names": "provider_names",
        "status": "status",
        "uploaded_at": "uploaded_at",
        "uploaded_by": "uploaded_by",
    }

    def __init__(
        self_,
        billed_cost: Union[float, UnsetType] = unset,
        billing_currency: Union[str, UnsetType] = unset,
        charge_period: Union[CustomCostsFileUsageChargePeriod, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        provider_names: Union[List[str], UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        uploaded_at: Union[float, UnsetType] = unset,
        uploaded_by: Union[CustomCostsUser, UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema of a Custom Costs metadata.

        :param billed_cost: Total cost in the cost file.
        :type billed_cost: float, optional

        :param billing_currency: Currency used in the Custom Costs file.
        :type billing_currency: str, optional

        :param charge_period: Usage charge period of a Custom Costs file.
        :type charge_period: CustomCostsFileUsageChargePeriod, optional

        :param name: Name of the Custom Costs file.
        :type name: str, optional

        :param provider_names: Providers contained in the Custom Costs file.
        :type provider_names: [str], optional

        :param status: Status of the Custom Costs file.
        :type status: str, optional

        :param uploaded_at: Timestamp, in millisecond, of the upload time of the Custom Costs file.
        :type uploaded_at: float, optional

        :param uploaded_by: Metadata of the user that has uploaded the Custom Costs file.
        :type uploaded_by: CustomCostsUser, optional
        """
        if billed_cost is not unset:
            kwargs["billed_cost"] = billed_cost
        if billing_currency is not unset:
            kwargs["billing_currency"] = billing_currency
        if charge_period is not unset:
            kwargs["charge_period"] = charge_period
        if name is not unset:
            kwargs["name"] = name
        if provider_names is not unset:
            kwargs["provider_names"] = provider_names
        if status is not unset:
            kwargs["status"] = status
        if uploaded_at is not unset:
            kwargs["uploaded_at"] = uploaded_at
        if uploaded_by is not unset:
            kwargs["uploaded_by"] = uploaded_by
        super().__init__(kwargs)
