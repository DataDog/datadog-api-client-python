# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringBatchMigrationResourceStatusCounts(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "canceled": (int,),
            "completed": (int,),
            "duplicate": (int,),
            "failed": (int,),
            "in_progress": (int,),
            "pending": (int,),
            "published": (int,),
            "publishing": (int,),
        }

    attribute_map = {
        "canceled": "canceled",
        "completed": "completed",
        "duplicate": "duplicate",
        "failed": "failed",
        "in_progress": "inProgress",
        "pending": "pending",
        "published": "published",
        "publishing": "publishing",
    }

    def __init__(
        self_,
        canceled: int,
        completed: int,
        duplicate: int,
        failed: int,
        in_progress: int,
        pending: int,
        published: int,
        publishing: int,
        **kwargs,
    ):
        """
        The number of resources of a batch migration in each status.

        :param canceled: Number of resources whose translation was canceled.
        :type canceled: int

        :param completed: Number of resources translated and ready to be published.
        :type completed: int

        :param duplicate: Number of resources identified as duplicates of an existing rule. Reserved for future use.
        :type duplicate: int

        :param failed: Number of resources whose translation failed.
        :type failed: int

        :param in_progress: Number of resources being translated.
        :type in_progress: int

        :param pending: Number of resources waiting to be translated.
        :type pending: int

        :param published: Number of resources published as Cloud SIEM detection rules.
        :type published: int

        :param publishing: Number of resources being published.
        :type publishing: int
        """
        super().__init__(kwargs)

        self_.canceled = canceled
        self_.completed = completed
        self_.duplicate = duplicate
        self_.failed = failed
        self_.in_progress = in_progress
        self_.pending = pending
        self_.published = published
        self_.publishing = publishing
