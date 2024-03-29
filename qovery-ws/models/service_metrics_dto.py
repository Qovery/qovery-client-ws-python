# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List
from pydantic import BaseModel, Field, StrictStr, conlist
from qovery-ws.models.metric_dto import MetricDto

class ServiceMetricsDto(BaseModel):
    """
    ServiceMetricsDto
    """
    cpu: MetricDto = Field(...)
    memory: MetricDto = Field(...)
    pod_name: StrictStr = Field(...)
    storages: conlist(MetricDto) = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["cpu", "memory", "pod_name", "storages"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ServiceMetricsDto:
        """Create an instance of ServiceMetricsDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict['cpu'] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory
        if self.memory:
            _dict['memory'] = self.memory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in storages (list)
        _items = []
        if self.storages:
            for _item in self.storages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['storages'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServiceMetricsDto:
        """Create an instance of ServiceMetricsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceMetricsDto.parse_obj(obj)

        _obj = ServiceMetricsDto.parse_obj({
            "cpu": MetricDto.from_dict(obj.get("cpu")) if obj.get("cpu") is not None else None,
            "memory": MetricDto.from_dict(obj.get("memory")) if obj.get("memory") is not None else None,
            "pod_name": obj.get("pod_name"),
            "storages": [MetricDto.from_dict(_item) for _item in obj.get("storages")] if obj.get("storages") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


