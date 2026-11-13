# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_refresh_status import ExperimentsBanditRefreshStatus


class ExperimentsBanditRefreshV2(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_refresh_status import ExperimentsBanditRefreshStatus

        return {
            "created_at": (datetime,),
            "ended_at": (datetime, none_type),
            "id": (UUID,),
            "started_at": (datetime, none_type),
            "status": (ExperimentsBanditRefreshStatus,),
        }

    attribute_map = {
        "created_at": "created_at",
        "ended_at": "ended_at",
        "id": "id",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(
        self_,
        created_at: datetime,
        ended_at: Union[datetime, none_type],
        id: UUID,
        started_at: Union[datetime, none_type],
        status: ExperimentsBanditRefreshStatus,
        **kwargs,
    ):
        """
        The most recently started refresh. Null until one starts.

        :param created_at: When the refresh was requested.
        :type created_at: datetime

        :param ended_at: When the refresh finished. Null while it runs.
        :type ended_at: datetime, none_type

        :param id: The refresh ID.
        :type id: UUID

        :param started_at: When the refresh started running. Null while it is pending.
        :type started_at: datetime, none_type

        :param status: The status of the refresh.
        :type status: ExperimentsBanditRefreshStatus
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.ended_at = ended_at
        self_.id = id
        self_.started_at = started_at
        self_.status = status
