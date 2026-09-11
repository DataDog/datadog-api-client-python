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


class SnowflakeEventTableLogsIntegrationDataflowSettingsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "event_table_events_enabled": (bool,),
            "event_table_logs_enabled": (bool,),
            "event_table_logs_interval_min": (int,),
            "event_table_span_events_enabled": (bool,),
            "event_table_spans_enabled": (bool,),
        }

    attribute_map = {
        "event_table_events_enabled": "event_table_events_enabled",
        "event_table_logs_enabled": "event_table_logs_enabled",
        "event_table_logs_interval_min": "event_table_logs_interval_min",
        "event_table_span_events_enabled": "event_table_span_events_enabled",
        "event_table_spans_enabled": "event_table_spans_enabled",
    }

    def __init__(
        self_,
        event_table_events_enabled: Union[bool, UnsetType] = unset,
        event_table_logs_enabled: Union[bool, UnsetType] = unset,
        event_table_logs_interval_min: Union[int, UnsetType] = unset,
        event_table_span_events_enabled: Union[bool, UnsetType] = unset,
        event_table_spans_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings of the event table dataflow. Each record type is collected independently so that you can control ingestion costs, and every record type is ingested into Datadog as logs tagged with its ``record_type``. Only the fields provided are changed.

        :param event_table_events_enabled: Whether records with a ``record_type`` of ``event`` are collected. Defaults to ``false``.
        :type event_table_events_enabled: bool, optional

        :param event_table_logs_enabled: Whether records with a ``record_type`` of ``log`` are collected. Defaults to ``false``.
        :type event_table_logs_enabled: bool, optional

        :param event_table_logs_interval_min: How often event table records are collected, in minutes. One of ``5`` , ``15`` , ``30`` , ``60`` , or ``1440``. Defaults to ``5``.
        :type event_table_logs_interval_min: int, optional

        :param event_table_span_events_enabled: Whether records with a ``record_type`` of ``span_event`` are collected. Defaults to ``false``.
        :type event_table_span_events_enabled: bool, optional

        :param event_table_spans_enabled: Whether records with a ``record_type`` of ``span`` are collected. Defaults to ``false``.
        :type event_table_spans_enabled: bool, optional
        """
        if event_table_events_enabled is not unset:
            kwargs["event_table_events_enabled"] = event_table_events_enabled
        if event_table_logs_enabled is not unset:
            kwargs["event_table_logs_enabled"] = event_table_logs_enabled
        if event_table_logs_interval_min is not unset:
            kwargs["event_table_logs_interval_min"] = event_table_logs_interval_min
        if event_table_span_events_enabled is not unset:
            kwargs["event_table_span_events_enabled"] = event_table_span_events_enabled
        if event_table_spans_enabled is not unset:
            kwargs["event_table_spans_enabled"] = event_table_spans_enabled
        super().__init__(kwargs)
