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


class DeviceEmployee(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "city": (str,),
            "country": (str,),
            "department": (str,),
            "email": (str,),
            "name": (str,),
            "office": (str,),
            "team": (str,),
        }

    attribute_map = {
        "city": "city",
        "country": "country",
        "department": "department",
        "email": "email",
        "name": "name",
        "office": "office",
        "team": "team",
    }

    def __init__(
        self_,
        city: Union[str, UnsetType] = unset,
        country: Union[str, UnsetType] = unset,
        department: Union[str, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        office: Union[str, UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Directory information about the employee associated with the device,
        sourced from a customer reference table.
        Absent when no reference table is configured or the device has no match.

        :param city: City where the employee is based.
        :type city: str, optional

        :param country: Country where the employee is based.
        :type country: str, optional

        :param department: Department the employee belongs to.
        :type department: str, optional

        :param email: Email address of the employee.
        :type email: str, optional

        :param name: Full name of the employee.
        :type name: str, optional

        :param office: Office the employee is assigned to.
        :type office: str, optional

        :param team: Team the employee belongs to.
        :type team: str, optional
        """
        if city is not unset:
            kwargs["city"] = city
        if country is not unset:
            kwargs["country"] = country
        if department is not unset:
            kwargs["department"] = department
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        if office is not unset:
            kwargs["office"] = office
        if team is not unset:
            kwargs["team"] = team
        super().__init__(kwargs)
