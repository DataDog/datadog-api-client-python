# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_recommended_test_config import DemRecommendedTestConfig


class DemRecommendedTestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_recommended_test_config import DemRecommendedTestConfig

        return {
            "config": (DemRecommendedTestConfig,),
            "created_at": (datetime,),
            "name": (str,),
            "result_id": (str,),
            "session_id": (str,),
            "source": (str,),
            "type": (str,),
            "variant_id": (str,),
        }

    attribute_map = {
        "config": "config",
        "created_at": "created_at",
        "name": "name",
        "result_id": "result_id",
        "session_id": "session_id",
        "source": "source",
        "type": "type",
        "variant_id": "variant_id",
    }

    def __init__(
        self_,
        config: DemRecommendedTestConfig,
        created_at: datetime,
        name: str,
        source: str,
        type: str,
        result_id: Union[str, UnsetType] = unset,
        session_id: Union[str, UnsetType] = unset,
        variant_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an AI-recommended synthetic test for a DEM journey.

        :param config: The browser test configuration that can be used to create the recommended test.
        :type config: DemRecommendedTestConfig

        :param created_at: The time when the recommendation was generated.
        :type created_at: datetime

        :param name: The display name of the recommended test.
        :type name: str

        :param result_id: The identifier of the validating sample run, when available.
        :type result_id: str, optional

        :param session_id: The RUM session identifier for the validating sample run, when available.
        :type session_id: str, optional

        :param source: The pipeline that produced the recommendation.
        :type source: str

        :param type: The type of synthetic test.
        :type type: str

        :param variant_id: The variant associated with the recommendation, when applicable.
        :type variant_id: str, optional
        """
        if result_id is not unset:
            kwargs["result_id"] = result_id
        if session_id is not unset:
            kwargs["session_id"] = session_id
        if variant_id is not unset:
            kwargs["variant_id"] = variant_id
        super().__init__(kwargs)

        self_.config = config
        self_.created_at = created_at
        self_.name = name
        self_.source = source
        self_.type = type
