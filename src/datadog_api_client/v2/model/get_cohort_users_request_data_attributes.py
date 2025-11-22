# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition import (
        GetCohortUsersRequestDataAttributesDefinition,
    )
    from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_time import (
        GetCohortUsersRequestDataAttributesTime,
    )


class GetCohortUsersRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition import (
            GetCohortUsersRequestDataAttributesDefinition,
        )
        from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_time import (
            GetCohortUsersRequestDataAttributesTime,
        )

        return {
            "data_source": (str,),
            "definition": (GetCohortUsersRequestDataAttributesDefinition,),
            "execution": (int,),
            "time": (GetCohortUsersRequestDataAttributesTime,),
            "user_selection": (str,),
            "window_size": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "definition": "definition",
        "execution": "execution",
        "time": "time",
        "user_selection": "user_selection",
        "window_size": "window_size",
    }

    def __init__(
        self_,
        data_source: Union[str, UnsetType] = unset,
        definition: Union[GetCohortUsersRequestDataAttributesDefinition, UnsetType] = unset,
        execution: Union[int, UnsetType] = unset,
        time: Union[GetCohortUsersRequestDataAttributesTime, UnsetType] = unset,
        user_selection: Union[str, UnsetType] = unset,
        window_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data_source:
        :type data_source: str, optional

        :param definition:
        :type definition: GetCohortUsersRequestDataAttributesDefinition, optional

        :param execution:
        :type execution: int, optional

        :param time:
        :type time: GetCohortUsersRequestDataAttributesTime, optional

        :param user_selection:
        :type user_selection: str, optional

        :param window_size:
        :type window_size: str, optional
        """
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if definition is not unset:
            kwargs["definition"] = definition
        if execution is not unset:
            kwargs["execution"] = execution
        if time is not unset:
            kwargs["time"] = time
        if user_selection is not unset:
            kwargs["user_selection"] = user_selection
        if window_size is not unset:
            kwargs["window_size"] = window_size
        super().__init__(kwargs)
